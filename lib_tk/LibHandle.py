# # -*- coding: utf-8 -*-
"""


"""
import os, urllib, urllib2, re, sys, yaml, logging, zipfile
from tk import appFuncs as func

try:
    from pyunpack import Archive
except ImportError:
    from tk import appFuncs as func

    func.checkPackageInstall('pyunpack')
else:
    pass

# We can configure the current level to make it disable certain logs when we don't want it.
logging.basicConfig()
logger = logging.getLogger(__file__)
logger.setLevel(logging.DEBUG)


class LibHandle(object):
    def __init__(self):

        super(LibHandle, self).__init__()

        if os.getenv('PIPELINE_TOOL') is None:
            self.configLibPth = os.getcwd()
        else:
            self.configLibPth = os.path.join(os.getenv('PIPELINE_TOOL'), 'lib_tk')

        # print self.configLibPth, os.path.exists(self.configLibPth)

        self.lib_root = os.getcwd()

        self.inspectLibrary()

        # self.libDataFilePth = os.path.join(self.configLibPth, '__vmm__.yml')
        #
        # with open(libDataFilePth, 'w') as f:
        #     yaml.dump(vmm_List, f, default_flow_style=False)
        #
        # with open(self.libDataFilePth, 'r') as f:
        #     urls = yaml.load(f)
        #
        # download_files = self.batchDownloadFiles(urls, self.configLibPth)

    def inspectLibrary(self, *args):

        sections = ['__vmm__', '__tex__', '__hdri__', '__alpha__']

        for lib in sections:
            dataDir = os.path.join(os.getenv('PIPELINE_TOOL'), 'sql_tk/lib/%s.config.yml' % lib)

            with open(dataDir, 'r') as f:
                checkList = yaml.load(f)

            libDir = os.path.join(os.getenv('PIPELINE_TOOL'), 'lib_tk/%s' % lib)

            filePths = func.getfilePath(libDir)

            missing = []
            checked = []

            for f in checkList:
                if f in filePths:
                    checked.append(f)
                else:
                    missing.append(f)

            if len(missing)==0:
                logger.info('%s is checked, no missing')
            else:
                for f in missing:
                    logger.info('missing %s' % f)

    def batchDownload(self, urls, directory=None, *args):
        if directory is None:
            directory = os.path.join(os.getenv('PIPELINE_TOOL'), 'lib_tk')

        download_files = []

        if type(urls) == 'str':
            # print urls
            file_name = urls.split('/')[-1]
            # print file_name
            file_path = os.path.join(directory, file_name)
            # print file_path
            doDL = urllib.urlretrieve(urls, file_path)
            print "Finish downloading: %s" % str(doDL)
            download_files.append(file_path)
        else:
            for url in urls:
                # print url
                file_name = url.split('/')[-1]
                # print file_name
                file_path = os.path.join(directory, file_name)
                # print file_path
                doDL = urllib.urlretrieve(url, file_path)
                # print file_path
                download_files.append(file_path)
                print "Finish downloading: %s" % str(doDL)

        return download_files

    def extactingFiles(self, inDir, file_name, outDir, *args):

        Archive(os.path.join(inDir, file_name)).extractall(outDir)

    def link_detect(self, url, *args):

        website = urllib2.urlopen(url)

        html = website.read()

        links = re.findall("((http|ftp)s?://.*?)", html)

        getLinks = [f[0] for f in links]

        return getLinks


def initialize():
    LibHandle()


if __name__ == '__main__':
    initialize()

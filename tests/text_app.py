# -*- coding: utf-8 -*-
"""

Script Name: text_app.py
Author: Do Trinh/Jimmy - 3D artist.

Description:

    a test file corresponding to app.py in source directory

"""
# -------------------------------------------------------------------------------------------------------------
from .context import PLM


def test_app(capsys, example_fixture):
    # pylint: disable=W0612,W0613
    PLM.PLM.run()
    captured = capsys.readouterr()

    assert "Hello World..." in captured.out

# -------------------------------------------------------------------------------------------------------------
# Created by panda on 3/16/2020 - 2:18 AM
# © 2017 - 2019 DAMGteam. All rights reserved
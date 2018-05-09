#!/usr/bin/env python3# -*- coding: utf-8 -*-"""Script Name: sql_local.pyAuthor: Do Trinh/Jimmy - 3D artist.Description:    This script is main file to create, modify and/or query local data"""# -------------------------------------------------------------------------------------------------------------""" About Plt """__root__ = "PLT_RT"# -------------------------------------------------------------------------------------------------------------""" Import modules """# Pythonimport loggingimport osimport shutilimport requestsimport sqlite3 as lite# -------------------------------------------------------------------------------------------------------------""" Configure the current level to make it disable certain log """logPth = os.path.join(os.getenv(__root__), 'appData', 'logs', 'utils_sql.log')logger = logging.getLogger('utils_sql')handler = logging.FileHandler('utils_sql')formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')handler.setFormatter(formatter)logger.addHandler(handler)logger.setLevel(logging.DEBUG)# -------------------------------------------------------------------------------------------------------------""" Plt tools """from utilities import utils as func# -------------------------------------------------------------------------------------------------------------""" Variables """dataPth = os.path.join(os.getenv(__root__), 'appData', 'plt.db')conn = lite.connect(dataPth)conn.text_factory = lambda x: (x, 'utf-8', 'ignore')c = conn.cursor()USERCLASSDATA = ['Tester, DemoUser, NormalUser', 'Artist', 'Instructor', 'CEO', 'Supervisor', 'Leader']questions = ["What is zero divided by zero?",             "How much wood would a woodchuck chuck if a woodchuck could chuck wood?",            "I’m drunk?", "Make me a sandwich?", "Read me a haiku?", "What’s your favorite movie?", "What is ‘Inception’ about?",            "Do you have a boyfriend?", "Do you have any pets?", "What is your favorite animal?", "What are you wearing?",            "I’m naked", "Do you follow the three laws of robotics?", "Do you believe in God?", "What is the meaning of life?",            "When will the world end?", "What is the best operating system?", "What phone is the best?", "What’s better: Windows or Mac?",            "Tell me a story?", "Beatbox?", "I am your father!", "What came first: The chicken or the egg?",            "What do you think about Google Now?", "Where is Elvis Presley?", "Are you her?", "Where did I put my keys?",            "How many Apple Store geniuses does it take to screw in a lightbulb?", "How do I look?", "What are you doing later?",            "What is your best pickup line?", "Are you on Facebook?", "Are you intelligent?", "Are you serious?",            "Are you stupid?", "Is John Snow dead?", "Is winter coming?", "What are you afraid of?", "Are you human?",            "Blah blah blah blah.", "Do I look good in this dress?", "Do these pants make me look fat?", "Do you prefer iPhone or Mac?",            "Do you like the Apple Watch?", "Can you sing?", "Why am I here?", "What can you answer?",]# -------------------------------------------------------------------------------------------------------------""" DELETE """def remove_data_table(tableName):    # Delete old data first    c.execute("SELECT * FROM {tableName}".format(tableName=tableName))    c.fetchall()    c.execute("DELETE FROM {tableName}".format(tableName=tableName))    conn.commit()    insert_timeLog('Clean data in table: %s' % tableName)# -------------------------------------------------------------------------------------------------------------""" CREATE """def create_username_table(username):    c.execute("CREATE TABLE IF NOT EXISTS {username} (password TEXT, firstname TEXT, lastname TEXT, title TEXT,"    "email TEXT, phone TEXT, address1 TEXT, address2 TEXT, postal TEXT, city TEXT, country TEXT)".format(username=username))    logger.info("table %s created" % username)    conn.commit()def create_userData_table():    c.execute("CREATE TABLE IF NOT EXISTS userData (username TEXT, date_create TEXT, unix TEXT, token TEXT, "              "question1 TEXT, answer1 TEXT, question2 TEXT, answer2 TEXT)")    logger.info("table userData created")    conn.commit()def create_userSetting_table():    c.execute("CREATE TABLE IF NOT EXISTS userSetting (username TEXT, showToolbar TXT, avatar TEXT)")    logger.info("table userSetting created")    conn.commit()def create_userLog_table():    c.execute("CREATE TABLE IF NOT EXISTS userLog (username TEXT, date TEXT, login TEXT, logout TEXT)")    logger.info("table userLog created")    conn.commit()def create_userClass_table():    c.execute("CREATE TABLE IF NOT EXISTS userClass (username TEXT, class TEXT, status TEXT)")    logger.info("table userClass created")    conn.commit()def create_curUser_table():    c.execute("CREATE TABLE IF NOT EXISTS curUser (username TEXT, auto_login TEXT)")    logger.info("table curUser created")    conn.commit()def create_timeLog_table():    c.execute("CREATE TABLE IF NOT EXISTS timeLog (dateTime TEXT , username TEXT, eventlog TEXT)")    logger.info("table timeLog created")    conn.commit()def create_tokenID_table():    c.execute("CREATE TABLE IF NOT EXISTS tokenID (token TEXT, username TEXT, timelog TEXT, productID TEXT, ip TEXT, "              "city TEXT, country TEXT)")    logger.info("table tokenID created")    conn.commit()def create_pcID_table():    c.execute("CREATE TABLE IF NOT EXISTS pcID (token TEXT, productID TEXT, os TEXT, pcUser TEXT, python TEXT)")    logger.info("table pcID created")    conn.commit()# Projectdef create_prjLst_table():    c.execute("CREATE TABLE IF NOT EXISTS prjLst (status TEXT, projName TEXT, start TEXT, end TEXT )")    logger.info("table prjLst created")    conn.commit()def create_prjCrew_table():    c.execute("CREATE TABLE IF NOT EXISTS projCrew (projID TEXT, username TEXT, position TEXT)")    logger.info("table projCrew created")    conn.commit()def create_prjTaskID_table( projName):    c.execute("CREATE TABLE IF NOT EXISTS {projName} (projStage TEXT, assetID TEXT, shotID TEXT, taskID TEXT, "              "status TEXT, assign TEXT, start TEXT, end TEXT)".format(projName=projName))    logger.info("table %s created" % projName)    conn.commit()# Configurationdef create_pltConfig_table():    c.execute("CREATE TABLE IF NOT EXISTS pltConfig (appName TEXT, version VARCHAR(20), exePth VARCHAR(20))")    logger.info("table plt created")    conn.commit()def create_tableConfig_table():    c.execute("CREATE TABLE IF NOT EXISTS tableConfig (tableName TEXT, columnList TEXT, datetimeLog TEXT)")    logger.info("table tableConfig created")    conn.commit()def create_dataConfig_table():    c.execute("CREATE TABLE IF NOT EXISTS dataConfig (setup TEXT, account TEXT, message TEXT, name TEXT, format TEXT)")    logger.info("table dataConfig created")    conn.commit()# Librarydef create_questions_library():    c.execute("CREATE TABLE IF NOT EXISTS security_questions (questionLst TEXT, update_by TEXT, datetime TEXT)")    logger.info("table questions created")    conn.commit()# New userdef create_user_token_table():    c.execute("CREATE TABLE IF NOT EXISTS userTokenLogin (username TEXT, token TEXT, cookie TEXT)")    conn.commit()def create_new_user_data(data):    create_username_table(data[0])    c.execute("INSERT INTO {username} (password, firstname, lastname, title, email, phone, address1, address2, "              "postal, city, country) VALUES (?,?,?,?,?,?,?,?,?,?,?)".format(username=data[0]),        (data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11]))    c.execute("INSERT INTO tokenID (token, username, timelog, productID, ip, city, country) VALUES (?,?,?,?,?,?,?)",              (data[12], data[0], data[13], data[14], data[15], data[16], data[17]))    c.execute("INSERT INTO userData (username, unix, token, question1, answer1, question2, answer2, dateCreate) "              "VALUES (?,?,?,?,?,?,?,?)", (data[0], data[18], data[12], data[19], data[20], data[21], data[22], data[23]))    c.execute("INSERT INTO pcid (token, productid, os, pcuser, python) VALUES (?,?,?,?,?)", (data[12], data[14],                                    data[24], data[25], data[26]))    c.execute("INSERT INTO curUser (username, autoLogin) VALUES (?,?)", (data[0], False))    c.execute("INSERT INTO userClass (username, class, status) VALUES (?,?,?)",(data[0], "Normal User", "Good"))    avatarPth = func.get_avatar(data[0])    if not os.path.exists(avatarPth):        shutil.copy2(data[27], avatarPth)    else:        if func.check_match(avatarPth, data[27]):            pass        else:            os.rename(avatarPth, avatarPth + '.old')            shutil.copy2(data[27], avatarPth)    logger.info("Created table for %s" % data[0])    conn.commit()# -------------------------------------------------------------------------------------------------------------""" QUERY """# Query Table infodef query_tableLst():    c.execute("SELECT name FROM sqlite_master WHERE type='table';")    return [str(t[0]) for t in c.fetchall()]def query_columnLst(tableName):    c.execute("SELECT * FROM {tn}".format(tn=tableName))    return [str(m[0]) for m in c.description]# Query user infodef query_curUser():    c.execute("SELECT * FROM curUser")    data = c.fetchall()    if len(data) == 0:        user = ""        rememberLogin = False    else:        userData = [str(p[0]) for p in list(data[0])]        user = userData[0].split("b'")[1].split("'")[0]        rememberLogin = func.str2bool(userData[1].split("b'")[1].split("'")[0])    return user, rememberLogindef query_userClass(username):    c.execute("SELECT * FROM userClass")    rows = c.fetchall()    for row in rows:        if username == row[0]:            return str(row[1]).split("'")[0]        else:            return Nonedef query_userStatus(username):    c.execute("SELECT * FROM userClass")    rows = c.fetchall()    for row in rows:        if username == row[0]:            return str(row[2])        else:            return 'Good'def query_userData(username=None):    if username == None:        data = query_curUser()        user = data[0]    c.execute("SELECT * FROM userData")    data = [r for r in c.fetchall()]    for accountData in data:        if accountData[0] == user:            return accountDatadef query_userList():    c.execute("SELECT username FROM userData")    return [str(r[0]) for r in c.fetchall()]# Query account infodef query_unixLst():    c.execute("SELECT unix FROM userData")    return [str(r[0]) for r in c.fetchall()]def query_tokenLst():    c.execute("SELECT token FROM userData")    return [str(r[0]) for r in c.fetchall()]# Query security questions & andswer:def query_questions(username=None):    userdata = query_userData(username)    return userdata[4], userdata[6]def query_answers(username=None):    userdata = query_userData(username)    return userdata[5], userdata[7]def query_all_questions():    c.execute("SELECT questionLst FROM security_questions")    return [r[0] for r in c.fetchall()]def query_user_session():    c.execute("SELECT * FROM userTokenLogin")    d = c.fetchall()    if len(d) == 0 or d is None or d is []:        username = None        token = None        cookie = None    else:        data = d[0]        username = str(data[0][0]).split("b'")[-1].split("'")[0]        token = str(data[1][0]).split("b'")[-1].split("'")[0]        cookie = str(data[2][0]).split("b'")[-1].split("'")[0]    return username, token, cookie# -------------------------------------------------------------------------------------------------------------""" ADDING """# Build databasedef insert_questions_library(question, source=None):    username = query_curUser()[0]    timeLog = func.get_datetime()    if source == None:        source = 'Internet'    c.execute("INSERT INTO questions (questionLst, timeLog, uploadBy, source) VALUES (?,?,?,?)",              (question, timeLog, username, source))    conn.commit()def insert_timeLog(eventlog):    username = query_curUser()[0]    datetimeLog = func.get_datetime()    c.execute("INSERT INTO TimeLog (dateTime, username, eventLog) VALUES (?,?,?)",              (datetimeLog, username, eventlog))    conn.commit()    return True# -------------------------------------------------------------------------------------------------------------""" UPDATE """def update_tableConfig_table():    remove_data_table("tableConfig")    tableLst = query_tableLst()    for table in tableLst:        columnLst = query_columnLst(table)        content = '|'.join(columnLst)        timelog = func.get_datetime()        c.execute("INSERT INTO tableConfig (tableName, columnList, datetimeLog) VALUES (?,?,?)",                  (table, content, timelog))        conn.commit()def update_remember_login(username, param):    remove_data_table('curUser')    c.execute("INSERT INTO curUser (username, autoLogin) VALUES (?,?)", (username, param))    conn.commit()def update_questions_library_begin_set():    c.execute("CREATE TABLE IF NOT EXISTS security_questions (questionLst TEXT, update_by TEXT, datetime TEXT, sources TEXT)")    curUser = query_curUser()[0]    sources = 'Internet'    for question in questions:        datetime = func.get_datetime()        c.execute("INSERT INTO security_questions (questionLst, update_by, datetime, sources) VALUES (?, ?, ?, ?)",                  (question, curUser, datetime, sources))    conn.commit()def update_user_token(username, token, cookie):    create_user_token_table()    remove_data_table('userTokenLogin')    c.execute("INSERT INTO userTokenLogin (username, token, cookie) VALUES (?,?,?)", (username, token, cookie))    conn.commit()# -------------------------------------------------------------------------------------------------------------""" CHECK """def check_account(username):    userList = query_userList()    if username in userList:        return True    else:        return Falsedef check_status(username):    userStatus = query_userStatus(username)    if userStatus == 'Block':        return False    else:        return Truedef check_pw_match(username, password):    # c.execute("SELECT password FROM {username}".format(username=username))    # data = c.fetchall()    # passwordCheck = func.hex_to_text(str((data[0])[0]))    # check = func.check_match(passwordCheck, password)    # return check    post = requests.get('<MY_URI>', headers={'Authorization': 'Bearer <MY_TOKEN>'})def logout_account():    username, token, cookie = query_user_session()    r = requests.get("https://pipeline.damgteam.com/logout", verify=False,                     headers={'Authorization': 'Bearer %s' % token}, cookies={'connect.sid': cookie})    if r.status_code == 200:        return True    else:        return False
import sqlite3
import os


def iter_docs(topdir):
    result = []
    for fn in os.listdir(topdir):
        if(fn.find('.txt')!=-1):
            fin = open(os.path.join(topdir, fn), 'rb')
            text = fin.read()
            array = text.split('\n')
            result.append(array)
            fin.close()
    for list in result:
        del list[1]
        list[0] = list[0][0:list[0].find(' ID')]
        for i in range(1, 11):
            list[i] = list[i][list[i].find(' ') + 1: list[i].find(':')]
    return result


def get_db():
    conn = sqlite3.connect('recomd.db')
    print "Opened database successfully"

    conn.execute('''DROP TABLE IF EXISTS che;''')
    conn.execute('''DROP TABLE IF EXISTS RECMDLIST_1;''')
    conn.execute('''CREATE TABLE RECMDLIST_1
        (ID INT PRIMARY KEY     NOT NULL,
        TARGET_PERSON     CHAR(50),
        PERSON1        CHAR(50),
        PERSON2        CHAR(50),
        PERSON3        CHAR(50),
        PERSON4        CHAR(50),
        PERSON5        CHAR(50),
        PERSON6        CHAR(50),
        PERSON7        CHAR(50),
        PERSON8        CHAR(50),
        PERSON9        CHAR(50),
        PERSON10        CHAR(50));''')


    conn.execute('''DROP TABLE IF EXISTS RECMDLIST_2;''')
    conn.execute('''CREATE TABLE RECMDLIST_2
        (ID INT PRIMARY KEY     NOT NULL,
        TARGET_PERSON     CHAR(50),
        PERSON1        CHAR(50),
        PERSON2        CHAR(50),
        PERSON3        CHAR(50),
        PERSON4        CHAR(50),
        PERSON5        CHAR(50),
        PERSON6        CHAR(50),
        PERSON7        CHAR(50),
        PERSON8        CHAR(50),
        PERSON9        CHAR(50),
        PERSON10        CHAR(50));''')


    conn.execute('''DROP TABLE IF EXISTS RECMDLIST_3;''')
    conn.execute('''CREATE TABLE RECMDLIST_3
        (ID INT PRIMARY KEY     NOT NULL,
        TARGET_PERSON     CHAR(50),
        PERSON1        CHAR(50),
        PERSON2        CHAR(50),
        PERSON3        CHAR(50),
        PERSON4        CHAR(50),
        PERSON5        CHAR(50),
        PERSON6        CHAR(50),
        PERSON7        CHAR(50),
        PERSON8        CHAR(50),
        PERSON9        CHAR(50),
        PERSON10        CHAR(50));''')


    conn.execute('''DROP TABLE IF EXISTS RECMDLIST_4;''')
    conn.execute('''CREATE TABLE RECMDLIST_4
        (ID INT PRIMARY KEY     NOT NULL,
        TARGET_PERSON     CHAR(50),
        PERSON1        CHAR(50),
        PERSON2        CHAR(50),
        PERSON3        CHAR(50),
        PERSON4        CHAR(50),
        PERSON5        CHAR(50),
        PERSON6        CHAR(50),
        PERSON7        CHAR(50),
        PERSON8        CHAR(50),
        PERSON9        CHAR(50),
        PERSON10        CHAR(50));''')


    conn.execute('''DROP TABLE IF EXISTS RECMDLIST_5;''')
    conn.execute('''CREATE TABLE RECMDLIST_5
        (ID INT PRIMARY KEY     NOT NULL,
        TARGET_PERSON     CHAR(50),
        PERSON1        CHAR(50),
        PERSON2        CHAR(50),
        PERSON3        CHAR(50),
        PERSON4        CHAR(50),
        PERSON5        CHAR(50),
        PERSON6        CHAR(50),
        PERSON7        CHAR(50),
        PERSON8        CHAR(50),
        PERSON9        CHAR(50),
        PERSON10        CHAR(50));''')

    # conn.execute('''DROP TABLE IF EXISTS List;''')
    # conn.execute('''CREATE TABLE List
    #     (Name              CHAR(50),
    #     Email              CHAR(50),
    #     CheckIn            INT,
    #     PublicTag         INT,
    #     EventID            INT);''')
    # print "Table created successfully"

    conn.close()

    result1 = iter_docs("../RecommendationResult/TFSessionModel131")
    result2 = iter_docs("../RecommendationResult/TFKeywordModel131")
    result3 = iter_docs("../RecommendationResult/TFSerMailModel131")
    result4 = iter_docs("../RecommendationResult/TFModel131")
    result5 = iter_docs("../RecommendationResult/IDFModel131")

    conn = sqlite3.connect('recomd.db')
    print "Opened database successfully"

    # list = open("all_profile_list.txt")
    # names = list.readlines()
    # for i in names:
    #     if i.endswith('\n'):
    #         i = i[:-1]
    #     conn.execute("INSERT INTO List VALUES (?, ?, ?, ?, ?)", (i, i + '@gmail.com', 0, 1, 1))
    # print "Initialized List table successfully"

    # profiles = open("init_profile.txt")
    # names = profiles.readlines()
    # for i in names:
    #     if i.endswith('\n'):
    #         i = i[:-1]
    #     conn.execute("INSERT INTO profile VALUES (?, ?, ?, ?, ?)", (i, i + '@gmail.com', 1, 1, 1))
    # print "Initialized List table successfully"


    n = 1
    for i in range(len(result1)):
        conn.execute("INSERT INTO RECMDLIST_1 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
             (n, result1[i][0], result1[i][1], result1[i][2], result1[i][3], result1[i][4], result1[i][5], result1[i][6], result1[i][7],  result1[i][8], result1[i][9], result1[i][10]))
        n = n+1

    n = 1
    for i in range(len(result2)):
        conn.execute("INSERT INTO RECMDLIST_2 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
             (n, result2[i][0], result2[i][1], result2[i][2], result2[i][3], result2[i][4], result2[i][5], result2[i][6], result2[i][7],  result2[i][8], result2[i][9], result2[i][10]))
        n = n+1

    n = 1
    for i in range(len(result3)):
        conn.execute("INSERT INTO RECMDLIST_3 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
             (n, result3[i][0], result3[i][1], result3[i][2], result3[i][3], result3[i][4], result3[i][5], result3[i][6], result3[i][7],  result3[i][8], result3[i][9], result3[i][10]))
        n = n+1

    n = 1
    for i in range(len(result4)):
        conn.execute("INSERT INTO RECMDLIST_4 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
             (n, result4[i][0], result4[i][1], result4[i][2], result4[i][3], result4[i][4], result4[i][5], result4[i][6], result4[i][7],  result4[i][8], result4[i][9], result4[i][10]))
        n = n+1

    n = 1
    for i in range(len(result5)):
        conn.execute("INSERT INTO RECMDLIST_5 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
             (n, result5[i][0], result5[i][1], result5[i][2], result5[i][3], result5[i][4], result5[i][5], result5[i][6], result5[i][7],  result5[i][8], result5[i][9], result5[i][10]))
        n = n+1

    conn.commit()
    print "Records created successfully"
    conn.close()

# get_db()
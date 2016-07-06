from flask_sqlalchemy import SQLAlchemy
import sqlite3
import os
import DBlog

def recommendations_filter_by_event(name, List, event_id):
    status = List.query.filter_by(Name=name).first()
    if status == None:
        return ''
    if status.CheckIn == 1 and status.PublicTag == 1 and status.EventID == event_id:
        return name + ', ' + status.Email + '|'
    return ''


def recommendations_filter_by_session(name, List, event_id, session_id):
    status = List.query.filter_by(Name=name).first()
    if status == None:
        return ''
    if status.CheckIn == 1 and status.PublicTag == 1 and status.EventID == event_id and status.SessionID == session_id:
        return name + ', ' + status.Email + '|'
    return ''


def add_new_person2List(profile, db, List):
    try:
        new_user = List(profile['firstname'] + ' ' + profile['lastname'], profile['email'], profile['check_in'], profile['public_tag'],
                        profile['event_id'])
        db.session.add(new_user)
        DBlog.logging('log/List.log', 'add', profile)
        db.session.commit()
        return 'new person added\n'
    except:
        db.session.rollback()
        return 'some error happened, rollback\n'


def update_person_in_List(user, profile, db):
    try:
        DBlog.logging('log/List.log', 'update', profile, user)
        user.Name = profile['firstname'] + ' ' + profile['lastname']
        user.CheckIn = profile['check_in']
        user.PublicTag = profile['public_tag']
        user.EventID = profile['event_id']
        user.SessionID = profile['session_id']
        db.session.commit()
        return 'information updated\n'
    except:
        db.session.rollback()
        return 'some error happened, rollback\n'


def iter_docs(topdir):
    result = []
    name = []
    for fn in os.listdir(topdir):
        if (fn.find('.txt') != -1):
            fin = open(os.path.join(topdir, fn), 'rb')
            text = fin.read()
            array = text.split('\n')
            name.append(fn[:-4].replace('_', ' '))
            result.append(array)
            fin.close()
    for list in result:
        if len(list) > 1:
            for i in range(10):
                list[i] = list[i][: list[i].find(':')].replace('_', ' ')
    return name, result


def init_recommendation_tables():
    conn = sqlite3.connect('recomd.db')

    conn.execute('''DROP TABLE IF EXISTS RECMDLIST;''')
    conn.execute('''CREATE TABLE RECMDLIST
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
        PERSON10       CHAR(50));''')

    # conn.execute('''DROP TABLE IF EXISTS RECMDLIST_1;''')

    # conn.execute('''DROP TABLE IF EXISTS RECMDLIST_2;''')
    # conn.execute('''CREATE TABLE RECMDLIST_2
    #     (ID INT PRIMARY KEY     NOT NULL,
    #     TARGET_PERSON     CHAR(50),
    #     PERSON1        CHAR(50),
    #     PERSON2        CHAR(50),
    #     PERSON3        CHAR(50),
    #     PERSON4        CHAR(50),
    #     PERSON5        CHAR(50),
    #     PERSON6        CHAR(50),
    #     PERSON7        CHAR(50),
    #     PERSON8        CHAR(50),
    #     PERSON9        CHAR(50),
    #     PERSON10       CHAR(50),
    #     Rate1          INT,
    #     Rate2          INT,
    #     Rate3          INT,
    #     Rate4          INT,
    #     Rate5          INT,
    #     Rate6          INT,
    #     Rate7          INT,
    #     Rate8          INT,
    #     Rate9          INT,
    #     Rate10         INT);''')
    #
    # conn.execute('''DROP TABLE IF EXISTS RECMDLIST_3;''')
    # conn.execute('''CREATE TABLE RECMDLIST_3
    #     (ID INT PRIMARY KEY     NOT NULL,
    #     TARGET_PERSON     CHAR(50),
    #     PERSON1        CHAR(50),
    #     PERSON2        CHAR(50),
    #     PERSON3        CHAR(50),
    #     PERSON4        CHAR(50),
    #     PERSON5        CHAR(50),
    #     PERSON6        CHAR(50),
    #     PERSON7        CHAR(50),
    #     PERSON8        CHAR(50),
    #     PERSON9        CHAR(50),
    #     PERSON10       CHAR(50),
    #     Rate1          INT,
    #     Rate2          INT,
    #     Rate3          INT,
    #     Rate4          INT,
    #     Rate5          INT,
    #     Rate6          INT,
    #     Rate7          INT,
    #     Rate8          INT,
    #     Rate9          INT,
    #     Rate10         INT);''')
    #
    # conn.execute('''DROP TABLE IF EXISTS RECMDLIST_4;''')
    # conn.execute('''CREATE TABLE RECMDLIST_4
    #     (ID INT PRIMARY KEY     NOT NULL,
    #     TARGET_PERSON     CHAR(50),
    #     PERSON1        CHAR(50),
    #     PERSON2        CHAR(50),
    #     PERSON3        CHAR(50),
    #     PERSON4        CHAR(50),
    #     PERSON5        CHAR(50),
    #     PERSON6        CHAR(50),
    #     PERSON7        CHAR(50),
    #     PERSON8        CHAR(50),
    #     PERSON9        CHAR(50),
    #     PERSON10       CHAR(50),
    #     Rate1          INT,
    #     Rate2          INT,
    #     Rate3          INT,
    #     Rate4          INT,
    #     Rate5          INT,
    #     Rate6          INT,
    #     Rate7          INT,
    #     Rate8          INT,
    #     Rate9          INT,
    #     Rate10         INT);''')
    #
    # conn.execute('''DROP TABLE IF EXISTS RECMDLIST_5;''')
    # conn.execute('''CREATE TABLE RECMDLIST_5
    #     (ID INT PRIMARY KEY     NOT NULL,
    #     TARGET_PERSON     CHAR(50),
    #     PERSON1        CHAR(50),
    #     PERSON2        CHAR(50),
    #     PERSON3        CHAR(50),
    #     PERSON4        CHAR(50),
    #     PERSON5        CHAR(50),
    #     PERSON6        CHAR(50),
    #     PERSON7        CHAR(50),
    #     PERSON8        CHAR(50),
    #     PERSON9        CHAR(50),
    #     PERSON10       CHAR(50),
    #     Rate1          INT,
    #     Rate2          INT,
    #     Rate3          INT,
    #     Rate4          INT,
    #     Rate5          INT,
    #     Rate6          INT,
    #     Rate7          INT,
    #     Rate8          INT,
    #     Rate9          INT,
    #     Rate10         INT);''')

    conn.close()
    print 'Recommendation tables initialized'


def init_List():
    conn = sqlite3.connect('recomd.db')

    conn.execute('''DROP TABLE IF EXISTS List;''')
    conn.execute('''CREATE TABLE List
        (Name              CHAR(50),
        Email              CHAR(50),
        CheckIn            INT,
        PublicTag         INT,
        EventID            INT,
        SessionID         INT);''')

    conn.close()
    print 'List table initialized'


def init_event():
    conn = sqlite3.connect('recomd.db')

    conn.execute('''DROP TABLE IF EXISTS event;''')
    conn.execute('''CREATE TABLE event
            (ID               INT PRIMARY KEY,
            Name              CHAR(50));''')

    conn.close()
    print 'event table initialized'


def init_session():
    conn = sqlite3.connect('recomd.db')

    conn.execute('''DROP TABLE IF EXISTS session;''')
    conn.execute('''CREATE TABLE session
            (EventID                INT,
            SessionID               INT,
            Name              CHAR(50),
            PRIMARY KEY (EventID, SessionID));''')

    conn.close()
    print 'session table initialized'


def add_event(ID, name, Event, db):
    event = Event.query.filter_by(ID=ID).first()
    if event == None:
        try:
            event = Event(ID, name)
            db.session.add(event)
            db.session.commit()
            print 'new event added'
        except:
            db.session.rollback()
            print 'some error happened, rollback'
    else:
        print 'event already exists'
    return


def add_session(eventID, sessionID, name, Session, db):
    session = Session.query.filter_by(EventID=eventID, SessionID=sessionID).first()
    if session == None:
        try:
            session = Session(eventID, sessionID, name)
            db.session.add(session)
            db.session.commit()
            print 'new session added'
        except:
            db.session.rollback()
            print 'some error happened, rollback'
    else:
        print 'session already exists'
    return


def add_rate(name, num, rate, RECMDLIST_4, db):
    user = RECMDLIST_4.query.filter_by(TARGET_PERSON=name).first()
    if user == None:
        print 'wrong name'
        return
    if num == 1:
        try:
            user.Rate1 = rate
            db.session.commit()
            print 'successfully added rate'
        except:
            db.rollback()
            print 'some error happened, rollback'
    if num == 2:
        try:
            user.Rate2 = rate
            db.session.commit()
            print 'successfully added rate'
        except:
            db.rollback()
            print 'some error happened, rollback'
    if num == 3:
        try:
            user.Rate3 = rate
            db.session.commit()
            print 'successfully added rate'
        except:
            db.rollback()
            print 'some error happened, rollback'
    if num == 4:
        try:
            user.Rate4 = rate
            db.session.commit()
            print 'successfully added rate'
        except:
            db.rollback()
            print 'some error happened, rollback'
    if num == 5:
        try:
            user.Rate5 = rate
            db.session.commit()
            print 'successfully added rate'
        except:
            db.rollback()
            print 'some error happened, rollback'
    if num == 6:
        try:
            user.Rate6 = rate
            db.session.commit()
            print 'successfully added rate'
        except:
            db.rollback()
            print 'some error happened, rollback'
    if num == 7:
        try:
            user.Rate7 = rate
            db.session.commit()
            print 'successfully added rate'
        except:
            db.rollback()
            print 'some error happened, rollback'
    if num == 8:
        try:
            user.Rate8 = rate
            db.session.commit()
            print 'successfully added rate'
        except:
            db.rollback()
            print 'some error happened, rollback'
    if num == 9:
        try:
            user.Rate9 = rate
            db.session.commit()
            print 'successfully added rate'
        except:
            db.rollback()
            print 'some error happened, rollback'
    if num == 10:
        try:
            user.Rate10 = rate
            db.session.commit()
            print 'successfully added rate'
        except:
            db.rollback()
            print 'some error happened, rollback'
    return


def insert_into_recommendation_tables():
    name1, result1 = iter_docs('../New_Data/Results/Recommendations')
    # name2, result2 = iter_docs("../RecommendationResult/TFKeywordModel131")
    # name3, result3 = iter_docs("../RecommendationResult/TFSerMailModel131")
    # name4, result4 = iter_docs("../RecommendationResult/TFModel131")
    # name5, result5 = iter_docs("../RecommendationResult/IDFModel131")

    conn = sqlite3.connect('recomd.db')

    for i in range(len(result1)):
        if len(result1[i]) > 1:
            conn.execute("INSERT INTO RECMDLIST VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                     (i, name1[i], result1[i][0], result1[i][1], result1[i][2], result1[i][3], result1[i][4], result1[i][5],
                      result1[i][6], result1[i][7], result1[i][8], result1[i][9]))

    # for i in range(len(result2)):
    #     conn.execute("INSERT INTO RECMDLIST_2 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
    #                  (n, name2[i], result2[i][0], result2[i][1], result2[i][2], result2[i][3], result2[i][4], result2[i][5],
    #                   result2[i][6], result2[i][7], result2[i][8], result2[i][9]))
    #     n = n + 1
    #
    # n = 1
    # for i in range(len(result3)):
    #     conn.execute("INSERT INTO RECMDLIST_3 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
    #                  (n, name3[i], result3[i][0], result3[i][1], result3[i][2], result3[i][3], result3[i][4], result3[i][5],
    #                   result3[i][6], result3[i][7], result3[i][8], result3[i][9]))
    #     n = n + 1
    #
    # n = 1
    # for i in range(len(result4)):
    #     conn.execute("INSERT INTO RECMDLIST_4 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
    #                  (n, name4[i], result4[i][0], result4[i][1], result4[i][2], result4[i][3], result4[i][4], result4[i][5],
    #                   result4[i][6], result4[i][7], result4[i][8], result4[i][9]))
    #     n = n + 1
    #
    # n = 1
    # for i in range(len(result5)):
    #     conn.execute("INSERT INTO RECMDLIST_5 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
    #                  (n, name5[i], result5[i][0], result5[i][1], result5[i][2], result5[i][3], result5[i][4], result5[i][5],
    #                   result5[i][6], result5[i][7], result5[i][8], result5[i][9]))
    #     n = n + 1

    conn.commit()
    conn.close()
    print 'Successfully inserted records into recommendation tables'


def insert_into_List():
    conn = sqlite3.connect('recomd.db')

    list = open("all_profile_list.txt")
    names = list.readlines()
    for i in names:
        if i.endswith('\n'):
            i = i[:-1]
        conn.execute("INSERT INTO List VALUES (?, ?, ?, ?, ?, ?)", (i, i + '@gmail.com', 0, 1, 1, -1))

    conn.close()
    print "Successfully inserted records into recommendation tables"


def get_recommendation_tables():
    init_recommendation_tables()
    insert_into_recommendation_tables()


def get_List():
    init_List()
    insert_into_List()
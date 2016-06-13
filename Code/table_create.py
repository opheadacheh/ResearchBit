from flask.ext.sqlalchemy import SQLAlchemy
from flask import Flask

application = Flask(__name__)

application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recomd.db'
db = SQLAlchemy(application)


class RECMDLIST_1(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    TARGET_PERSON = db.Column(db.Unicode)
    PERSON1 = db.Column(db.Unicode)
    PERSON2 = db.Column(db.Unicode)
    PERSON3 = db.Column(db.Unicode)
    PERSON4 = db.Column(db.Unicode)
    PERSON5 = db.Column(db.Unicode)
    PERSON6 = db.Column(db.Unicode)
    PERSON7 = db.Column(db.Unicode)
    PERSON8 = db.Column(db.Unicode)
    PERSON9 = db.Column(db.Unicode)
    PERSON10 = db.Column(db.Unicode)

    def __init__(self, id, name, p1, p2, p3, p4, p5, p6 , p7 , p8, p9, p10):
        self.ID = id
        self.TARGET_PERSON = name
        self.PERSON1 = p1
        self.PERSON2 = p2
        self.PERSON3 = p3
        self.PERSON4 = p4
        self.PERSON5 = p5
        self.PERSON6 = p6
        self.PERSON7 = p7
        self.PERSON8 = p8
        self.PERSON9 = p9
        self.PERSON10 = p10


class RECMDLIST_2(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    TARGET_PERSON = db.Column(db.Unicode)
    PERSON1 = db.Column(db.Unicode)
    PERSON2 = db.Column(db.Unicode)
    PERSON3 = db.Column(db.Unicode)
    PERSON4 = db.Column(db.Unicode)
    PERSON5 = db.Column(db.Unicode)
    PERSON6 = db.Column(db.Unicode)
    PERSON7 = db.Column(db.Unicode)
    PERSON8 = db.Column(db.Unicode)
    PERSON9 = db.Column(db.Unicode)
    PERSON10 = db.Column(db.Unicode)

    def __init__(self, id, name, p1, p2, p3, p4, p5, p6 , p7 , p8, p9, p10):
        self.ID = id
        self.TARGET_PERSON = name
        self.PERSON1 = p1
        self.PERSON2 = p2
        self.PERSON3 = p3
        self.PERSON4 = p4
        self.PERSON5 = p5
        self.PERSON6 = p6
        self.PERSON7 = p7
        self.PERSON8 = p8
        self.PERSON9 = p9
        self.PERSON10 = p10


class RECMDLIST_3(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    TARGET_PERSON = db.Column(db.Unicode)
    PERSON1 = db.Column(db.Unicode)
    PERSON2 = db.Column(db.Unicode)
    PERSON3 = db.Column(db.Unicode)
    PERSON4 = db.Column(db.Unicode)
    PERSON5 = db.Column(db.Unicode)
    PERSON6 = db.Column(db.Unicode)
    PERSON7 = db.Column(db.Unicode)
    PERSON8 = db.Column(db.Unicode)
    PERSON9 = db.Column(db.Unicode)
    PERSON10 = db.Column(db.Unicode)

    def __init__(self, id, name, p1, p2, p3, p4, p5, p6 , p7 , p8, p9, p10):
        self.ID = id
        self.TARGET_PERSON = name
        self.PERSON1 = p1
        self.PERSON2 = p2
        self.PERSON3 = p3
        self.PERSON4 = p4
        self.PERSON5 = p5
        self.PERSON6 = p6
        self.PERSON7 = p7
        self.PERSON8 = p8
        self.PERSON9 = p9
        self.PERSON10 = p10


class RECMDLIST_4(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    TARGET_PERSON = db.Column(db.Unicode)
    PERSON1 = db.Column(db.Unicode)
    PERSON2 = db.Column(db.Unicode)
    PERSON3 = db.Column(db.Unicode)
    PERSON4 = db.Column(db.Unicode)
    PERSON5 = db.Column(db.Unicode)
    PERSON6 = db.Column(db.Unicode)
    PERSON7 = db.Column(db.Unicode)
    PERSON8 = db.Column(db.Unicode)
    PERSON9 = db.Column(db.Unicode)
    PERSON10 = db.Column(db.Unicode)

    def __init__(self, id, name, p1, p2, p3, p4, p5, p6 , p7 , p8, p9, p10):
        self.ID = id
        self.TARGET_PERSON = name
        self.PERSON1 = p1
        self.PERSON2 = p2
        self.PERSON3 = p3
        self.PERSON4 = p4
        self.PERSON5 = p5
        self.PERSON6 = p6
        self.PERSON7 = p7
        self.PERSON8 = p8
        self.PERSON9 = p9
        self.PERSON10 = p10


class RECMDLIST_5(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    TARGET_PERSON = db.Column(db.Unicode)
    PERSON1 = db.Column(db.Unicode)
    PERSON2 = db.Column(db.Unicode)
    PERSON3 = db.Column(db.Unicode)
    PERSON4 = db.Column(db.Unicode)
    PERSON5 = db.Column(db.Unicode)
    PERSON6 = db.Column(db.Unicode)
    PERSON7 = db.Column(db.Unicode)
    PERSON8 = db.Column(db.Unicode)
    PERSON9 = db.Column(db.Unicode)
    PERSON10 = db.Column(db.Unicode)

    def __init__(self, id, name, p1, p2, p3, p4, p5, p6 , p7 , p8, p9, p10):
        self.ID = id
        self.TARGET_PERSON = name
        self.PERSON1 = p1
        self.PERSON2 = p2
        self.PERSON3 = p3
        self.PERSON4 = p4
        self.PERSON5 = p5
        self.PERSON6 = p6
        self.PERSON7 = p7
        self.PERSON8 = p8
        self.PERSON9 = p9
        self.PERSON10 = p10

class CheckList(db.Model):
    LastName = db.Column(db.Unicode)
    FirstName = db.Column(db.Unicode)
    EmailAdd = db.Column(db.Unicode)
    CheckIn = db.Column(db.Unicode)
    PrivacyTag = db.Column(db.Unicode)
    FileName = db.Column(db.Unicode)


db.create_all()
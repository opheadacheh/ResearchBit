from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os
import DBoperations, DBlog

application = Flask(__name__)

application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recomd.db'
db = SQLAlchemy(application)


class RECMDLIST(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    TARGET_PERSON = db.Column(db.String(80))
    PERSON1 = db.Column(db.String(80))
    PERSON2 = db.Column(db.String(80))
    PERSON3 = db.Column(db.String(80))
    PERSON4 = db.Column(db.String(80))
    PERSON5 = db.Column(db.String(80))
    PERSON6 = db.Column(db.String(80))
    PERSON7 = db.Column(db.String(80))
    PERSON8 = db.Column(db.String(80))
    PERSON9 = db.Column(db.String(80))
    PERSON10 = db.Column(db.String(80))

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


# create a list of researchers and their situations
class List(db.Model):
    Name = db.Column(db.String(80))
    Email = db.Column(db.String(80), primary_key=True)
    CheckIn = db.Column(db.Integer)
    PublicTag = db.Column(db.Integer)
    EventID = db.Column(db.Integer)
    SessionID = db.Column(db.Integer)

    def __init__(self, name, email, check_in, public, event_id, session_id = -1):
        self.Name = name
        self.Email = email
        self.CheckIn = check_in
        self.PublicTag = public
        self.EventID = event_id
        self.SessionID = session_id


# create a table for all researchers to help locate their profiles.
class Profile(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(80))
    Email = db.Column(db.String(80))
    Filename = db.Column(db.String(80))

    def __init__(self, name, email):
        self.Name = name
        self.Email = email
        self.Filename = name + 'Compressed'


# create a table for event, with ID and name
class Event(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100))

    def __init__(self, ID, name):
        self.ID = ID
        self.Name = name


# create a table for session, with ID and name
class Session(db.Model):
    __tablename__ = 'session'
    EventID = db.Column(db.Integer, primary_key=True)
    SessionID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100))

    def __init__(self, eventID, sessionID, name):
        self.EventID = eventID
        self.SessionID = sessionID
        self.Name = name

db.create_all()

# handle http get request, return recommendation list
@application.route('/r/get/', methods=['GET'])
def recomd_get():
    args = request.args
    name = args['firstname'].title() + ' ' + args['lastname'].title()
    event_id = int(args['event_id'])
    status = List.query.filter_by(Name=name, Email=args['email']).first()
    if status == None:
        return 'Person not found\n'
    elif status.CheckIn != 1:
        return 'Person didn\'t check in\n'
    elif status.EventID != event_id:
        return 'Person checked in but event ID doesn\'t match\n'
    elif not 'session_id' in args.keys():
        user = RECMDLIST.query.filter_by(TARGET_PERSON=name).first()
        if user == None:
            return 'Sorry, we cannot find any recommendations for you'
        recomd_list = ''
        recomd_list += DBoperations.recommendations_filter_by_event(user.PERSON1, List, event_id)
        recomd_list += DBoperations.recommendations_filter_by_event(user.PERSON2, List, event_id)
        recomd_list += DBoperations.recommendations_filter_by_event(user.PERSON3, List, event_id)
        recomd_list += DBoperations.recommendations_filter_by_event(user.PERSON4, List, event_id)
        recomd_list += DBoperations.recommendations_filter_by_event(user.PERSON5, List, event_id)
        recomd_list += DBoperations.recommendations_filter_by_event(user.PERSON6, List, event_id)
        recomd_list += DBoperations.recommendations_filter_by_event(user.PERSON7, List, event_id)
        recomd_list += DBoperations.recommendations_filter_by_event(user.PERSON8, List, event_id)
        recomd_list += DBoperations.recommendations_filter_by_event(user.PERSON9, List, event_id)
        recomd_list += DBoperations.recommendations_filter_by_event(user.PERSON10, List, event_id)
    elif 'session_id' in args.keys():
        session_id = int(args['session_id'])
        user = RECMDLIST.query.filter_by(TARGET_PERSON=args['firstname'] + ', ' + args['lastname']).first()
        if user == None:
            return 'Sorry, we cannot find any recommendations for you'
        recomd_list = ''
        recomd_list += DBoperations.recommendations_filter_by_session(user.PERSON1, List, event_id, session_id)
        recomd_list += DBoperations.recommendations_filter_by_session(user.PERSON2, List, event_id, session_id)
        recomd_list += DBoperations.recommendations_filter_by_session(user.PERSON3, List, event_id, session_id)
        recomd_list += DBoperations.recommendations_filter_by_session(user.PERSON4, List, event_id, session_id)
        recomd_list += DBoperations.recommendations_filter_by_session(user.PERSON5, List, event_id, session_id)
        recomd_list += DBoperations.recommendations_filter_by_session(user.PERSON6, List, event_id, session_id)
        recomd_list += DBoperations.recommendations_filter_by_session(user.PERSON7, List, event_id, session_id)
        recomd_list += DBoperations.recommendations_filter_by_session(user.PERSON8, List, event_id, session_id)
        recomd_list += DBoperations.recommendations_filter_by_session(user.PERSON9, List, event_id, session_id)
        recomd_list += DBoperations.recommendations_filter_by_session(user.PERSON10, List, event_id, session_id)
    else:
        recomd_list = 'wrong input'
    return recomd_list


# handle http get request, return profile in the format of XML file
@application.route('/p/get/', methods=['GET'])
def profile_get():
    args = request.args
    name = args['firstname'] + ' ' + args['lastname']
    name = str(name).title()

    dir = '../New_Data/Profiles/'
    text = ''
    for fn in os.listdir(dir):
        name_segment = fn[8: -4].replace('_', ' ').title()
        if name_segment == name:
            file = open(dir + fn, 'rt')
            text = file.read()
    if text == '':
        return 'person not found\n'
    else:
        return text


@application.route('/reset/')
def reset_List():
    DBoperations.init_List()
    DBoperations.init_event()
    DBoperations.init_session()
    DBlog.reset_logging('log/List.log')
    return 'Successfully reset\n'


@application.route('/init_recomd/')
def init_recomd():
    DBoperations.get_recommendation_tables()
    return 'Recommedation tables initialiized\n'


@application.route('/feedback/', methods=['POST'])
def give_feedback():
    args = request.form.copy()
    name = args['lastname'] + ', ' + args['firstname']

    return 'rate added\n'


# handle http post request, return a succeed/fail message
@application.route('/post/', methods=['POST'])
def add_profile():
    profile = request.get_json()
    # if the given parameter is not in the format of json, e.g. using curl
    if profile == None:
        profile = request.form.copy()
    profile['lastname'] = str(profile['lastname']).title()
    profile['firstname'] = str(profile['firstname']).title()
    profile['check_in'] = int(profile['check_in'])
    profile['public_tag'] = int(profile['public_tag'])
    profile['event_id'] = int(profile['event_id'])
    if 'event_name' in profile.keys():
        profile['event_name'] = str(profile['event_name'])
        DBoperations.add_event(profile['event_id'], profile['event_name'], Event, db)
    if 'session_id' in profile.keys():
        profile['session_id'] = int(profile['session_id'])
        profile['session_name'] = str(profile['session_name'])
        DBoperations.add_session(profile['event_id'], profile['session_id'], profile['session_name'], Session, db)
    else:
        profile['session_id'] = -1
    user = List.query.filter_by(Email=profile['email']).first()

    # add a new person to database
    if user == None:
        return DBoperations.add_new_person2List(profile, db, List)

    # update the person's information
    else:
        return DBoperations.update_person_in_List(user, profile, db)

# post an event, automatically generate its ID
# @application.route('/event_post/', methods=['POST'])
# def add_event():
#     data = request.get_json()
#
#     # if the given parameter is not in the format of json, e.g. using curl
#     if data == None:
#         data = request.form.copy()
#
#     # see if the event already exists
#     event = Event.query.filter_by(Name = data['event_name']).first()
#
#     # if not exists
#     if event == None:
#         event = Event(data['event_name'])
#         db.session.add(event)
#         db.session.commit()
#         return 'The ID of the new event is ' + str(event.ID) + '\n'
#
#     # if exists
#     else:
#         return 'The event already exists, its ID is ' + str(event.ID) + '\n'
#
# # get the name of an event by its ID
# @application.route('/event_get/', methods=['GET'])
# def get_eventID():
#     ID = request.args['event_id']
#
#     # find the event
#     event = Event.query.filter_by(ID = ID).first()
#
#     # if doesn't exist
#     if event == None:
#         return 'The event doesn\'t exist\n'
#
#     # if found
#     else:
#         return 'The name of event is \"' + event.Name + '\"\n'

# get method webpage
@application.route('/get_page/')
def get_page():
    return render_template('get.html')

# handle request from webpage
@application.route('/get_page/%lastname=<lastname>%firstname=<firstname>%method=<method>', methods=['GET'])
def get(lastname, firstname, method):
    if method == 'ss':
        record = RECMDLIST.query.filter_by(TARGET_PERSON=lastname + ', ' + firstname).first()
    elif method == 'kw':
        record = RECMDLIST.query.filter_by(TARGET_PERSON=lastname + ', ' + firstname).first()
    elif method == 'ml':
        record = RECMDLIST.query.filter_by(TARGET_PERSON=lastname + ', ' + firstname).first()
    elif method == 'tf':
        record = RECMDLIST.query.filter_by(TARGET_PERSON=lastname + ', ' + firstname).first()
    else:
        record = RECMDLIST.query.filter_by(TARGET_PERSON=lastname + ', ' + firstname).first()

    if record == None:
        return 'Person not found\n'
    else:
        return render_template('get_result.html', id=record.ID, p=record.TARGET_PERSON, p1=record.PERSON1,
                               p2=record.PERSON2, p3=record.PERSON3, p4=record.PERSON4, p5=record.PERSON5,
                               p6=record.PERSON6, p7=record.PERSON7, p8=record.PERSON8, p9=record.PERSON9,
                               p10=record.PERSON10)

# post method webpage
@application.route('/post_page/')
def post_page():
    return render_template('post.html')

# hand post request from webpage
@application.route('/post_page/%lastname=<lastname>%firstname=<firstname>%email=<email>%check_in=<check_in>%public_tag=<public_tag>%event_id=<event_id>')
def post(lastname, firstname, email, check_in, public_tag, event_id):
    name = firstname.lower() + lastname.lower()
    user = List.query.filter_by(Email=email).first()

    # add a new person to database
    if user == None:
        new_user = List(name, email, check_in, public_tag, event_id)
        db.session.add(new_user)
        db.session.commit()
        return 'new person added\n'

    # update the person's information
    else:
        user.CheckIn = check_in
        user.PublicTag = public_tag
        user.EventID = event_id
        db.session.commit()
        return 'infomation updated\n'


# the main page
@application.route('/')
def index():
    return render_template('main.html')


if __name__ == "__main__":
    DBlog.init_logging()
    application.run(host='0.0.0.0')

# curl --data "name=denisehills&email=denisehills@gmail.com&check_in=1&public_tag=1&event_id=1" http://54.175.39.137:5000/post/
# curl --data "lastname=Hills&firstname=Denise&recommendation_num=2&rate=5" http://54.175.39.137:5000/feedback/
# curl "http://54.175.39.137:5000/r/get/?email=denisehills@gmail.com&event_id=1&lastname=Hills&firstname=Denise"
# curl "http://54.175.39.137:5000/p/get/?lastname=Hills&firstname=Denise&email=denisehills@gmail.com"

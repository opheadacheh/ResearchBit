from writeSql import get_db
from flask import Flask, render_template, request, jsonify, Response
from flask.ext.sqlalchemy import SQLAlchemy
from file import delete, copy
from requests import post, get
from run import run
from copy import deepcopy as list_copy
import os
import json

application = Flask(__name__)

application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recomd.db'
db = SQLAlchemy(application)


# create a table for recommendation based on session method
class RECMDLIST_1(db.Model):
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


# create a table for recommendation based on keyword method
class RECMDLIST_2(db.Model):
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


# create a table for recommendation based on mailing list method
class RECMDLIST_3(db.Model):
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


# create a table for recommendation based on term frequency method
class RECMDLIST_4(db.Model):
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


# create a table for recommendation based on TF-IDF method
class RECMDLIST_5(db.Model):
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

    def __init__(self, name, email, check_in, public, event_id):
        self.Name = name
        self.Email = email
        self.CheckIn = check_in
        self.PublicTag = public
        self.EventID = event_id


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

    def __init__(self, name):
        self.Name = name

db.create_all()

# get method webpage
@application.route('/get_page/')
def get_page():
    return render_template('get.html')

# handle request from webpage
@application.route('/get_page/%lastname=<lastname>%firstname=<firstname>%method=<method>', methods = ['GET'])
def get(lastname, firstname, method):
    if method == 'ss':
        record = RECMDLIST_1.query.filter_by(TARGET_PERSON = lastname + ', ' + firstname).first()
    elif method == 'kw':
        record = RECMDLIST_2.query.filter_by(TARGET_PERSON = lastname + ', ' + firstname).first()
    elif method == 'ml':
        record = RECMDLIST_3.query.filter_by(TARGET_PERSON = lastname + ', ' + firstname).first()
    elif method == 'tf':
        record = RECMDLIST_4.query.filter_by(TARGET_PERSON = lastname + ', ' + firstname).first()
    else:
        record = RECMDLIST_5.query.filter_by(TARGET_PERSON = lastname + ', ' + firstname).first()

    if record == None:
        return 'Person not found\n'
    else:
        return render_template('get_result.html', id = record.ID, p = record.TARGET_PERSON, p1 = record.PERSON1,
                               p2 = record.PERSON2, p3 = record.PERSON3, p4 = record.PERSON4, p5 = record.PERSON5,
                               p6 = record.PERSON6, p7 = record.PERSON7, p8 = record.PERSON8, p9 = record.PERSON9,
                               p10 = record.PERSON10)

# handle http get request, return recommendation list
@application.route('/r/get/', methods=['GET'])
def recomd_get():
    args = request.args
    name = args['firstname'].lower()+args['lastname'].lower()
    status = List.query.filter_by(Name=name, Email=args['email']).first()
    #print args['email']
    #print status
    #print status.CheckIn
    if status == None:
        return 'Person not found\n'
    elif status.CheckIn != 1:
        return 'Person didn\'t check in\n'
    elif status.EventID != int(args['event_id']):
        return 'Person checked in but event ID doesn\'t match\n'
    else:
        user = RECMDLIST_4.query.filter_by(TARGET_PERSON=args['lastname'] + ', ' + args['firstname']).first()
        recomd_list = ''

        name = user.PERSON1.replace(' ', '')
        status = List.query.filter_by(Name=name).first()
        if status.PublicTag == 1:
            recomd_list += user.PERSON1.title() + ', ' + status.Email + '|'

        name = user.PERSON2.replace(' ', '')
        status = List.query.filter_by(Name=name).first()
        if status.PublicTag == 1:
            recomd_list += user.PERSON2.title() + ', ' + status.Email + '|'

        name = user.PERSON3.replace(' ', '')
        status = List.query.filter_by(Name=name).first()
        if status.PublicTag == 1:
            recomd_list += user.PERSON3.title() + ', ' + status.Email + '|'

        name = user.PERSON4.replace(' ', '')
        status = List.query.filter_by(Name=name).first()
        if status.PublicTag == 1:
            recomd_list += user.PERSON4.title() + ', ' + status.Email + '|'

        name = user.PERSON5.replace(' ', '')
        status = List.query.filter_by(Name=name).first()
        if status.PublicTag == 1:
            recomd_list += user.PERSON5.title() + ', ' + status.Email + '|'

        name = user.PERSON6.replace(' ', '')
        status = List.query.filter_by(Name=name).first()
        if status.PublicTag == 1:
            recomd_list += user.PERSON6.title() + ', ' + status.Email + '|'

        name = user.PERSON7.replace(' ', '')
        status = List.query.filter_by(Name=name).first()
        if status.PublicTag == 1:
            recomd_list += user.PERSON7.title() + ', ' + status.Email + '|'

        name = user.PERSON8.replace(' ', '')
        status = List.query.filter_by(Name=name).first()
        if status.PublicTag == 1:
            recomd_list += user.PERSON8.title() + ', ' + status.Email + '|'

        name = user.PERSON9.replace(' ', '')
        status = List.query.filter_by(Name=name).first()
        if status.PublicTag == 1:
            recomd_list += user.PERSON9.title() + ', ' + status.Email + '|'

        name = user.PERSON10.replace(' ', '')
        status = List.query.filter_by(Name=name).first()
        if status.PublicTag == 1:
            recomd_list += user.PERSON10.title() + ', ' + status.Email + '|'

    return recomd_list


# handle http get request, return profile in the format of XML file
@application.route('/p/get/', methods=['GET'])
def profile_get():
    args = request.args
    name = args['firstname'].lower() + args['lastname'].lower()

    dir = '../Data/Data/All_Profile_Data/'
    text = ''
    for fn in os.listdir(dir):
        name_segment = fn[fn.find('_') + 1 : fn.rfind('.')]
        if name_segment.find('.') != -1:
            name_segment = name_segment[name_segment.find('.')+1: ]
        if name_segment == name + 'Compressed':
            file = open(dir + fn, 'rt')
            text = file.read()
    if text == '':
        return 'person not found\n'
    else:
        return text


# handle http post request, return a succeed/fail message
@application.route('/post/', methods=['POST'])
def add_profile():
    profile = request.get_json()
    # if the given parameter is not in the format of json, e.g. using curl
    if profile == None:
        profile = request.form.copy()
    profile['name']=profile['name'].lower()
    user = List.query.filter_by(Email=profile['email']).first()

    # add a new person to database
    if user == None:
        new_user = List(profile['name'], profile['email'], profile['check_in'], profile['public_tag'], profile['event_id'])
        db.session.add(new_user)
        db.session.commit()
        return 'new person added\n'

    # update the person's information
    else:
        user.Name = str(profile['name'])
        user.CheckIn = int(profile['check_in'])
        user.PublicTag = int(profile['public_tag'])
        user.EventID = int(profile['event_id'])
        db.session.commit()
        return 'infomation updated\n'

# post an event, automatically generate its ID
@application.route('/event_post/', methods=['POST'])
def add_event():
    data = request.get_json()

    # if the given parameter is not in the format of json, e.g. using curl
    if data == None:
        data = request.form.copy()

    # see if the event already exists
    event = Event.query.filter_by(Name = data['event_name']).first()

    # if not exists
    if event == None:
        event = Event(data['event_name'])
        db.session.add(event)
        db.session.commit()
        return 'The ID of the new event is ' + str(event.ID) + '\n'

    # if exists
    else:
        return 'The event already exists, its ID is ' + str(event.ID) + '\n'

# get the name of an event by its ID
@application.route('/event_get/', methods=['GET'])
def get_eventID():
    ID = request.args['event_id']

    # find the event
    event = Event.query.filter_by(ID = ID).first()

    # if doesn't exist
    if event == None:
        return 'The event doesn\'t exist\n'

    # if found
    else:
        return 'The name of event is \"' + event.Name + '\"\n'

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

# run the recommendation generation algorithm
# @application.route('/run/')
# def run_alg():
#     # delete all existing files
#     delete()
#
#     # visit the List table, copy the profiles of all qualified people to target folder
#     ppl = List.query.all()
#     for i in ppl:
#         if i.PublicTag == 1 and i.CheckIn == 1:
#             copy(i.Name)
#
#     # run algorithm, right now only run TF method because it is fast
#     run(1, 0.25, 10, 'tf')
#
#     # rewrite our database
#     get_db()
#
#     # succeed information
#     return 'Successful\n'

# the main page
@application.route('/')
def index():
    return render_template('main.html')


if __name__ == "__main__":
    # get_db()
    application.run(host='0.0.0.0', debug=True)

# sample request commands:
# requests.post('http://0.0.0.0:5000/post/', json={'name':'denisehills', 'email':'denisehills@gmail.com', 'check_in':1, 'public_tag':1, 'event_id':1})
# requests.get('http://0.0.0.0:5000/r/get/', params={'firstname':'Denise', 'lastname':'Hills', 'event_id':1, 'email':'denisehills@gmail.com'})
# requests.get('http://0.0.0.0:5000/p/get/', params={'firstname':'Denise', 'lastname':'Hills', 'email':'denisehills@gmail.com'})

# curl --data "name=denisehills&email=denisehills@gmail.com&check_in=1&public_tag=1&event_id=1" http://54.165.138.137:5000/post/
# curl "http://54.165.138.137:5000/r/get/?email=denisehills@gmail.com&event_id=1&lastname=Hills&firstname=Denise" -o r.json
# curl "http://54.165.138.137:5000/p/get/?lastname=Hills&firstname=Denise&email=denisehills@gmail.com" -o profile.xml

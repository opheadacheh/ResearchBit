import os
import datetime


def init_logging():
    try:
        os.rename('log/List.log', 'log/List' + str(datetime.datetime.now()) + '.log')
        open('log/List.log', 'w').close()
    except:
        open('log/List.log', 'w').close()
    print('Logging initiated')
    return


def logging(filename, op, new_user, user = None):
    file = open(filename, 'a')
    file.write(op + '|')
    if op == 'update' and user != None:
        file.write(user.Name + ',' + user.Email + ',' + str(user.CheckIn) + ',' + str(user.PublicTag) + ',' + str(user.EventID) + ',' +
                   str(user.SessionID) +'|')
        file.write(new_user['firstname'] + ' ' + new_user['lastname'] + ',' + new_user['email'] + ',' + str(new_user['check_in']) + ',' +
                   str(new_user['public_tag']) + ',' + str(new_user['event_id']) + ',' + str(new_user['session_id']) + '\n')
    elif op == 'add':
        file.write(new_user['firstname'] + ' ' + new_user['lastname'] + ',' + new_user['email'] + ',' + str(new_user['check_in']) + ',' +
                   str(new_user['public_tag']) + ',' + str(new_user['event_id']) + ',' + str(new_user['session_id']) + '\n')
    return


def reset_logging(filename):
    file = open(filename, 'a')
    file.write('reset\n')
    return
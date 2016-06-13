import Keywords
import MailingListRecommendation
import Session
import sys

def run(k1, k2, listsize, reco_type):
    if reco_type == 'tf':
        Session.run(k1, k2, listsize, False, False, 'tf')
    if reco_type == 'idf':
        Session.run(k1, k2, listsize, True, False, 'idf')
    if reco_type == 'keywords':
    	Keywords.run(k1, k2, listsize, 'keywords')
    if reco_type == 'session':
    	Session.run(k1, k2, listsize, False, True, 'session')
    if reco_type == 'mailinglist':
    	MailingListRecommendation.run(k1, k2, listsize, 'mailinglist')
    if reco_type == 'all':
    	Keywords.run(k1, k2, listsize, 'keywords')
    	Session.run(k1, k2, listsize, False, True, 'session')
        Session.run(k1, k2, listsize, False, False, 'tf')
        Session.run(k1, k2, listsize, True, False, 'idf')
    	MailingListRecommendation.run(k1, k2, listsize, 'mailinglist')
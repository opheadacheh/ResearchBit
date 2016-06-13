import Keywords
import MailingListRecommendation
import Session
import sys

if __name__ == "__main__":

    k1 = int(sys.argv[1])
    k2 = float(sys.argv[2])
    listsize = int(sys.argv[3])
    reco_type = str(sys.argv[4])
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


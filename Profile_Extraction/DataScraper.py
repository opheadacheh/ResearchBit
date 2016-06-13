# -*- coding: utf-8 -*-
__author__ = 'LoganYoung'

# Import statements.
import os
import urllib.request
from bs4 import BeautifulSoup
import time
import random
import string
import calendar
from difflib import SequenceMatcher

def similar(stringA, stringB):
    return SequenceMatcher(None, stringA, stringB).ratio()

# Sets the beginning start time in order to calculate the runtimes of each process and the total runtime.
progStartTime = time.time()
processStartTime = time.time()

# Initializes each needed dictionary.
authorsGrantsXMLList = {}
authorsGrantsLocalXMLList = {}
authorsGrantsOnlineXMLList = {}
authorsGSLinks = {}
authorsMailingList = {}
authorsEmail = {}
authorsOrganization = {}
authorsNameList = {}
authorsSessions = {}
authorsDataFound = {}
authorsPubDuplicates = {}
authorsPubsFound = {}
authorsProfiles = {}
authorsCompressedProfiles = {}
authorsConferences = {}
authorsPostersXML = {}
authorsKeywords = {}

sessionAuthors = {}
sessionXML = {}

idsAuthors = {}
authorsIDs = {}
idsSessions = {}
sessionsIDs = {}
sessionIdNum = -1
idsPublications = {}
publicationsIDs = {}
pubIdNum = -1
idsKeywords = {}
keywordsIDs = {}
keywordIdNum = -1

keywordsPubs = {}
keywordsAuthors = {}

pubsKeywords = {}
pubsAuthors = {}

authorsPubsAGUXMLList = {}
authorsPubsMADXMLList = {}
authorsPubsSDXMLList = {}
authorsPubsGSXMLList = {}
authorsPubsPubMedXMLList = {}
authorsPubsTitlesList = {}
authorsPubsTextsList = {}

authorsDuplicatesEmails = {}

authorsGrantsCompressedXMLList = {}
authorsGrantsCompressedLocalXMLList = {}
authorsGrantsCompressedOnlineXMLList = {}
authorsPubsCompressedMADXMLList = {}
authorsPubsCompressedSDXMLList = {}
authorsPubsCompressedGSXMLList = {}
authorsPubsCompressedPubMedXMLList = {}
authorsPubsCompressedAGUXMLList = {}

# Opens 'gslinks.txt' and 'authors.txt'.
# authorsFile = open("Data_In/authors.txt", "r")
gsLinksFile = open("Data_In/gslinks.txt", "r")

# Sets up the dictionary associating the authors(keys) to the Google Scholars profile url.
for line in gsLinksFile:
    splitLine = line.split("|")
    if splitLine[1].endswith("\n"):
        authorsGSLinks[splitLine[0]] = splitLine[1][:-1]
    else:
        authorsGSLinks[splitLine[0]] = splitLine[1]
gsLinksFile.close()

# Initializes each list associated with each authors/keys.
"""for author in authorsFile:
    if author.endswith("\n"):
        authorsGrantsXMLList[author.lower()[:-1]] = []
        authorsGrantsCompressedXMLList[author.lower()[:-1]] = []
        authorsGrantsLocalXMLList[author.lower()[:-1]] = []
        authorsGrantsCompressedLocalXMLList[author.lower()[:-1]] = []
        authorsGrantsOnlineXMLList[author.lower()[:-1]] = []
        authorsGrantsCompressedOnlineXMLList[author.lower()[:-1]] = []
        authorsPubsAGUXMLList[author.lower()[:-1]] = []
        authorsPubsGSXMLList[author.lower()[:-1]] = []
        authorsPubsMADXMLList[author.lower()[:-1]] = []
        authorsPubsSDXMLList[author.lower()[:-1]] = []
        authorsPubsPubMedXMLList[author.lower()[:-1]] = []
        authorsPubsCompressedAGUXMLList[author.lower()[:-1]] = []
        authorsPubsCompressedGSXMLList[author.lower()[:-1]] = []
        authorsPubsCompressedMADXMLList[author.lower()[:-1]] = []
        authorsPubsCompressedSDXMLList[author.lower()[:-1]] = []
        authorsPubsCompressedPubMedXMLList[author.lower()[:-1]] = []
        authorsMailingList[author.lower()[:-1]] = []
    else:
        authorsGrantsXMLList[author.lower()] = []
        authorsGrantsCompressedXMLList[author.lower()] = []
        authorsGrantsLocalXMLList[author.lower()] = []
        authorsGrantsCompressedLocalXMLList[author.lower()] = []
        authorsGrantsOnlineXMLList[author.lower()] = []
        authorsGrantsCompressedOnlineXMLList[author.lower()] = []
        authorsPubsAGUXMLList[author.lower()] = []
        authorsPubsGSXMLList[author.lower()] = []
        authorsPubsMADXMLList[author.lower()] = []
        authorsPubsSDXMLList[author.lower()] = []
        authorsPubsPubMedXMLList[author.lower()] = []
        authorsPubsCompressedAGUXMLList[author.lower()] = []
        authorsPubsCompressedGSXMLList[author.lower()] = []
        authorsPubsCompressedMADXMLList[author.lower()] = []
        authorsPubsCompressedSDXMLList[author.lower()] = []
        authorsPubsCompressedPubMedXMLList[author.lower()] = []
        authorsMailingList[author.lower()] = []
authorsFile.close()"""

# Initializes each list associated with each atuhors/keys.
# --Working as of 7/23/2015--
def initAuthors():
    attendeeNum = 0
    for csvFile in os.listdir("Data_In/ESIP_Attendees"):
        reader = open("Data_In/ESIP_Attendees/" + csvFile, "r", encoding="utf8")
        reader.readline()
        for line in reader:
            attendeeNum += 1
            splitLine = line.split(",")
            name = (splitLine[2] + " " + splitLine[3]).lower().replace("  ", " ")
            if name not in authorsOrganization.keys():
                authorsOrganization[name] = splitLine[5]
                authorsEmail[name] = splitLine[12].replace("\n", "")
                authorsNameList[name] = [name]
                authorsGrantsXMLList[name] = []
                authorsGrantsCompressedXMLList[name] = []
                authorsGrantsLocalXMLList[name] = []
                authorsGrantsCompressedLocalXMLList[name] = []
                authorsGrantsOnlineXMLList[name] = []
                authorsGrantsCompressedOnlineXMLList[name] = []
                authorsPubsAGUXMLList[name] = []
                authorsPubsCompressedAGUXMLList[name] = []
                authorsPubsGSXMLList[name] = []
                authorsPubsCompressedGSXMLList[name] = []
                authorsPubsMADXMLList[name] = []
                authorsPubsCompressedMADXMLList[name] = []
                authorsPubsSDXMLList[name] = []
                authorsPubsCompressedSDXMLList[name] = []
                authorsPubsPubMedXMLList[name] = []
                authorsPubsCompressedPubMedXMLList[name] = []
                authorsMailingList[name] = []
                authorsSessions[name] = []
                authorsPubsTitlesList[name] = []
                authorsPubsTextsList[name] = []
                authorsConferences[name] = []
                authorsPostersXML[name] = []
                authorsKeywords[name] = []
                authorsDataFound[name] = {}
                authorsDataFound[name]["AGU"] = False
                authorsDataFound[name]["MAD"] = False
                authorsDataFound[name]["SD"] = False
                authorsDataFound[name]["PubMed"] = False
                authorsDataFound[name]["NSF"] = False
                authorsDataFound[name]["MailingList"] = False
                authorsDataFound[name]["ESIP_Session"] = False
                authorsDataFound[name]["Poster"] = False
                authorsDataFound[name]["Conference"] = False
                authorsDataFound[name]["Asilomar"] = False
                authorsPubsFound[name] = {}
                authorsPubsFound[name]["AGU"] = 0
                authorsPubsFound[name]["MAD"] = 0
                authorsPubsFound[name]["SD"] = 0
                authorsPubsFound[name]["PubMed"] = 0
                authorsPubDuplicates[name] = {}
                authorsPubDuplicates[name]["AGU"] = 0
                authorsPubDuplicates[name]["MAD"] = 0
                authorsPubDuplicates[name]["SD"] = 0
                authorsPubDuplicates[name]["PubMed"] = 0
                authorsProfiles[name] = ""
                authorsCompressedProfiles[name] = ""
            authorsConferences[name].append(csvFile[-11:-4])
            authorsDataFound[name]["Conference"] = True
    scrapeAlternateNames(authorsEmail.keys())
    scrapeAsilomarAttendees()
    print(str(len(authorsGrantsXMLList.keys())))

def scrapeAsilomarAttendees():
    authorReader = open("Data_In/authors.txt", "r", encoding="utf8")
    for line in authorReader:
        author = line[:-1].lower()
        if author in authorsOrganization.keys():
            authorsDataFound[author]["Asilomar"] = True

# Reads the files in the IDs_Keys folder to associate each ID to authors and sessions.
def initIds():
    global pubIdNum
    global sessionIdNum
    global keywordIdNum
    authKeysReader = open("Data_In/IDs_Keys/authKeys.txt", "r", encoding="utf8")
    for line in authKeysReader:
        splitLine = line.replace("\n", "").split("|")
        idsAuthors[splitLine[0]] = splitLine[1]
        authorsIDs[splitLine[1]] = splitLine[0]
    authKeysReader.close()
    sessionKeysReader = open("Data_In/IDs_Keys/sessionKeys.txt", "r", encoding="utf8")
    for line in sessionKeysReader:
        splitLine = line.replace("\n", "").split("|")
        idsSessions[splitLine[0]] = splitLine[1]
        sessionsIDs[splitLine[1]] = splitLine[0]
        sessionIdNum = int(splitLine[0][3:])
    sessionKeysReader.close()
    sessionIdNum += 1
    pubKeysReader = open("Data_In/IDs_Keys/pubKeys.txt", "r", encoding="utf8")
    for line in pubKeysReader:
        splitLine = line.replace("\n", "").split("|")
        idsPublications[splitLine[0]] = splitLine[1]
        publicationsIDs[splitLine[1]] = splitLine[0]
        pubIdNum = int(splitLine[0][3:])
        pubsAuthors[splitLine[1]] = []
    pubKeysReader.close()
    pubIdNum += 1
    keywordKeysReader = open("Data_In/IDs_Keys/keywordKeys.txt", "r", encoding="utf8")
    for line in keywordKeysReader:
        splitLine = line.replace("\n", "").split("|")
        idsKeywords[splitLine[0]] = splitLine[1]
        keywordsIDs[splitLine[1]] = splitLine[0]
        keywordIdNum = int(splitLine[0][3:])
        keywordsAuthors[splitLine[1]] = []
        keywordsPubs[splitLine[1]] = []
    keywordKeysReader.close()
    keywordIdNum += 1

# Assigns an ID to every author and every session.
def assignIDs():
    authIdWriter = open("Data_In/IDs_Keys/authKeys.txt", "w", encoding="utf8")
    sessionIdWriter = open("Data_In/IDs_Keys/sessionKeys.txt", "w", encoding="utf8")
    authIdNum = 0
    sessionIdNum = 0
    for author in authorsOrganization.keys():
        id = "ATT"
        for num in range(0, 5-len(str(authIdNum))):
            id += "0"
        id += str(authIdNum)
        authIdWriter.write(id + "|" + author + "\n")
        authIdNum += 1
    authIdWriter.close()
    for fileName in os.listdir("Data_In/ESIP_Sessions_Asilomar"):
        id = "SES"
        for num in range(0, 5-len(str(sessionIdNum))):
            id += "0"
        id += str(sessionIdNum)
        sessionIdWriter.write(id + "|" + fileName[:-4] + "\n")
        sessionIdNum += 1

# Scrapes the AGU ESIP matches for alternative names for authors.
# --Working as of 7/21/2015--
def scrapeAlternateNames(authors):
    for file in os.listdir("Data_In/ESIP_AGU_Matches/"):
        reader = open("Data_In/ESIP_AGU_Matches/" + file)
        reader.readline()
        reader.readline()
        esipName = reader.readline().strip(" \t\n\r").lower().replace("\'", "").replace("-", "").replace(" ", "")[10:-11]
        aguName = reader.readline().strip(" \t\n\r").lower().replace("\'", "").replace("-", " ").replace("  ", " ")[9:-10]
        emailAddress = reader.readline().strip(" \t\n\r").lower().replace("\'", "").replace("-", "").replace(" ", "")[14:-15]
        for author in authors:
            if author.replace("\'", "").replace(" ", "") == esipName and authorsEmail[author] == emailAddress:
                authorsNameList[author].append(aguName)
                #print(authorsNameList[author])
                #print(file)

# Scrapes the ESIP session attendance data from the ESIP_Sessions folder.
def scrapeESIPAsilomarSessionData():
    for file in os.listdir("Data_In/ESIP_Sessions_Asilomar/"):
        sessionFileReader = open("Data_In/ESIP_Sessions_Asilomar/" + file, "r", encoding="utf8")
        authorsList = []
        for line in sessionFileReader:
            splitLine = line.split(",")
            name = splitLine[0].lower()
            if name not in authorsList and name in authorsSessions.keys():
                authorsList.append(name)
                authorsSessions[name].append(file[:-4])
                authorsDataFound[name]["ESIP_Session"] = True
        sessionAuthors[file[:-4]] = authorsList
        sessionXML[file[:-4]] = "\t<Session>\n\t\t<Name>" + file[:-4] + "</Name>\n\t</Session>\n"

# A quick and easy function for scraping the ESIP_Session data then writing it to the output folder.
# Not used for the larger database construction.
def writeESIPSessionData():
    authSessions = {}
    authEmails = {}
    for file in os.listdir("Data_In/ESIP_Sessions_Asilomar/"):
        sessionFileReader = open("Data_In/ESIP_Sessions_Asilomar/" + file, "r", encoding="utf8")
        authorsList = []
        for line in sessionFileReader:
            splitLine = line.split(",")
            name = splitLine[0].lower()
            if name not in authorsList and not name == "":
                authorsList.append(name)
                if name not in authSessions.keys():
                    authSessions[name] = []
                    authEmails[name] = splitLine[1]
                authSessions[name].append(file[:-4])
        sessionAuthors[file[:-4]] = authorsList
    authSessionsCSVWriter = open("OutputOld/Sessions/Session_Data.csv", "w", encoding="utf8")
    authSessionsCSVWriter.write("Author,Email,Session,Date")
    for author in authSessions.keys():
        if len(authSessions[author]) > 0:
            for sessionDate in authSessions[author]:
                splitSession = sessionDate.split("_")
                date = splitSession[0]
                session = splitSession[1]
                day = int(date[-2:])
                print(date[-2:])
                print(day)
                if day >= 14 and day <= 17:
                    authSessionsCSVWriter.write("\n\"" + author + "\",\"" + authEmails[author] + "\",\"" + session + "\",\"" + date + "\"")
    authSessionsCSVWriter.close()

    """for author in authSessions.keys():
        if len(authSessions[author]) > 0:
            authSessionsWriter = open("Output/AuthSessions/" + author.replace(" ", "") + ".xml", "w", encoding="utf8")
            authSessionsWriter.write("<Attendee>")
            for session in authSessions[author]:
                authSessionsWriter.write("\n\t<Session>" + session + "</Session>")
            authSessionsWriter.write("\n</Attendee>")
            authSessionsWriter.close()
    for session in sessionAuthors.keys():
        if len(sessionAuthors[session]) > 0:
            sessionAuthsWriter = open("Output/Sessions/" + session + ".xml", "w", encoding="utf8")
            sessionAuthsWriter.write("<Session>")
            for author in sessionAuthors[session]:
                sessionAuthsWriter.write("\n\t<Attendee>" + author + "</Attendee>")
            sessionAuthsWriter.write("\n</Session>")
            sessionAuthsWriter.close()"""

def scrapeESIPSessionData():
    sessionIdWriter = open("Data_In/IDs_Keys/sessionKeys.txt", "a", encoding="utf8")
    global sessionIdNum
    for file in os.listdir("Data_In/ESIP_Sessions"):
        reader = open("Data_In/ESIP_Sessions/" + file, "r", encoding="utf8")
        reader.readline()
        readerContent = reader.read()
        splitContent = readerContent.split("\"\n\"")
        for line in splitContent:
            authorsList = []
            splitLine = line.split("\",\"")
            title = splitLine[1]
            teaser = splitLine[5]
            abstract = splitLine[6]
            rawDate = splitLine[3]
            splitRawDate = rawDate.split(",")
            date = splitRawDate[2].strip(" ")[:4]
            splitMonthDay = splitRawDate[1].split(" ")
            monthName = splitMonthDay[1]
            day = splitMonthDay[2]
            if len(day) == 0:
                day = "0" + day
            month = ""
            for num in range(1, len(calendar.month_name)):
                if calendar.month_name[num].lower() == monthName.lower():
                    if num < 10:
                        month = "0" + str(num)
                    else:
                        month = str(num)
            date += "-" + month + "-" + day
            session = date + "_" + title
            sessionLeaders = splitLine[13]
            participants = splitLine[14]
            splitSessionLeaders = sessionLeaders.split(",")
            splitParticipants = participants.split(",")
            for sessionLeader in splitSessionLeaders:
                authName = sessionLeader.strip(" ").lower()
                if authName not in authorsList and authName in authorsSessions.keys():
                    authorsList.append(authName)
                    authorsSessions[authName].append(session)
                    authorsDataFound[authName]["ESIP_Session"] = True
            for participant in splitParticipants:
                authName = participant.strip(" ").lower()
                if authName not in authorsList and authName in authorsSessions.keys():
                    authorsList.append(authName)
                    authorsSessions[authName].append(session)
                    authorsDataFound[authName]["ESIP_Session"] = True
            sessionAuthors[session] = authorsList
            sessionXML[session] = "\t<Session>\n\t\t<Name>" + session + "</Name>\n"
            sessionXML[session] += "\t\t<Teaser>" + teaser + "</Teaser>\n"
            sessionXML[session] += "\t\t<Abstract>" + abstract + "</Abstract>\n\t</Session>\n"
            if session not in sessionsIDs.keys():
                id = "SES"
                for num in range(0, 5-len(str(sessionIdNum))):
                    id += "0"
                id += str(sessionIdNum)
                idsSessions[id] = session
                sessionsIDs[session] = id
                sessionIdWriter.write(id + "|" + session + "\n")
                sessionIdNum += 1
                if not os.path.isfile("Data_Out/IDs_Data/Publications/" + id + ".txt"):
                    sessionWriter = open("Data_Out/IDs_Data/Publications/" + id + ".txt", "w", encoding="utf8")
                    sessionWriter.write(sessionXML[session])
                    sessionWriter.close()

# Scrapes the grant data from the local NSF folder.
# Disambiguation: Email
# --Working as of 7/22/2015--
def scrapeLocalGrantData(authors):
    for folder in os.listdir("Data_In/NSF"):
        print("Scraping local grant data from " + folder + " . . .")
        processStartTime = time.time()
        for file in os.listdir("Data_In/NSF/" + folder):
            if file.endswith(".xml"):
                name = ""
                namesFound = []
                namesVerified = []
                awardId = ""
                awardTitle = ""
                abstractNarration = ""
                nameFound = ""
                reader = open("Data_In/NSF/" + folder + "/" + file, "r", encoding="utf8")
                for line in reader:
                    lineStartsWith = lambda x: line.strip(" \t\n\r").startswith(x)
                    if lineStartsWith("<SignBlockName>"):
                        for author in authors.keys():
                            test = line.strip(" \t\n\r")[15:-16].lower()
                            if author.lower().replace(" ", "").replace("-", "") == line.strip(" \t\n\r")[15:-16].lower().replace(" ", "").replace("-", ""):
                                namesVerified.append(author)
                    if lineStartsWith("<FirstName>"):
                        name = line.strip(" \t\n\r")[11:-12]
                    if lineStartsWith("<LastName>"):
                        name += " " + line.strip(" \t\n\r")[10:-11]
                        for author in authors.keys():
                            if author.lower().replace(" ", "").replace("-", "") == name.lower().replace(" ", "").replace("-", ""):
                                nameFound = author
                    if lineStartsWith("<EmailAddress>"):
                        if not nameFound == "":
                            if authorsEmail[nameFound] == line.strip(" \t\n\r")[14:-15]:
                                namesVerified.append(nameFound)
                            nameFound = ""
                    if lineStartsWith("<AwardID>"):
                        awardId = line.strip(" \t\n\r")[9:-10]
                    if lineStartsWith("<AwardTitle>"):
                        awardTitle = line.strip(" \t\n\r")[12:-13]
                    if lineStartsWith("<AbstractNarration>"):
                        abstractNarration = line.strip(" \t\n\r")[19:-20]
                reader.close()
                if(len(namesVerified) > 0):
                    rereader = open("Data_In/NSF/" + folder + "/" + file, "r", encoding="utf8")
                    rereader.readline()
                    awardXML = rereader.read()
                    for author in namesVerified:
                        authorsGrantsLocalXMLList[author].append(awardXML)
                        awardCompressedXML = "\t<Award>\n\t\t<AwardTitle>" + awardTitle + "\t\t</AwardTitle>\n\t\t<AwardID>" + awardId + "</AwardID>\n\t</Award>\n"
                        authorsGrantsCompressedLocalXMLList[author].append(awardCompressedXML)
                        authorsDataFound[author]["NSF"] = True
        print("Finished scraping grant data from " + folder + " in " + str(time.time()-processStartTime) + " seconds.")
    return authors

# Scrapes grant data from the online NSF API.
# Disambiguation: Email
# --Working as of 7/22/15--
def scrapeOnlineGrantData(authors):
    onlineGrantsNum = 0
    print("Scraping online grant data . . .")
    processStartTime = time.time()
    for author in authors.keys():
        #print(author.encode("utf8"))
        authorUrl = "http://api.nsf.gov/services/v1/awards.xml?pdPIName=\"" + author.replace(" ", "+") + "\"&printFields=agency,awardeeCity,awardeeName,awardeeStateCode,date,fundsObligatedAmt,id,pdPIName,poName,title,piEmail"
        #print(authorUrl.encode("utf8"))
        try:
            authorAwards = urllib.request.urlopen(authorUrl)
            awardXML = ""
            awardId = ""
            awardTitle = ""
            piEmails = []
            authorAwardsXML = authorAwards.read().decode("utf8")
            authorAwardsList = authorAwardsXML.split("<")
            for term in authorAwardsList[3:-1]:
                termStartsWith = lambda x: term.strip(" \t\n\r").startswith(x)
                #if not termStartsWith("/") or termStartsWith("/award>"):
                #    awardXML += "\t"
                if not termStartsWith("award>") and not termStartsWith("/"):
                    awardXML += "\t"
                awardXML += "<" + term
                if termStartsWith("/") or termStartsWith("award>"):
                    awardXML += "\n"
                if termStartsWith("/award>"):
                    if authorsEmail[author].lower() in piEmails:
                        authorsGrantsOnlineXMLList[author].append(awardXML)
                        authorsGrantsCompressedOnlineXMLList[author].append("\t<Award>\n\t\t<AwardTitle>" + awardTitle + "</AwardTitle>\n\t\t<AwardID>" + awardId + "</AwardID>\n\t</Award>\n")
                        authorsDataFound[author]["NSF"] = True
                        onlineGrantsNum += 1
                    awardXML = ""
                    piEmails = []
                if termStartsWith("id>"):
                    awardId = term.strip(" \t\n\r")[3:]
                if termStartsWith("title>"):
                    awardTitle = term.strip(" \t\n\r")[6:]
                if termStartsWith("piEmail>"):
                    piEmails.append(term.strip(" \t\n\r")[8:].lower())
                    #print(term.strip(" \t\n\r")[8:])
        except:
            print("Error for " + author)
    print("Finished scraping online grant data in " + str(time.time()-processStartTime) + " seconds with " + str(onlineGrantsNum) + " grants.")
    return authorsGrantsOnlineXMLList

# Scrapes abstract data from the AGU_IN_Abstracts folder.
# Disambiguation: Email
# --Working as of 7/24/2015--
def scrapeAGUPublicationData(authors):
    global pubIdNum
    global keywordIdNum
    pubIdWriter = open("Data_In/IDs_Keys/pubKeys.txt", "a", encoding="utf8")
    keywordIdWriter = open("Data_In/IDs_Keys/keywordKeys.txt", "a", encoding="utf8")
    for folder in os.listdir("Data_In/AGU_IN_Abstracts"):
        if "." not in folder:
            print("Scraping AGU abstracts data from " + folder + ". . .")
            processStartTime = time.time()
            if folder == "2014":
                a = 1
            for file in os.listdir("Data_In/AGU_IN_Abstracts/" + folder):
                if file.endswith(".xml"):
                    namesFound = []
                    text = ""
                    keywords = []
                    reader = open("Data_In/AGU_IN_Abstracts/" + folder + "/" + file, "r", encoding="utf8")
                    foundAuthorName = ""
                    for line in reader:
                        if line.strip(" \t\n\r").startswith("<Name>"):
                            for author in authors.keys():
                                # Author last name first initial
                                if author == "karl benedict":
                                    c = 1
                                authorsNameListTest = authorsNameList[author]
                                if len(authorsNameList[author]) > 1:
                                    b = 1
                                for authorName in authorsNameList[author]:
                                    splitAuthor = authorName.split(" ")
                                    authorLNFI = splitAuthor[len(splitAuthor) - 1] + ","
                                    for i in range(len(splitAuthor)-1):
                                        authorLNFI += " " + splitAuthor[i][0]
                                    #if len(authorsNameList[author]) > 1:
                                        #b = 1
                                    if authorLNFI.replace(" ", "").replace("-", "") == line.strip(" \t\n\r").lower()[6:-7].replace(" ", "").replace("-", ""):
                                        foundAuthorName = author
                                        #namesFound.append(foundAuthorName)
                        if line.strip(" \t\n\r").startswith("<Email>"):
                            if not foundAuthorName=="":
                                foundEmail = line.strip(" \t\n\r")[7:-8].lower()
                                storedEmail = authorsEmail[foundAuthorName]
                                if authorsEmail[foundAuthorName]==foundEmail:
                                    namesFound.append(foundAuthorName)
                                else:
                                    if foundAuthorName not in authorsDuplicatesEmails.keys():
                                        authorsDuplicatesEmails[foundAuthorName] = []
                                    if foundEmail not in authorsDuplicatesEmails[foundAuthorName]:
                                        authorsDuplicatesEmails[foundAuthorName].append(foundEmail)
                        if line.strip(" \t\n\r").startswith("<Keyword>"):
                            keywords.append(line.strip(" \t\n\r").lower()[9:-10])
                        if line.strip(" \t\n\r").startswith("<Text>"):
                            text = line.strip(" \t\n\r").lower()[6:-7]
                    reader.close()
                    for author in namesFound:
                        authorsPubsFound[author]["AGU"] += 1
                        rereader = open("Data_In/AGU_IN_Abstracts/" + folder + "/" + file, "r", encoding="utf8")
                        rereader.readline()
                        fullAbstractXML = rereader.read()
                        rereader.close()
                        authorsPubsAGUXMLList[author].append(fullAbstractXML)
                        compressedXML = "\t<Publication>\n\t\t<Text>" + text + "</Text>\n\t\t<Keywords>\n"
                        fileTitle = file[:-4]
                        for keyword in keywords:
                            compressedXML += "\t\t\t<Keyword>" + keyword + "</Keyword>\n"
                            keyword = keyword.lower()
                            if keyword not in authorsKeywords[author]:
                                authorsKeywords[author].append(keyword)
                            if keyword not in idsKeywords.values():
                                id = "KEY"
                                for num in range(0, 5-len(str(keywordIdNum))):
                                    id += "0"
                                id += str(keywordIdNum)
                                idsKeywords[id] = keyword
                                keywordsIDs[keyword] = id
                                keywordsAuthors[keyword] = []
                                keywordsPubs[keyword] = []
                                keywordIdWriter.write(id + "|" + keyword + "\n")
                                keywordIdNum += 1
                            keywordsAuthors[keyword].append(author)
                            if fileTitle not in pubsKeywords.keys():
                                pubsKeywords[fileTitle] = []
                            pubsKeywords[fileTitle].append(keyword)
                            keywordsPubs[keyword].append(fileTitle)
                        compressedXML += "\t\t</Keywords>\n\t</Publication>\n"
                        authorsPubsCompressedAGUXMLList[author].append(compressedXML)
                        authorsPubsTextsList[author].append(text)
                        authorsDataFound[author]["AGU"] = True
                        if fileTitle not in idsPublications.values():
                            id = "PUB"
                            for num in range(0, 5-len(str(pubIdNum))):
                                id += "0"
                            id += str(pubIdNum)
                            idsPublications[id] = fileTitle
                            publicationsIDs[fileTitle] = id
                            pubsAuthors[fileTitle] = []
                            pubIdWriter.write(id + "|" + fileTitle + "\n")
                            pubIdNum += 1
                            if not os.path.isfile("Data_Out/IDs_Data/Publications/" + id + ".txt"):
                                pubWriter = open("Data_Out/IDs_Data/Publications/" + id + ".txt", "w", encoding="utf8")
                                pubWriter.write(fullAbstractXML)
                                pubWriter.close()
                        pubsAuthors[fileTitle].append(author)
            print("Finished scraping AGU abstracts data from " + folder + " in " + str(time.time()-processStartTime) + " seconds.")
    pubIdWriter.close()
    keywordIdWriter.close()
    return authors

# Scrapes publication data from the authors' Google Scholar profile page.
# --Not working as Google Scholar blocks automated queries--
def scrapeGSPublicationData(authors):
    print("Scraping GS publication data . . .")
    processStartTime = time.time()
    for author in authors.keys():
        pubsGSUrls = []
        print(authorsGSLinks[author])
        authUrlReader = urllib.request.urlopen(authorsGSLinks[author])
        authorHTML = authUrlReader.read()
        authSouper = BeautifulSoup(authorHTML)
        rawPubInfo = authSouper.find_all(class_="gsc_a_at")
        # Find all of the urls for the publications themselves.
        for term in rawPubInfo:
            term = str(term).replace("<", ">")
            splitTerm = term.split(">")
            splitATag = splitTerm[1].split("\"")
            pubsGSUrls.append("https://scholar.google.com" + splitATag[3].replace("&amp;", "&"))
            #authorsPubsGSXMLList[author].append(splitTerm[2])
        for url in pubsGSUrls:
            pubJournal = ""
            pubDescription = ""
            print(url)
            pubUrlReader = urllib.request.urlopen(url)
            pubHTML = pubUrlReader.read()
            pubSouper = BeautifulSoup(pubHTML)
            # Find title information.
            rawTitleInfo = str(pubSouper.find(class_="gsc_title_link"))
            rawTitleInfo = rawTitleInfo.replace("<", ">")
            print(rawTitleInfo)
            splitTitleInfo = rawTitleInfo.split(">")
            pubTitle = splitTitleInfo[2]
            rawPubDetails = pubSouper.find_all(class_="gsc_scl")
            for term in rawPubDetails:
                term = str(term).replace("<", ">")
                splitTerm = term.split(">")
                if splitTerm[4] == "Journal":
                    pubJournal = splitTerm[8]
                if splitTerm[4] == "Description":
                    pubDescription = splitTerm[8] + splitTerm[10] + splitTerm[12] + splitTerm[14] + splitTerm[16] + splitTerm[18]
            authorsPubsGSXMLList[author].append("\t<Publication>\n\t\t<Title>" + pubTitle + "</Title>\n\t\t<Description>" + pubDescription + "</Description>\n\t\t<Journal>" + pubJournal + "</Journal>\n\t</Publication>\n")
            authorsPubsCompressedGSXMLList[author].append("\t<Publication>\n\t\t<Title>" + pubTitle + "</Title>\n\t</Publication>\n")
    print("Finished scraping GS publication data in " + str(time.time()-processStartTime) + " seconds.")
    return authorsPubsGSXMLList

# Scrapes publication data from the Microsoft Academic Data
# --Working as of 7/15/2015--
def scrapeMADPublicationData(authors):
    pubIdWriter = open("Data_In/IDs_Keys/pubKeys.txt", "a", encoding="utf8")
    keywordIdWriter = open("Data_In/IDs_Keys/keywordKeys.txt", "a", encoding="utf8")
    errorCount = 0
    global pubIdNum
    global keywordIdNum
    for author in authors.keys():
        print(author)
        processStartTime = time.time()
        print("Scraping " + author + "\'s MAD publication data . . .")
        authIds = []
        paperIdsKeywordIds = {}
        paperIdsKeywords = {}
        authorSplit = author.split(" ")
        url = "https://api.datamarket.azure.com/MRC/MicrosoftAcademic/v2/Author?$select=ID&$filter=Name%20eq%20%27" + authorSplit[0] + "%20" + authorSplit[1].replace("\'", "").replace("-", "") + "%27"
        try:
            authUrlReader = urllib.request.urlopen(url)
            authUrlContent = str(authUrlReader.read())
            splitUrlContent = authUrlContent.replace("<", ">").split(">")
        except:
            errorCount += 1
            print("Error for " + url)
        authorId = ""
        for term in splitUrlContent:
            if term.isdigit() and authorId == "":
                # authIds.append(term)
                authorId = term
        if authorId != "":
            authIds.append(authorId)
        for authId in authIds:
            authPapersUrl = "https://api.datamarket.azure.com/MRC/MicrosoftAcademic/v2/Paper_Author?$select=PaperID&$filter=AuthorID%20eq%20" + authId
            try:
                authPapersUrlReader = urllib.request.urlopen(authPapersUrl)
                authPapersContent = str(authPapersUrlReader.read())
                splitAuthPapersContent = authPapersContent.replace("<", ">").split(">")
            except:
                errorCount += 1
                print("Error for " + authPapersUrl)
            for term in splitAuthPapersContent:
                if term.isdigit():
                    paperIdsKeywordIds[term] = []
                    paperIdsKeywords[term] = []
        for paperId in paperIdsKeywordIds.keys():
            paperKeywordIdUrl = "https://api.datamarket.azure.com/MRC/MicrosoftAcademic/v2/Paper_Keyword?$select=KeywordID&$filter=CPaperID%20eq%20" + paperId
            try:
                paperKeywordIdUrlReader = urllib.request.urlopen(paperKeywordIdUrl)
                paperKeywordIdContent = str(paperKeywordIdUrlReader.read())
                splitPaperKeywordIdContent = paperKeywordIdContent.replace("<", ">").split(">")
                for term in splitPaperKeywordIdContent:
                    if term.isdigit():
                        paperIdsKeywordIds[paperId].append(term)
            except:
                errorCount += 1
                print("Error for " + paperKeywordIdUrl)
            pubXML = "\t<Publication>\n\t\t<MADID>" + paperId + "</MADID>"
            paperTitleUrl = "https://api.datamarket.azure.com/MRC/MicrosoftAcademic/v2/Paper?$select=ID,Title&$filter=ID%20eq%20" + paperId
            title = ""
            try:
                paperTitleReader = urllib.request.urlopen(paperTitleUrl)
                paperTitleContent = str(paperTitleReader.read())
                splitPaperTitleContent = paperTitleContent.replace("<", ">").split(">")
                title = splitPaperTitleContent[len(splitPaperTitleContent)-11]
                pubXML += "\n\t\t<Title>" + title + "</Title>"
            except:
                errorCount += 1
                print("Error for " + paperTitleUrl)
            for keywordId in paperIdsKeywordIds[paperId]:
                keywordUrl = "https://api.datamarket.azure.com/MRC/MicrosoftAcademic/v2/Keyword?$select=DisplayName&$filter=ID%20eq%20" + keywordId
                try:
                    keywordUrlReader = urllib.request.urlopen(keywordUrl)
                    keywordContent = str(keywordUrlReader.read())
                    splitKeywordContent = keywordContent.replace("<", ">").split(">")
                    for num in range(0, len(splitKeywordContent)):
                        if splitKeywordContent[num] == "d:DisplayName":
                            paperIdsKeywords[paperId].append(splitKeywordContent[num+1])
                except:
                    errorCount += 1
                    print("Error for " + keywordUrl)
            for keyword in paperIdsKeywords[paperId]:
                pubXML += "\n\t\t<Keyword>" + keyword + "</Keyword>"
            pubXML += "\n\t</Publication>"
            duplicate = False
            for storedTitle in authorsPubsTitlesList[author]:
                if similar(storedTitle, title) >= .93:
                    duplicate = True
            if not duplicate:
                authorsPubsTitlesList[author].append(title)
                authorsPubsMADXMLList[author].append(pubXML)
                authorsPubsCompressedMADXMLList[author].append(pubXML)
                authorsDataFound[author]["MAD"] = True
                if title not in idsPublications.values():
                    id = "PUB"
                    for num in range(0, 5-len(str(pubIdNum))):
                        id += "0"
                    id += str(pubIdNum)
                    idsPublications[id] = title
                    publicationsIDs[title] = id
                    pubsAuthors[title] = []
                    pubIdWriter.write(id + "|" + title + "\n")
                    pubIdNum += 1
                    if not os.path.isfile("Data_Out/IDs_Data/Publications/" + id + ".txt"):
                        pubWriter = open("Data_Out/IDs_Data/Publications/" + id + ".txt", "w", encoding="utf8")
                        pubWriter.write(pubXML)
                        pubWriter.close()
                pubsAuthors[title].append(author)
                for keyword in paperIdsKeywords[paperId]:
                    keyword = keyword.lower()
                    if keyword not in authorsKeywords[author]:
                        authorsKeywords[author].append(keyword)
                    if keyword not in idsKeywords.values():
                        id = "KEY"
                        for num in range(0, 5-len(str(keywordIdNum))):
                            id += "0"
                        id += str(keywordIdNum)
                        idsKeywords[id] = keyword
                        keywordsIDs[keyword] = id
                        keywordsAuthors[keyword] = []
                        keywordsPubs[keyword] = []
                        keywordIdWriter.write(id + "|" + keyword + "\n")
                        keywordIdNum += 1
                    keywordsAuthors[keyword].append(author)
                    if title not in pubsKeywords.keys():
                        pubsKeywords[title] = []
                    pubsKeywords[title].append(keyword)
                    keywordsPubs[keyword].append(title)
        print("Finished scraping " + author + "\'s MAD publication data in " + str(time.time()-processStartTime) + " seconds.")
    print(str(errorCount) + " errors.")
    pubIdWriter.close()
    keywordIdWriter.close()
    return authorsPubsMADXMLList

# Scrapes the local MAD publication data from the previously scraped data in the Output/MADPublicationData folder.
def scrapeLocalMADPublicationData(authors):
    pubIdWriter = open("Data_In/IDs_Keys/pubKeys.txt", "a", encoding="utf8")
    keywordIdWriter = open("Data_In/IDs_Keys/keywordKeys.txt", "a", encoding="utf8")
    global pubIdNum
    global keywordIdNum
    for author in authors.keys():
        print(author)
        processStartTime = time.time()
        print("Scraping " + author + "\'s MAD publication data . . .")
        if os.path.exists("Data_In/StoredMADPublicationData/" + author.replace(" ", "") + ".txt"):
            authMADDataReader = open("Data_In/StoredMADPublicationData/" + author.replace(" ", "") + ".txt", "r", encoding="utf8")
            authXML = authMADDataReader.read()
            authMADDataReader.close()
            splitAuthXML = authXML.split("<Publication>")
            for num in range(1, len(splitAuthXML)):
                title = ""
                keywords = []
                pubXML = "<Publication>" + splitAuthXML[num]
                titleSplitPubXML = pubXML.split("<Title>")
                if len(titleSplitPubXML) > 1:
                    title = titleSplitPubXML[1].split("</Title>")[0]
                keywordSplitPubXML = pubXML.split("<Keyword>")
                if len(keywordSplitPubXML) > 1:
                    for num2 in range(1, len(keywordSplitPubXML)):
                        keywords.append(keywordSplitPubXML[num2].split("</Keyword>")[0])
                duplicate = False
                for storedTitle in authorsPubsTitlesList[author]:
                    if similar(storedTitle, title) >= .93:
                        duplicate = True
                authorsPubsFound[author]["MAD"] += 1
                if not duplicate:
                    authorsPubsTitlesList[author].append(title)
                    authorsPubsMADXMLList[author].append(pubXML)
                    authorsPubsCompressedMADXMLList[author].append(pubXML)
                    authorsDataFound[author]["MAD"] = True
                    if title not in idsPublications.values():
                        id = "PUB"
                        for num in range(0, 5-len(str(pubIdNum))):
                            id += "0"
                        id += str(pubIdNum)
                        idsPublications[id] = title
                        publicationsIDs[title] = id
                        pubsAuthors[title] = []
                        pubIdWriter.write(id + "|" + title + "\n")
                        pubIdNum += 1
                        if not os.path.isfile("Data_Out/IDs_Data/Publications/" + id + ".txt"):
                            pubWriter = open("Data_Out/IDs_Data/Publications/" + id + ".txt", "w", encoding="utf8")
                            pubWriter.write(pubXML)
                            pubWriter.close()
                    pubsAuthors[title].append(author)
                    for keyword in keywords:
                        keyword = keyword.lower()
                        if keyword not in authorsKeywords[author]:
                            authorsKeywords[author].append(keyword)
                        if keyword not in idsKeywords.values():
                            id = "KEY"
                            for num in range(0, 5-len(str(keywordIdNum))):
                                id += "0"
                            id += str(keywordIdNum)
                            idsKeywords[id] = keyword
                            keywordsIDs[keyword] = id
                            keywordsAuthors[keyword] = []
                            keywordsPubs[keyword] = []
                            keywordIdWriter.write(id + "|" + keyword + "\n")
                            keywordIdNum += 1
                        keywordsAuthors[keyword].append(author)
                        if title not in pubsKeywords.keys():
                            pubsKeywords[title] = []
                        pubsKeywords[title].append(keyword)
                        keywordsPubs[keyword].append(title)
                else:
                    authorsPubDuplicates[author]["MAD"] += 1
        print("Finished scraping " + author + "\'s MAD publication data in " + str(time.time()-processStartTime) + " seconds.")
    pubIdWriter.close()
    keywordIdWriter.close()
    return authorsPubsMADXMLList

# Scrapes publication data from the Science Direct API.
# --Working as of 7/15/2015--
def scrapeSDPublicationData(authors):
    pubIdWriter = open("Data_In/IDs_Keys/pubKeys.txt", "a", encoding="utf8")
    global pubIdNum
    print("Scraping SD publication data . . .")
    processStartTime = time.time()
    for author in authors.keys():
        print(author)
        splitAuthor = author.split(" ")
        try:
            authUrl = "https://api.elsevier.com/content/search/index:SCIDIR?query=specific-author(\"" + splitAuthor[1] + "%20" + splitAuthor[0] +"\")&apiKey=ee5e3b734ae2235f41b2219cf0cba8c0&httpAccept=application/xml"
            authUrlReader = urllib.request.urlopen(authUrl)
            authUrlContent = authUrlReader.read()
            splitAuthUrlContent = str(authUrlContent).split("<entry>")
            for i in range(1, len(splitAuthUrlContent)):
                title = ""
                teaser = ""
                if not splitAuthUrlContent[i].startswith("<error>"):
                    splitEntry = splitAuthUrlContent[i].replace(">", "<").split("<")
                    for j in range(0, len(splitEntry)):
                        if splitEntry[j].lower().endswith("title") and not splitEntry[j].startswith("/"):
                            title = splitEntry[j+1]
                        if splitEntry[j].lower().endswith("teaser") and not splitEntry[j].startswith("/"):
                            teaser = splitEntry[j+1]
                    compressedPubXML = "\t<entry>"
                    if not title=="":
                        compressedPubXML += "\n\t\t<Title>" + title + "</Title>"
                    if not teaser=="":
                        compressedPubXML += "\n\t\t<Teaser>" + teaser + "</Teaser>"
                    compressedPubXML += "\n\t</entry>"
                    duplicate = False
                    for storedTitle in authorsPubsTitlesList[author]:
                        if similar(title, storedTitle) >= .93:
                            duplicate = True
                    authorsPubsFound[author]["SD"] += 1
                    if not duplicate:
                        authorsPubsTitlesList[author].append(title)
                        authorsPubsSDXMLList[author].append("\t<entry>\n\t\t" + splitAuthUrlContent[i].replace("><", ">\n\t\t<").replace("\t</entry>", "</entry>"))
                        authorsPubsCompressedSDXMLList[author].append(compressedPubXML)
                        authorsDataFound[author]["SD"] = True
                        if title not in idsPublications.values():
                            id = "PUB"
                            for num in range(0, 5-len(str(pubIdNum))):
                                id += "0"
                            id += str(pubIdNum)
                            idsPublications[id] = title
                            publicationsIDs[title] = id
                            pubsAuthors[title] = []
                            pubIdWriter.write(id + "|" + title + "\n")
                            pubIdNum += 1
                            if not os.path.isfile("Data_Out/IDs_Data/Publications/" + id + ".txt"):
                                pubWriter = open("Data_Out/IDs_Data/Publications/" + id + ".txt", "w", encoding="utf8")
                                pubWriter.write("\t<entry>\n\t\t" + splitAuthUrlContent[i].replace("><", ">\n\t\t<").replace("\t</entry>", "</entry>"))
                                pubWriter.close()
                        pubsAuthors[title].append(author)
                    else:
                        authorsPubDuplicates[author]["SD"] += 1
        except:
            print("Error for " + author)
    print("Finished scraping SD publication data in " + str(time.time() - processStartTime) + " seconds.")
    pubIdWriter.close()
    return authorsPubsSDXMLList

# Scrapes publication data from the Pubmed API.
# --Working as of 7/15/2015--
def scrapePubMedPublicationData(authors):
    pubIdWriter = open("Data_In/IDs_Keys/pubKeys.txt", "a", encoding="utf8")
    global pubIdNum
    processStartTime = time.time()
    print("Scraping Pubmed publication data . . .")
    for author in authors:
        print(author)
        try:
            splitAuthor = author.replace("\'", "").split(" ")
            pubMedAuthName = splitAuthor[1] + " " + splitAuthor[0][0]
            authUrl = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=" + pubMedAuthName
            authUrlReader = urllib.request.urlopen(authUrl)
            authUrlContent = authUrlReader.read()
            splitAuthUrlContent = str(authUrlContent).split("\\n")
            pubIds = []
            for line in splitAuthUrlContent:
                if line.strip(" \n\t\r").startswith("<Id>"):
                    pubIds.append(line.strip(" \t\n\r")[4:-5])
            if len(pubIds) > 0:
                idsUrl = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id="
                for id in pubIds:
                     idsUrl += id + ","
                idsUrl = idsUrl[:-1] + "&rettype=xml&retmode=text"
                idsUrlReader = urllib.request.urlopen(idsUrl)
                idsUrlContent = idsUrlReader.read()
                splitIdsUrlContent = str(idsUrlContent).split("\\n")
                articleFound = False
                pubXML = ""
                compressedPubXML = "\t<PubmedArticle>"
                abstractFound = False
                abstract = ""
                titleFound = False
                title = ""
                for line in splitIdsUrlContent:
                    lineStartsWith = lambda x: line.strip(" \t\n\r").startswith(x)
                    if lineStartsWith("<PubmedArticle>"):
                        articleFound = True
                    if articleFound:
                        pubXML += "\n" + line
                        if lineStartsWith("</PubmedArticle>"):
                            compressedPubXML += "\n\t\t<Title>" + title + "</Title>\n\t\t<Abstract>" + abstract + "</Abstract>\n\t</PubmedArticle>"
                            duplicate = False
                            for storedTitle in authorsPubsTitlesList[author]:
                                if similar(storedTitle, title) >= .93:
                                    duplicate = True
                            authorsPubsFound[author]["PubMed"] += 1
                            if not duplicate:
                                authorsPubsTitlesList[author].append(title)
                                authorsPubsPubMedXMLList[author].append(pubXML)
                                authorsPubsCompressedPubMedXMLList[author].append(compressedPubXML)
                                authorsDataFound[author]["PubMed"] = True
                                if title not in idsPublications.values():
                                    id = "PUB"
                                    for num in range(0, 5-len(str(pubIdNum))):
                                        id += "0"
                                    id += str(pubIdNum)
                                    idsPublications[id] = title
                                    publicationsIDs[title] = id
                                    pubsAuthors[title] = []
                                    pubIdWriter.write(id + "|" + title + "\n")
                                    pubIdNum += 1
                                    if not os.path.isfile("Data_Out/IDs_Data/Publications/" + id + ".txt"):
                                        pubWriter = open("Data_Out/IDs_Data/Publications/" + id + ".txt", "w", encoding="utf8")
                                        pubWriter.write(pubXML)
                                        pubWriter.close()
                                pubsAuthors[title].append(author)
                            else:
                                authorsPubDuplicates[author]["PubMed"] += 1
                            compressedPubXML = "\t<PubmedArticle>"
                            pubXML = ""
                            articleFound = False
                        if lineStartsWith("<AbstractText"):
                            abstractFound = True
                        if abstractFound:
                            splitLine = line.replace("<", ">").split(">")
                            abstract = splitLine[2]
                            abstractFound = False
                        if lineStartsWith("<ArticleTitle>"):
                            if line.strip(" \t\n\r").endswith("</ArticleTitle>"):
                                title = line.strip(" \t\n\r")[14:-15]
                            else:
                                titleFound = True
                        if titleFound:
                            title = line.strip(" \t\n\r")
                            titleFound = False
        except:
            print("Error for " + author)
    pubIdWriter.close()
    print("Finished scraping Pubmed publication data in " + str(time.time() - processStartTime) + " seconds.")

# Scrapes the mailing list data from the local ESIP mailing list data folder.
# Disambiguation: Email
# --Working as of 7/24/2015--
def scrapeMailingListData(authors):
    print("Scraping mailing list data . . .")
    processStartTime = time.time()
    files = os.listdir("Data_In/ESIP_MailingLists")
    for file in files:
        if file.endswith(".xml"):
            name = ""
            mailingList = ""
            email = ""
            lineStartsWith = lambda x: line.strip(" \t\n\r").startswith(x)
            reader = open("Data_In/ESIP_MailingLists/" + file, "r", encoding="utf8")
            for line in reader:
                if lineStartsWith("<Name>"):
                    name = line.strip(" \t\n\r")[6:-7]
                if lineStartsWith("<MailingList>"):
                    mailingList = line.strip(" \t\n\r")[13:-14]
                if lineStartsWith("<Email>"):
                    email = line.strip(" \t\n\r")[7:-8]
            for author in authors.keys():
                if author.lower().replace(" ", "").replace("-", "") == name.replace(" ", "").replace("-", ""):
                    if authorsEmail[author] == email:
                        authorsMailingList[author].append(mailingList)
                        authorsDataFound[author]["MailingList"] = True
    print("Finished scraping mailing list data in " + str(time.time()-processStartTime) + " seconds.")
    return authorsMailingList

# Scrapes the poster data from the local ESIP poster data folder.
def scrapePosterData():
    print("Scraping poster data . . .")
    processStartTime = time.time()
    for file in os.listdir("Data_In/ESIP_Posters"):
        reader = open("Data_In/ESIP_Posters/" + file, "r", encoding="utf8")
        reader.readline()
        for line in reader:
            splitLine = line.split("\",\"")
            title = splitLine[1]
            abstract = splitLine[2]
            authors = splitLine[10].split(",")
            for rawAuthor in authors:
                author = rawAuthor.strip(" \t\n\r").lower()
                if author in authorsPostersXML.keys():
                    authorsPostersXML[author].append("\t<Poster>\n\t\t<Title>" + title + "</Title>\n\t\t<Abstract>" + abstract + "</Abstract>\n\t</Poster>")
                    authorsDataFound[author]["Poster"] = True
    print("Finished scraping poster data in " + str(time.time()-processStartTime) + " seconds.")

# Scrapes MAD publication data and writes it to the Output/MADPublicationData folder.
def writeMADPublicationData():
    authors = []
    scrapedAuthors = []
    authorsReader = open("authorKeys.txt", "r", encoding="utf8")
    for line in authorsReader:
        splitLine = line.split("|")
        authors.append(splitLine[1].replace("\n", ""))
    errorCount = 0
    for author in authors:
        print(author)
        processStartTime = time.time()
        print("Scraping " + author + "\'s MAD publication data . . .")
        authIds = []
        paperIdsKeywordIds = {}
        paperIdsKeywords = {}
        authorSplit = author.split(" ")
        url = "https://api.datamarket.azure.com/MRC/MicrosoftAcademic/v2/Author?$select=ID&$filter=Name%20eq%20%27" + authorSplit[0] + "%20" + authorSplit[1].replace("\'", "").replace("-", "") + "%27"
        try:
            authUrlReader = urllib.request.urlopen(url)
            authUrlContent = str(authUrlReader.read())
            splitUrlContent = authUrlContent.replace("<", ">").split(">")
        except:
            errorCount += 1
            print("Error for " + url)
        authorId = ""
        for term in splitUrlContent:
            if term.isdigit() and authorId == "":
                # authIds.append(term)
                authorId = term
        if authorId != "":
            authIds.append(authorId)
        for authId in authIds:
            authPapersUrl = "https://api.datamarket.azure.com/MRC/MicrosoftAcademic/v2/Paper_Author?$select=PaperID&$filter=AuthorID%20eq%20" + authId
            try:
                authPapersUrlReader = urllib.request.urlopen(authPapersUrl)
                authPapersContent = str(authPapersUrlReader.read())
                splitAuthPapersContent = authPapersContent.replace("<", ">").split(">")
            except:
                errorCount += 1
                print("Error for " + authPapersUrl)
            for term in splitAuthPapersContent:
                if term.isdigit():
                    paperIdsKeywordIds[term] = []
                    paperIdsKeywords[term] = []
        for paperId in paperIdsKeywordIds.keys():
            paperKeywordIdUrl = "https://api.datamarket.azure.com/MRC/MicrosoftAcademic/v2/Paper_Keyword?$select=KeywordID&$filter=CPaperID%20eq%20" + paperId
            try:
                paperKeywordIdUrlReader = urllib.request.urlopen(paperKeywordIdUrl)
                paperKeywordIdContent = str(paperKeywordIdUrlReader.read())
                splitPaperKeywordIdContent = paperKeywordIdContent.replace("<", ">").split(">")
                for term in splitPaperKeywordIdContent:
                    if term.isdigit():
                        paperIdsKeywordIds[paperId].append(term)
            except:
                errorCount += 1
                print("Error for " + paperKeywordIdUrl)
            pubXML = "\t<Publication>\n\t\t<MADID>" + paperId + "</MADID>"
            paperTitleUrl = "https://api.datamarket.azure.com/MRC/MicrosoftAcademic/v2/Paper?$select=ID,Title&$filter=ID%20eq%20" + paperId
            title = ""
            try:
                paperTitleReader = urllib.request.urlopen(paperTitleUrl)
                paperTitleContent = str(paperTitleReader.read())
                splitPaperTitleContent = paperTitleContent.replace("<", ">").split(">")
                title = splitPaperTitleContent[len(splitPaperTitleContent)-11]
                pubXML += "\n\t\t<Title>" + title + "</Title>"
            except:
                errorCount += 1
                print("Error for " + paperTitleUrl)
            for keywordId in paperIdsKeywordIds[paperId]:
                keywordUrl = "https://api.datamarket.azure.com/MRC/MicrosoftAcademic/v2/Keyword?$select=DisplayName&$filter=ID%20eq%20" + keywordId
                try:
                    keywordUrlReader = urllib.request.urlopen(keywordUrl)
                    keywordContent = str(keywordUrlReader.read())
                    splitKeywordContent = keywordContent.replace("<", ">").split(">")
                    for num in range(0, len(splitKeywordContent)):
                        if splitKeywordContent[num] == "d:DisplayName":
                            paperIdsKeywords[paperId].append(splitKeywordContent[num+1])
                except:
                    errorCount += 1
                    print("Error for " + keywordUrl)
            for keyword in paperIdsKeywords[paperId]:
                pubXML += "\n\t\t<Keyword>" + keyword + "</Keyword>"
            pubXML += "\n\t</Publication>"
            duplicate = False
            for storedTitle in authorsPubsTitlesList[author]:
                if similar(storedTitle, title) >= .93:
                    duplicate = True
            if not duplicate and not pubXML == "":
                authorsPubsTitlesList[author].append(title)
                publicationWriter = open("OutputOld/MADPublicationData/" + author.replace(" ", "") + ".txt", "a", encoding="utf8")
                publicationWriter.write(pubXML)
                authorsDataFound[author]["MAD"] = True
        print("Finished scraping " + author + "\'s MAD publication data in " + str(time.time()-processStartTime) + " seconds.")
        scrapedAuthors.append(author)
    for author in scrapedAuthors:
        print(author)
    print(str(errorCount) + " errors.")
    return authorsPubsMADXMLList

# Scrapes the publication data from the AGU abstracts and Google Scholar and writes it to the Output folder.
# --Working as of 7/24/2015--
def scrapePubData(authPubsXML):
    scrapeLocalMADPublicationData(authorsPubsMADXMLList)
    authorsPubsAGUXMLList = scrapeAGUPublicationData(authPubsXML)
    #authorsPubsGSXMLList = scrapeGSPublicationData(authsGSLinks)
    scrapeSDPublicationData(authorsPubsSDXMLList)
    scrapePubMedPublicationData(authorsPubsPubMedXMLList)
    for author in authorsPubsAGUXMLList.keys():
        if authorsDataFound[author]["AGU"]:
            for item in authorsPubsAGUXMLList[author]:
                authorsProfiles[author] += item.replace("\n", "\n\t")
            for item in authorsPubsCompressedAGUXMLList[author]:
                authorsCompressedProfiles[author] += item
        if authorsDataFound[author]["MAD"]:
            for item in authorsPubsMADXMLList[author]:
                authorsProfiles[author] += "\n" + item
            for item in authorsPubsCompressedMADXMLList[author]:
                authorsCompressedProfiles[author] += "\n" + item
        if authorsDataFound[author]["SD"]:
            for item in authorsPubsSDXMLList[author]:
                authorsProfiles[author] += "\n" + item
            for item in authorsPubsCompressedSDXMLList[author]:
                authorsCompressedProfiles[author] += "\n" + item
        if authorsDataFound[author]["PubMed"]:
            for item in authorsPubsPubMedXMLList[author]:
                authorsProfiles[author] += "\n\t" + item.replace("\n", "\n\t")
            for item in authorsPubsCompressedPubMedXMLList[author]:
                authorsCompressedProfiles[author] += "\n" + item
    authorsPubsAGUXMLList.clear()
    authorsPubsCompressedAGUXMLList.clear()
    authorsPubsMADXMLList.clear()
    authorsPubsCompressedMADXMLList.clear()
    authorsPubsSDXMLList.clear()
    authorsPubsCompressedSDXMLList.clear()
    authorsPubsPubMedXMLList.clear()
    authorsPubsCompressedPubMedXMLList.clear()

# Scrapes the grant data from the local NSF folder and the online NSF API and writes it to the Grants folder in the Output folder.
# Also deduplicates the local and online grant data.
# --Working as of 7/24/2015--
def scrapeGrantData(authsGrantsLocalXMLList, authsGrantsOnlineXMLList):
    authorsGrantsLocalXMLList = scrapeLocalGrantData(authsGrantsLocalXMLList)
    authorsGrantsOnlineXMLList = scrapeOnlineGrantData(authsGrantsOnlineXMLList)
    debugger = open("debug.txt", "w", encoding="utf8")
    for author in authorsGrantsOnlineXMLList.keys():
        debugger.write(author + "\n")
        for award in authorsGrantsOnlineXMLList[author]:
            debugger.write(award + "\n")
        debugger.write("\n")
    for author in authorsGrantsLocalXMLList.keys():
        if len(authorsGrantsLocalXMLList[author]) > 0:
            if len(authorsGrantsOnlineXMLList[author]) > 0:
                for localAward in authorsGrantsLocalXMLList[author]:
                    localAwardID = "localNull"
                    localAwardIndex = localAward.find("<AwardID>")
                    if localAwardIndex > -1:
                        localAwardID = localAward[localAwardIndex + 9:localAwardIndex + 16]
                    for onlineAward in authorsGrantsOnlineXMLList[author]:
                        onlineAwardID = "onlineNull"
                        onlineAwardIndex = onlineAward.find("<id>")
                        if onlineAwardIndex > -1:
                            onlineAwardID = onlineAward[onlineAwardIndex + 4:onlineAwardIndex + 11]
                        if localAwardID == onlineAwardID:
                            authorsGrantsCompressedOnlineXMLList[author].remove(authorsGrantsCompressedOnlineXMLList[author][authorsGrantsOnlineXMLList[author].index(onlineAward)])
                            authorsGrantsOnlineXMLList[author].remove(onlineAward)
                    authorsGrantsXMLList[author].append(localAward)
                    authorsGrantsCompressedXMLList[author].append(authorsGrantsCompressedLocalXMLList[author][authorsGrantsLocalXMLList[author].index(localAward)])
                for onlineAward in authorsGrantsOnlineXMLList[author]:
                    authorsGrantsXMLList[author].append(onlineAward)
                    authorsGrantsCompressedXMLList[author].append(authorsGrantsCompressedOnlineXMLList[author][authorsGrantsOnlineXMLList[author].index(onlineAward)])
            else:
                for award in authorsGrantsLocalXMLList[author]:
                    authorsGrantsXMLList[author].append(award)
                    authorsGrantsCompressedXMLList[author].append(authorsGrantsCompressedLocalXMLList[author][authorsGrantsLocalXMLList[author].index(award)])
        elif len(authorsGrantsOnlineXMLList[author]) > 0:
            for award in authorsGrantsOnlineXMLList[author]:
                authorsGrantsXMLList[author].append(award)
                authorsGrantsCompressedXMLList[author].append(authorsGrantsCompressedOnlineXMLList[author][authorsGrantsOnlineXMLList[author].index(award)])
    for author in authorsGrantsOnlineXMLList.keys():
        debugger.write(author + "\n")
        for award in authorsGrantsOnlineXMLList[author]:
            debugger.write(award + "\n")
        debugger.write("\n")
    debugger.close()
    for author in authorsGrantsXMLList.keys():
        if len(authorsGrantsXMLList[author]) > 0:
            writer = open("OutputOld/Grants/" + author.replace(" ", "") + "Grants.xml", "w", encoding="utf8")
            compressedWriter = open("OutputOld/Grants/" + author.replace(" ", "") + "CompressedGrants.xml", "w", encoding="utf8")
            for award in authorsGrantsXMLList[author]:
                writer.write(award.replace("\n", "\n\t"))
                authorsProfiles[author] += award.replace("\n", "\n\t")
            for award in authorsGrantsCompressedXMLList[author]:
                compressedWriter.write(award)
                authorsCompressedProfiles[author] += award
            writer.close()
            compressedWriter.close()
    authorsGrantsOnlineXMLList.clear()
    authorsGrantsCompressedOnlineXMLList.clear()
    authorsGrantsLocalXMLList.clear()
    authorsGrantsCompressedLocalXMLList.clear()
    authorsGrantsXMLList.clear()
    authorsGrantsCompressedXMLList.clear()

# Adds the attendee info to the profiles.
def addAttendeeData():
    for author in authorsEmail.keys():
        attendeeInfo = "\t<AttendeeInfo>"
        attendeeInfo += "\n\t\t<Email>" + authorsEmail[author] + "</Email>\n"
        attendeeInfo += "\t\t<Organization>" + authorsOrganization[author] + "</Organization>\n"
        attendeeInfo += "\t</AttendeeInfo>\n"
        authorsProfiles[author] += attendeeInfo
        authorsCompressedProfiles[author] += attendeeInfo

# Adds the mailing list and session info to the profiles.
def addSimpleData():
    for author in authorsMailingList.keys():
        for mailingList in authorsMailingList[author]:
            authorsProfiles[author] += "\t<MailingList>\n\t\t<ListName>" + mailingList + "</ListName>\n\t</MailingList>\n"
            authorsCompressedProfiles[author] += "\t<MailingList>\n\t\t<ListName>" + mailingList + "</ListName>\n\t</MailingList>\n"
        for session in authorsSessions[author]:
            authorsProfiles[author] += sessionXML[session]
            authorsCompressedProfiles[author] += sessionXML[session]
        for conference in authorsConferences[author]:
            authorsProfiles[author] += "\t<Conference>\n\t\t<ID>" + conference + "</ID>\n\t</Conference>\n"
            authorsCompressedProfiles[author] += "\t<Conference>\n\t\t<ID>" + conference + "</ID>\n\t</Conference>\n"
        for posterXML in authorsPostersXML[author]:
            authorsProfiles[author] += posterXML
            authorsCompressedProfiles[author] += posterXML

# Scrapes all of the data for the profiles then writes them to the appropriate folders.
def scrapeProfileData(authPubsXML, authsGrantsLocalXMLList, authsGrantsOnlineXMLList, authsMailingList):
    addAttendeeData()
    scrapePosterData()
    scrapePubData(authPubsXML)
    scrapeGrantData(authsGrantsLocalXMLList, authsGrantsOnlineXMLList)
    scrapeMailingListData(authsMailingList)
    scrapeESIPSessionData()
    scrapeESIPAsilomarSessionData()
    addSimpleData()
    for id in idsAuthors.keys():
        author = idsAuthors[id]
        if not authorsProfiles[author] == "":
            fullProfile = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<Attendee>\n\t" + authorsProfiles[author] + "</Attendee>"
            compressedProfile = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<Attendee>\n\t" + authorsCompressedProfiles[author] + "</Attendee>"
            fileName = id + "_" + author.replace(" ", "") + ".txt"
            compressedFileName = id + "_" + author.replace(" ", "") + "Compressed.txt"
            profileWriter = open("Data_Out/Profile_Data/" + fileName, "w", encoding="utf8")
            compressedProfileWriter = open("Data_Out/Profile_Data/" + compressedFileName, "w", encoding="utf8")
            profileWriter.write(fullProfile)
            compressedProfileWriter.write(compressedProfile)
            profileWriter.close()
            compressedProfileWriter.close()
            if authorsDataFound[author]["NSF"]:
                profileWriter = open("Data_Out/Profile_Data/Grants/" + fileName, "w", encoding="utf8")
                compressedProfileWriter = open("Data_Out/Profile_Data/Grants/" + compressedFileName, "w", encoding="utf8")
                profileWriter.write(fullProfile)
                compressedProfileWriter.write(compressedProfile)
                profileWriter.close()
                compressedProfileWriter.close()
            if authorsDataFound[author]["MailingList"]:
                profileWriter = open("Data_Out/Profile_Data/MailingLists/" + fileName, "w", encoding="utf8")
                compressedProfileWriter = open("Data_Out/Profile_Data/MailingLists/" + compressedFileName, "w", encoding="utf8")
                profileWriter.write(fullProfile)
                compressedProfileWriter.write(compressedProfile)
                profileWriter.close()
                compressedProfileWriter.close()
            if authorsDataFound[author]["ESIP_Session"]:
                profileWriter = open("Data_Out/Profile_Data/Sessions/" + fileName, "w", encoding="utf8")
                compressedProfileWriter = open("Data_Out/Profile_Data/Sessions/" + compressedFileName, "w", encoding="utf8")
                profileWriter.write(fullProfile)
                compressedProfileWriter.write(compressedProfile)
                profileWriter.close()
                compressedProfileWriter.close()
            if authorsDataFound[author]["AGU"] or authorsDataFound[author]["MAD"] or authorsDataFound[author]["SD"] or authorsDataFound[author]["PubMed"]:
                profileWriter = open("Data_Out/Profile_Data/Publications/" + fileName, "w", encoding="utf8")
                compressedProfileWriter = open("Data_Out/Profile_Data/Publications/" + compressedFileName, "w", encoding="utf8")
                profileWriter.write(fullProfile)
                compressedProfileWriter.write(compressedProfile)
                profileWriter.close()
                compressedProfileWriter.close()
                if authorsDataFound[author]["NSF"]:
                    profileWriter = open("Data_Out/Profile_Data/Publications/Publications&Grants/" + fileName, "w", encoding="utf8")
                    compressedProfileWriter = open("Data_Out/Profile_Data/Publications/Publications&Grants/" + compressedFileName, "w", encoding="utf8")
                    profileWriter.write(fullProfile)
                    compressedProfileWriter.write(compressedProfile)
                    profileWriter.close()
                    compressedProfileWriter.close()
                if authorsDataFound[author]["MailingList"]:
                    profileWriter = open("Data_Out/Profile_Data/Publications/Publications&MailingList/" + fileName, "w", encoding="utf8")
                    compressedProfileWriter = open("Data_Out/Profile_Data/Publications/Publications&MailingList/" + compressedFileName, "w", encoding="utf8")
                    profileWriter.write(fullProfile)
                    compressedProfileWriter.write(compressedProfile)
                    profileWriter.close()
                    compressedProfileWriter.close()
                if authorsDataFound[author]["ESIP_Session"]:
                    profileWriter = open("Data_Out/Profile_Data/Publications/Publications&Sessions/" + fileName, "w", encoding="utf8")
                    compressedProfileWriter = open("Data_Out/Profile_Data/Publications/Publications&Sessions/" + compressedFileName, "w", encoding="utf8")
                    profileWriter.write(fullProfile)
                    compressedProfileWriter.write(compressedProfile)
                    profileWriter.close()
                    compressedProfileWriter.close()
                if authorsDataFound[author]["AGU"]:
                    profileWriter = open("Data_Out/Profile_Data/Publications/PublicationsAGU/" + fileName, "w", encoding="utf8")
                    compressedProfileWriter = open("Data_Out/Profile_Data/Publications/PublicationsAGU/" + compressedFileName, "w", encoding="utf8")
                    profileWriter.write(fullProfile)
                    compressedProfileWriter.write(compressedProfile)
                    profileWriter.close()
                    compressedProfileWriter.close()
                if authorsDataFound[author]["MAD"]:
                    profileWriter = open("Data_Out/Profile_Data/Publications/PublicationsMAD/" + fileName, "w", encoding="utf8")
                    compressedProfileWriter = open("Data_Out/Profile_Data/Publications/PublicationsMAD/" + compressedFileName, "w", encoding="utf8")
                    profileWriter.write(fullProfile)
                    compressedProfileWriter.write(compressedProfile)
                    profileWriter.close()
                    compressedProfileWriter.close()
                if authorsDataFound[author]["SD"]:
                    profileWriter = open("Data_Out/Profile_Data/Publications/PublicationsSD/" + fileName, "w", encoding="utf8")
                    compressedProfileWriter = open("Data_Out/Profile_Data/Publications/PublicationsSD/" + compressedFileName, "w", encoding="utf8")
                    profileWriter.write(fullProfile)
                    compressedProfileWriter.write(compressedProfile)
                    profileWriter.close()
                    compressedProfileWriter.close()
                if authorsDataFound[author]["PubMed"]:
                    profileWriter = open("Data_Out/Profile_Data/Publications/PublicationsPubMed/" + fileName, "w", encoding="utf8")
                    compressedProfileWriter = open("Data_Out/Profile_Data/Publications/PublicationsPubMed/" + compressedFileName, "w", encoding="utf8")
                    profileWriter.write(fullProfile)
                    compressedProfileWriter.write(compressedProfile)
                    profileWriter.close()
                    compressedProfileWriter.close()

# Adds the grant data to the each attendee's profile file.
# --Working as of 7/24/2015--
def compileProfiles():
    for author in authorsPubsAGUXMLList.keys():
        if len(authorsMailingList[author]) > 0:
            if os.path.isfile("Output/" + author.replace(" ", "") + ".xml"):
                appender = open("Output/" + author.replace(" ", "") + ".xml", "a", encoding="utf8")
                compressedAppender = open("Output/" + author.replace(" ", "") + "Compressed.xml", "a", encoding="utf8")
                for mailingList in authorsMailingList[author]:
                    appender.write("\t<MailingList>\n\t\t<ListName>" + mailingList + "</ListName>\n\t</MailingList>\n")
                    compressedAppender.write("\t<MailingList>\n\t\t<ListName>" + mailingList + "</ListName>\n\t</MailingList>\n")
                appender.close()
                compressedAppender.close()
            else:
                writer = open("Output/" + author.replace(" ", "") + ".xml", "w", encoding="utf8")
                writer.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<Attendee>\n")
                compressedWriter = open("Output/" + author.replace(" ", "") + "Compressed.xml", "w", encoding="utf8")
                compressedWriter.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<Attendee>\n")
                for mailingList in authorsMailingList[author]:
                    writer.write("\t<MailingList>\n\t\t<ListName>" + mailingList + "</ListName>\n\t</MailingList>\n")
                    compressedWriter.write("\t<MailingList>\n\t\t<ListName>" + mailingList + "</ListName>\n\t</MailingList>\n")
                writer.close()
                compressedWriter.close()
        if os.path.isfile("Output/Grants/" + author.replace(" ", "") + "Grants.xml"):
            reader = open("Output/Grants/" + author.replace(" ", "") + "Grants.xml")
            compressedReader = open("Output/Grants/" + author.replace(" ", "") + "CompressedGrants.xml")
            if os.path.isfile("Output/" + author.replace(" ", "") + ".xml"):
                appender = open("Output/" + author.replace(" ", "") + ".xml", "a", encoding="utf8")
                compressedAppender = open("Output/" + author.replace(" ", "") + "Compressed.xml", "a", encoding="utf8")
                appender.write(reader.read())
                compressedAppender.write(compressedReader.read())
                appender.write("</Attendee>")
                compressedAppender.write("</Attendee>")
                appender.close()
                compressedAppender.close()
            else:
                writer = open("Output/" + author.replace(" ", "") + ".xml", "w", encoding="utf8")
                compressedWriter = open("Output/" + author.replace(" ", "") + "Compressed.xml", "w", encoding="utf8")
                writer.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<Attendee>\n")
                compressedWriter.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<Attendee>\n")
                writer.write(reader.read())
                compressedWriter.write(compressedReader.read())
                writer.write("</Attendee>")
                compressedWriter.write("</Attendee>")
                writer.close()
                compressedWriter.close()
            reader.close()
            compressedReader.close()
        elif os.path.isfile("Output/" + author.replace(" ", "") + ".xml"):
            appender = open("Output/" + author.replace(" ", "") + ".xml", "a", encoding="utf8")
            compressedAppender = open("Output/" + author.replace(" ", "") + "Compressed.xml", "a", encoding="utf8")
            appender.write("</Attendee>")
            compressedAppender.write("</Attendee>")
            appender.close()
            compressedAppender.close()

# Scrapes the supplemental publication data from the SD, MAD, and Pubmed APIs and writes it to the SupplementalPublications folder in the Output folder.
# --Working as of 7/15/2015--
def scrapeSupplementalPubData():
    scrapeSDPublicationData(authorsPubsSDXMLList)
    scrapePubMedPublicationData(authorsPubsPubMedXMLList)
    scrapeMADPublicationData(authorsPubsMADXMLList)
    for author in authorsPubsMADXMLList.keys():
        if len(authorsPubsMADXMLList[author]) > 0 or len(authorsPubsSDXMLList[author]) > 0 or len(authorsPubsPubMedXMLList[author]) > 0:
            pubsSuppWriter = open("Output/SupplementalPublications/" + author.replace(" ", "") + "SupplementalPublications.xml", "w", encoding="utf8")
            pubsSuppWriter.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>")
            pubsCompressedSuppWriter = open("Output/SupplementalPublications/" + author.replace(" ", "") + "CompressedSupplementalPublications.xml", "w", encoding="utf8")
            pubsCompressedSuppWriter.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>")
            for publication in authorsPubsMADXMLList[author]:
                pubsSuppWriter.write("\n" + publication)
            for publication in authorsPubsSDXMLList[author]:
                pubsSuppWriter.write("\n" + publication)
            for publication in authorsPubsPubMedXMLList[author]:
                pubsSuppWriter.write("\n" + publication)
            for publication in authorsPubsCompressedMADXMLList[author]:
                pubsCompressedSuppWriter.write("\n" + publication)
            for publication in authorsPubsCompressedSDXMLList[author]:
                pubsCompressedSuppWriter.write("\n" + publication)
            for publication in authorsPubsCompressedPubMedXMLList[author]:
                pubsCompressedSuppWriter.write("\n" + publication)
            pubsSuppWriter.close()
            pubsCompressedSuppWriter.close()

# Writes the files mapping each attendee to sessions and publications,
# publications to authors,
# and sessions and authors.
def writeIDMapping():
    authorsMappingWriter = open("Data_Out/IDs_Data/authorNodes.txt", "w", encoding="utf8")
    for id in idsAuthors.keys():
        author = idsAuthors[id]
        authorsMappingWriter.write(id)
        for session in authorsSessions[author]:
            authorsMappingWriter.write("," + sessionsIDs[session])
        for publication in authorsPubsTitlesList[author]:
            authorsMappingWriter.write("," + publicationsIDs[publication])
        for keyword in authorsKeywords[author]:
            authorsMappingWriter.write("," + keywordsIDs[keyword])
        authorsMappingWriter.write("\n")
    authorsMappingWriter.close()
    sessionsMappingWriter = open("Data_Out/IDs_Data/sessionNodes.txt", "w", encoding="utf8")
    for id in idsSessions.keys():
        session = idsSessions[id]
        sessionsMappingWriter.write(id)
        for author in sessionAuthors[session]:
            sessionsMappingWriter.write("," + authorsIDs[author])
        sessionsMappingWriter.write("\n")
    sessionsMappingWriter.close()
    publicationsMappingWriter = open("Data_Out/IDs_Data/publicationNodes.txt", "w", encoding="utf8")
    for id in idsPublications.keys():
        publication = idsPublications[id]
        publicationsMappingWriter.write(id)
        for author in pubsAuthors[publication]:
            publicationsMappingWriter.write("," + authorsIDs[author])
        if publication in pubsKeywords.keys():
            for keyword in pubsKeywords[publication]:
                publicationsMappingWriter.write("," + keywordsIDs[keyword])
        publicationsMappingWriter.write("\n")
    publicationsMappingWriter.close()
    keywordsMappingWriter = open("Data_Out/IDs_Data/keywordNodes.txt", "w", encoding="utf8")
    for id in idsKeywords.keys():
        keyword = idsKeywords[id]
        keywordsMappingWriter.write(id)
        for author in keywordsAuthors[keyword]:
            keywordsMappingWriter.write("," + authorsIDs[author])
        for publication in keywordsPubs[keyword]:
            keywordsMappingWriter.write("," + publicationsIDs[publication])
        keywordsMappingWriter.write("\n")
    keywordsMappingWriter.close()

# Writes the attendees and session ID data to the IDs_Data folder.
def writeIDData():
    for id in idsAuthors.keys():
        authName = idsAuthors[id]
        authorWriter = open("Data_Out/IDs_Data/Attendees/" + id + ".txt", "w", encoding="utf8")
        authorWriter.write("<Attendee>\n\t<Name>" + authName + "</Name>\n\t<Email>" + authorsEmail[authName] + "</Email>\n\t<Organization>" + authorsOrganization[authName] + "</Organization>\n</Attendee>")
        authorWriter.close()
    for id in idsSessions.keys():
        sessionWriter = open("Data_Out/IDs_Data/Sessions/" + id + ".txt", "w", encoding="utf8")
        sessionWriter.write("<Session>\n\t<Name>" + idsSessions[id] + "</Name>\n</Session>")
        sessionWriter.close()
    for id in idsKeywords.keys():
        keywordWriter = open("Data_Out/IDs_Data/Keywords/" + id + ".txt", "w", encoding="utf8")
        keywordWriter.write("<Keyword>" + idsKeywords[id] + "</Keyword>")
        keywordWriter.close()

def writeDataFound():
    dataFoundWriter = open("Data_Out/DataFound.csv", "w", encoding="utf8")
    dataFoundWriter.write("Author,ID,AGU,Science Direct,Microsoft Academic,PubMed,Grants,MailingList,ESIP Session,Poster,Conference,Asilomar\n")
    dataList = ["AGU", "SD", "MAD", "PubMed", "NSF", "MailingList", "ESIP_Session", "Poster", "Conference", "Asilomar"]
    for author in authorsDataFound.keys():
        dataFoundWriter.write(author + "," + authorsIDs[author])
        for dataType in dataList:
            dataFoundWriter.write("," + str(authorsDataFound[author][dataType]))
        dataFoundWriter.write("\n")

# Scans the AGU ESIP matches data to find information about match frequency for each person.
# --Working as of 7/20/15--
def scanAGUESIPMatches():
    matchesDict = {}
    for file in os.listdir("Data_In/ESIP_AGU_Matches/"):
        reader = open("Data_In/ESIP_AGU_Matches/" + file, "r")
        for line in reader:
            if line.strip(" \t\n\r").startswith("<EsipName>"):
                name = line.strip(" \t\n\r")[10:-11]
                if name in matchesDict.keys():
                    matchesDict[name] += 1
                else:
                    matchesDict[name] = 1
    attendeeTotal = 0
    for attendee in matchesDict.keys():
        attendeeTotal += matchesDict[attendee]
        if matchesDict[attendee] > 1:
            print(attendee + " " + str(matchesDict[attendee]))
    print(float(attendeeTotal)/float(len(matchesDict.keys())))

# Scans the AGU abstract data to make a list of possibly mismatched data.
# --Working as of 7/23/15--
def scanAGUData():
    mismatchedDataCount = 0
    mismatchedDataXML = "<DataList>"
    for folder in os.listdir("Data_In/AGU_IN_Abstracts"):
        if "." not in folder:
            print("Scanning AGU abstracts data from " + folder + ". . .")
            processStartTime = time.time()
            for file in os.listdir("Data_In/AGU_IN_Abstracts/" + folder):
                if file.endswith(".xml"):
                    name = ""
                    lastName = ""
                    email = ""
                    reader = open("Data_In/AGU_IN_Abstracts/" + folder + "/" + file, "r", encoding="utf8")
                    for line in reader:
                        if line.strip(" \t\n\r").startswith("<Name>"):
                            name = line.strip(" \t\n\r")[6:-7]
                            splitName = name.split(",")
                            lastName = splitName[0].lower().replace(" ", "")
                            if len(splitName[1]) > 0:
                                firstInitial = splitName[1].strip(" ")[0]
                            else:
                                firstInitial = ""
                        if line.strip(" \t\n\r").startswith("<Email>"):
                            email = line.strip(" \t\n\r")[7:-8]
                            if not email.lower().startswith(firstInitial.lower()) and not lastName[0:4] in email.lower():
                                mismatchedDataXML += "\n\t<MismatchedData>\n\t\t<Name>" + name + "</Name>\n\t\t<Email>" + email + "</Email>\n\t\t<File>" + file + "</File>\n\t</MismatchedData>"
                                mismatchedDataCount += 1
    mismatchedDataXML += "\n</DataList>"
    writer = open("mismatchedData.xml", "w", encoding="utf8")
    writer.write(mismatchedDataXML)
    writer.close()
    print(str(mismatchedDataCount))
"""
def scrapeESIPSessionData():
    for file in os.listdir("ESIP_Sessions/"):
        sessionFileReader = open("ESIP_Sessions/" + file, "r", encoding="utf8")
        authorsList = []
        for line in sessionFileReader:
            splitLine = line.split(",")
            if splitLine[0] not in authorsList:
                authorsList.append(splitLine[0])
                authorsSessions[splitLine[0]].append(file[:-4])
                authorsDataFound[splitLine[0]]["ESIP_Session"] = True
        sessionAuthors[file[:-4]] = authorsList
"""

# Calculates various statistics for the scraped data.
# Currently finds the number of attendee with different types of data
# and the average runtime based on runtimes.txt
# --Working as of 7/24/15--
def calcScrapeStats():
    pubsAuthNum = 0
    pubsAuthList = []
    grantsAuthNum = 0
    grantsAuthList = []
    mailingListAuthNum = 0
    mailingListAuthList = []
    pubsGrantsAuthNum = 0
    pubsGrantsAuthList = []
    pubsOrGrantsOrMailingListAuthNum = 0
    pubsOrGrantsOrMailingListAuthList = []
    pubsOrGrantsAuthNum = 0
    pubsOrGrantsAuthList = []
    mailingListOnlyAuthNum = 0
    mailingListOnlyAuthList = []
    for author in authorsPubsAGUXMLList.keys():
        hasPublications = lambda auth: len(authorsPubsAGUXMLList[author]) > 0 or len(authorsPubsGSXMLList[author]) > 0
        hasGrants = lambda auth: len(authorsGrantsLocalXMLList[author]) > 0
        hasMailingLists = lambda auth: len(authorsMailingList[author]) > 0
        if hasPublications(author):
            pubsAuthNum += 1
            pubsAuthList.append(author)
            if hasGrants(author):
                pubsGrantsAuthNum += 1
                pubsGrantsAuthList.append(author)
        if hasMailingLists(author):
            mailingListAuthNum += 1
            mailingListAuthList.append(author)
            if not hasPublications(author) and not hasGrants(author):
                mailingListOnlyAuthNum += 1
                mailingListOnlyAuthList.append(author)
        if hasGrants(author):
            grantsAuthNum += 1
            grantsAuthList.append(author)
        if hasGrants(author) or hasPublications(author):
            pubsOrGrantsAuthNum += 1
            pubsOrGrantsAuthList.append(author)
        if hasPublications(author) or hasGrants(author) or hasMailingLists(author):
            pubsOrGrantsOrMailingListAuthNum += 1
            pubsOrGrantsOrMailingListAuthList.append(author)
    runtimeReader = open("runtimes.txt", "r", encoding="utf8")
    runtimeTotal = 0
    runtimeNum = 0
    for line in runtimeReader:
        runtimeNum += 1
        runtimeTotal += float(line.strip("\n"))
    runtimeReader.close()
    scrapeStatsWriter = open("scrapeStats.txt", "w", encoding="utf8")
    scrapeStatsWriter.write("There are " + str(pubsAuthNum) + " authors with publication data.\n")
    scrapeStatsWriter.write("There are " + str(grantsAuthNum) + " authors with grant data.\n")
    scrapeStatsWriter.write("There are " + str(mailingListAuthNum) + " authors with mailing list data.\n")
    scrapeStatsWriter.write("There are " + str(pubsGrantsAuthNum) + " authors with publication and grant data.\n")
    scrapeStatsWriter.write("There are " + str(pubsOrGrantsAuthNum) + " authors with publication or grant data.\n")
    scrapeStatsWriter.write("There are " + str(mailingListOnlyAuthNum) + " authors with only mailing list data.\n")
    scrapeStatsWriter.write("There are " + str(pubsOrGrantsOrMailingListAuthNum) + " authors with publication or grant or mailing list data.\n")
    runtimeAvg = runtimeTotal/runtimeNum
    scrapeStatsWriter.write("The average runtime is now " + str(runtimeAvg))

def calcDuplStats():
    sources = ["AGU","MAD", "SD", "PubMed"]
    for source in sources:
        duplStatsWriter = open("Data_Out/Duplicate_Stats/" + source + "DuplStats.txt", "w", encoding="utf8")
        for author in authorsPubsFound.keys():
            duplStatsWriter.write(author + "|" + str(authorsPubsFound[author][source]) + "|" + str(authorsPubDuplicates[author][source]) + "\n")
        duplStatsWriter.close()
    duplEmailWriter = open("Data_Out/duplicateEmails.txt", "w", encoding="utf8")
    for author in authorsDuplicatesEmails.keys():
        duplEmailWriter.write(author)
        for email in authorsDuplicatesEmails[author]:
            duplEmailWriter.write("|" + email)
        duplEmailWriter.write("\n")
    duplEmailWriter.close()

# Initializes all the needed dictionaries.
initAuthors()
initIds()

#findMissingAuthors()

#assignIDs()

#scanAGUESIPMatches()
#scanAGUData()

# Runs the scraping methods.
scrapeProfileData(authorsPubsAGUXMLList,authorsGrantsLocalXMLList, authorsGrantsOnlineXMLList, authorsMailingList)
writeIDData()
writeIDMapping()
writeDataFound()
calcDuplStats()

#writeMADPublicationData()

#scrapeMailingListData(authorsMailingList)
#scrapePubData(authorsPubsAGUXMLList, authorsGSLinks)
#scrapeGrantData(authorsGrantsLocalXMLList, authorsGrantsOnlineXMLList)
#compileProfiles()
#scrapeSupplementalPubData()
#authorsGrantsOnlineXMLList = scrapeOnlineGrantData(authorsGrantsOnlineXMLList)
#authorsGrantsLocalXMLList = scrapeLocalGrantData(authorsGrantsLocalXMLList)

#writeESIPSessionData()

# Logs the runtime of this program execution.
runTimeLogger = open("runtimes.txt", "a")
runTimeLogger.write("\n" + str(time.time() - progStartTime))
runTimeLogger.close()

# Calculates the scraped data statistics.
#calcScrapeStats()
print("Finished writing in " + str(time.time() - progStartTime) + " seconds.")
print("\nDone!")
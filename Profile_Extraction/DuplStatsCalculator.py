import statistics

pubs = []
dupls = []
AGUReader = open("Data_Out/Duplicate_Stats/AGUDuplStats.txt", "r", encoding="utf8")
for line in AGUReader:
	splitline = line.split("|")
	pubs.append(int(splitline[1]))
	dupls.append(int(splitline[2]))
print("Total AGU Pubs: " + str(sum(pubs)))
print("Total AGU Dupls: " + str(sum(dupls)))
print("Mean AGU Pubs: " + str(statistics.mean(pubs)))
print("Mean AGU Dupls: " + str(statistics.mean(dupls)))
print("Stddev AGU Pubs: " + str(statistics.pstdev(pubs)))
print("Stddev AGU Dupls: " + str(statistics.pstdev(dupls)))
AGUReader.close()

pubs = []
dupls = []
SDReader = open("Data_Out/Duplicate_Stats/SDDuplStats.txt", "r", encoding="utf8")
for line in SDReader:
	splitline = line.split("|")
	pubs.append(int(splitline[1]))
	dupls.append(int(splitline[2]))
print("Total SD Pubs: " + str(sum(pubs)))
print("Total SD Dupls: " + str(sum(dupls)))
print("Mean SD Pubs: " + str(statistics.mean(pubs)))
print("Mean SD Dupls: " + str(statistics.mean(dupls)))
print("Stddev SD Pubs: " + str(statistics.pstdev(pubs)))
print("Stddev SD Dupls: " + str(statistics.pstdev(dupls)))
SDReader.close()

pubs = []
dupls = []
MADReader = open("Data_Out/Duplicate_Stats/MADDuplStats.txt", "r", encoding="utf8")
for line in MADReader:
	splitline = line.split("|")
	pubs.append(int(splitline[1]))
	dupls.append(int(splitline[2]))
print("Total MAD Pubs: " + str(sum(pubs)))
print("Total MAD Dupls: " + str(sum(dupls)))
print("Mean MAD Pubs: " + str(statistics.mean(pubs)))
print("Mean MAD Dupls: " + str(statistics.mean(dupls)))
print("Stddev MAD Pubs: " + str(statistics.pstdev(pubs)))
print("Stddev MAD Dupls: " + str(statistics.pstdev(dupls)))
MADReader.close()

pubs = []
dupls = []
PubMedReader = open("Data_Out/Duplicate_Stats/PubMedDuplStats.txt", "r", encoding="utf8")
for line in PubMedReader:
	splitline = line.split("|")
	pubs.append(int(splitline[1]))
	dupls.append(int(splitline[2]))
print("Total PubMed Pubs: " + str(sum(pubs)))
print("Total PubMed Dupls: " + str(sum(dupls)))
print("Mean PubMed Pubs: " + str(statistics.mean(pubs)))
print("Mean PubMed Dupls: " + str(statistics.mean(dupls)))
print("Stddev PubMed Pubs: " + str(statistics.pstdev(pubs)))
print("Stddev PubMed Dupls: " + str(statistics.pstdev(dupls)))
PubMedReader.close()
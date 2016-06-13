import statistics

emailNums = []
emailDuplsReader = open("Data_Out/duplicateEmails.txt", "r", encoding="utf8")
for line in emailDuplsReader:
	splitLine = line.split("|")
	emailNums.append(len(splitLine))
emailDuplsReader.close()
for num in range(0,549):
	emailNums.append(1)
print("Mean emails per name: " + str(statistics.mean(emailNums)))
print("Stdev emails per name: " + str(statistics.pstdev(emailNums)))
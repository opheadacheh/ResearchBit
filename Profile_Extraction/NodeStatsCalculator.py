import statistics
import os

for file in os.listdir("Data_Out/IDs_Data"):
	if file.endswith(".txt"):
		nodeType = file[:-9]
		edgeNums = []
		nodeFileReader = open("Data_Out/IDs_Data/" + file, "r", encoding="utf8")
		for line in nodeFileReader:
			splitLine = line.split(",")
			edges = []
			edgeNum = -1
			for item in splitLine:
				if item not in edges:
					edges.append(item)
					edgeNum += 1
			edgeNums.append(edgeNum)
		nodeFileReader.close()
		print("Mean degree for " + nodeType + ": " + str(statistics.mean(edgeNums)))
		print("Stdev of degree for " + nodeType + ": " + str(statistics.pstdev(edgeNums)))
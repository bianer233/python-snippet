#cut -c1-4,38-45
# input indexStart indexStop

#simulate the shell cut function
from pprint import pprint
import yaml
results =  open('./test.txt', 'r')
# results = yaml.load(yaml_data)



str = results.read()

# input , how many start and stop point
input = raw_input()

#change input from string to list
# indexStop = int(raw_input())
input = input.split(" ")

#change string to list ,strip every line
strlist = str.splitlines()

#to record different group
temp = []
tempSum = []
#the index of 
i = 0
x = 0
j = 0

while i < len(input):
	temp.append([])
	indexStart = int(input[i])
	indexStop = int(input[i+1])

	for x in xrange(1,len(strlist)):
		strTemp = strlist[x][indexStart:indexStop]
		# print strTemp
		temp[j].append(strTemp)
		# print 'temp[',j,']',temp[j]
	i = i + 2
	print "i",i
	j = j + 1
	print "j",j

for item in xrange(0,len(temp[0])):
	tempSum.append("")

print len(tempSum)
print 'tempSum',tempSum
print temp


for index in xrange(0,len(temp)):
	print index ,'index'
	for item in xrange(0,len(tempSum)):

		if 0 == item:
			tempSum[item] = temp[int(index)][item]
		tempSum[item] = tempSum[item] + '   ' + temp[int(index)][item]

		# print 'temp[int',item,'][item]',temp[int(index)][item]
		# print 'tempSum[',item,']',tempSum[item]

	tempSum[item] = tempSum[item] + '\n'

pprint (tempSum)








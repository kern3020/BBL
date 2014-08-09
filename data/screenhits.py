#!/usr/bin/python
import sys
myCount = 0
myAccept = 0
filename = sys.argv[1]
cutoff = 1.0e-08
print("reading:{0}  cutoff:{1}".format(filename, cutoff))
# ugh need to add sequence lenghts 
for line in open(filename):
	(queryId, subjectId, percIdentity, alnLength, mismatchCount, gapOpenCount, queryStart, queryEnd, subjectStart, subjectEnd, eVal, bitScore) = line.split("\t")
	myCount += 1
	# do a gross cutoff in eVal first < 1e-08
	if float(eVal) < cutoff: 
		myAccept +=1
	"""
	subjectLen = int(subjectEnd) - int(subjectStart) + 1
	queryLen =  int(queryEnd) - int(queryStart) + 1
	nAlign = int(alnLength) - int(mismatchCount)- int(gapOpenCount)
	nAlign = int(alnLength)
	sCover = float(nAlign/subjectLen)
	qCover = float(nAlign/queryLen)
	#print("{0}	{1}").format(sCover,qCover)
	"""
print("read:{0} Accepted:{1}".format(myCount,myAccept)) 

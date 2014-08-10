#!/usr/bin/python
import sys
myCount = 0
myAccept = 0
filename = sys.argv[1]
cutoff = 1.0e-08
print("reading:{0}	cutoff:{1}".format(filename, cutoff))
# ugh need to add sequence lenghts 
fp = open(filename,'r')
fp.readline()
for line in fp:
	(queryId, subjectId, percIdentity, alnLength, mismatchCount, gapOpenCount, queryStart, queryEnd, subjectStart, subjectEnd, eVal, bitScore,queryLen,subjectLen) = line.split("\t")
	myCount += 1
	sAln = int(subjectEnd) - int(subjectStart) + 1
	qAln = int(queryEnd) - int(queryStart) + 1
	sCover = float( float(sAln)/ int(subjectLen) )
	qCover = float( float(qAln)/ int(queryLen) )
	# do a gross cutoff in eVal first < 1e-08
	if float(eVal) < cutoff:
	    if sCover > 0.8 or qCover > 0.8:
		    myAccept +=1
            print line,
	
print("#read:{0} Accepted:{1}".format(myCount,myAccept)) 

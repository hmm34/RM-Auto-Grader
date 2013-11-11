# Takes command arguments for the lab number to be automatically graded, and whether
# to grade just one specific student's or all students' assignment.

import sys
import os

# Usage: Grader.py <labNumber> <UANETID>
labNumber = sys.argv[1]
uanetid = sys.argv[2]

# Start by handling one student, then this can be expanded for all
sourceDir = uanetid + '/Eval/Labs/Lab' + labNumber


f = open(sourceDir + "/LabReport.txt","r")
t = f.read()
f = open(sourceDir + "/Autograde.txt","w")
grade = 20

codestart = t.find("------------ ")
header = t[0:codestart]

#detect compilation errors and output here

codestart = t.find(" ------------",codestart+1)+13
codeend = t.find("-------------",codestart+1)

#Check commit count, messages
footer = t[codeend:len(t)]
commits = footer.count("|") / 3
if commits < 5:
    grade -= 1
    f.write("Commit at least once for each part (-1)\n\n")

#text of submitted code
code = t[codestart:codeend]

#Check name in header comments
name = code.find("YOUR NAME")
if name >= 0:
    grade -= 1
    f.write("Name in header comment (-1)\n\n")
    
#detect max line length
linestart = 0
lineend = code.find("\n")
while lineend < len(code) and lineend >= 0:
	if lineend - linestart > 80:
		grade -= 1
		f.write("Keep lines to 80 characters (-1)\n\n")
		break
	linestart = lineend+1
	lineend = code.find("\n",linestart)

#Count "//" and "/*" and compare to original total for comment point
comments = code.count("//") + code.count("/*")
if comments < 5:
    grade -= 1
    f.write("Please ensure your code is commented (-1)\n\n")

f.write("Grade: " + str(grade))
f.close()
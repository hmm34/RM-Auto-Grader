
import sys
import os
import json

def gradeLab(labNumber,uanetid):
    # Read lab report and config file, create and open autograde file
    sourceDir = uanetid + '/Eval/Labs/Lab' + labNumber
    f = open(sourceDir + "/LabReport.txt","r")
    t = f.read()
    f = open("labConfig.json")
    config = json.loads(f.read())
    config = config[str(labNumber)]
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
    if commits < config["commits"]:
        grade -= 1
        f.write("Commit at least once for each part (-1)\n\n")

    #text of submitted code
    code = t[codestart:codeend]

    #Check name in header comments
    name = code.find("Your Name")
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
    if comments < config["comments"]:
        grade -= 1
        f.write("Please ensure your code is commented (-1)\n\n")

    if grade == 20:
        f.write("No errors detected by grading script")
    f.close()
   
# Takes command arguments for the lab number to be automatically graded, 
# and whether to grade just one specific student's or all students' assignment.   
# Usage: Grader.py <labNumber> <UANETID|"all">
labNumber = sys.argv[1]
uanetid = sys.argv[2]

if uanetid == "all":
    f = open("../admin/uanet.txt")
    text = f.read()
    lines = text.split("\n")
    for line in lines:
        if len(line) > 1:
            gradeLab(labNumber,line)
else:
    gradeLab(labNumber,uanetid)
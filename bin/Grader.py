# Takes command arguments for the lab number to be automatically graded, and whether
# to grade just one specific student's or all students' assignment.

import sys
import os

# Usage: Grader.py <labNumber> <UANETID>
labNumber = sys.argv[1]
uanetid = sys.argv[2]

# Start by handling one student, then this can be expanded for all
sourceDir = uanetid + '/Labs/Lab' + labNumber

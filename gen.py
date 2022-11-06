import sys
from data import hm

print('Please enter job description.')

s = ''
for line in sys.stdin:
    if 'e' == line.rstrip(): break
    s += line

ar = ["For the skills listed in the jd, I've aced the corresponding LinkedIn Skills Assessments."
      "You may verify this on my profile. \n\n"]

vector = s.split()

for word in vector:
    if word in hm:
        ar.append(word)
        ar.append(': Top ')
        ar.append(hm[word][0])
        ar.append('\n')
        ar.append('    ')
        ar.append(hm[word][1])
        ar.append('\n')

print(''.join(ar))


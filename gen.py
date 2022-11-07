import sys
from data import hm

print('Please enter job description.')

s = ''
for line in sys.stdin:
    if 'e' == line.rstrip(): break
    s += line

s = s.replace(':', '')
s = s.replace('!', '')
s = s.replace(',', '')
s = s.replace(')', '')
s = s.replace('(', '')
s = s.replace(';', '')

ar = ["For the skills listed in the job description, I've aced the corresponding LinkedIn Skills Assessments. "
      "You may verify this on my profile. \n\n"]

hs = set(s.split())

for word in hs:
    if word in hm:
        ar.append(word)
        ar.append(': Top ')
        ar.append(hm[word][0])
        ar.append('\n')
        ar.append('    ')
        ar.append(hm[word][1])
        ar.append('\n')
print(hs)
ar.append(" \nMy app Job Description Ninja created the above report. "
          "For you it's FOSS - Free and Open Source Software. "
          "Check it out on my Github https://github.com/zeusAlgo/Jd_Ninja")
print(''.join(ar))


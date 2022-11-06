import sys
from data import hm

print('Please enter job description.')
# jd = input()

jd_ar = []
for line in sys.stdin:
    if 'exit' == line.rstrip(): break
    jd_ar.extend(line.split())

print(jd_ar)

# import sys
# s = sys.stdin.readline(222)
# s = s.split()

# jd = s
# print(s)

# for line in jd:
#     print(line)
# jd = jd.replace('\n', '')
# jd = ''.join(jd.splitlines())
# jd = jd.split()
# jd = jd.strip().split()
# jd = jd.split('\n')

# print(jd)

ar = ["For the skills listed in the jd, "
      "I've aced the corresponding LinkedIn Skills Assessments."
      "You may verify this on my profile. \n\n"]

for word in jd_ar:
    if word in hm:
        ar.append(word)
        ar.append(': Top ')
        ar.append(hm[word][0])
        ar.append('\n')
        ar.append('    ')
        ar.append(hm[word][1])
        ar.append('\n')

print(''.join(ar))


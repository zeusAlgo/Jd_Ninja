from data import hm

print('Please enter job description.')
jd = input().split()

ar = ["For the skills listed in the jd, "
      "I've aced the corresponding LinkedIn Skills Assessments."
      "You may verify this on my profile. \n\n"]

for word in jd:
    if word in hm:
        ar.append(word)
        ar.append(': Top ')
        ar.append(hm[word][0])
        ar.append('\n')
        ar.append('    ')
        ar.append(hm[word][1])
        ar.append('\n')

print(''.join(ar))


from data import hm

print('Please enter job description.')
jd = input()

jd_vec = jd.split()
ar = ["Hello! For the job description you sent, I've aced many of "
      "the LinkedIn Skills Assessments for that skill and you may verify this on my profile. \n"]

for word in jd_vec:
    if word in hm:
        ar.append(word)
        ar.append(': Top ')
        ar.append(hm[word][0])

print(''.join(ar))


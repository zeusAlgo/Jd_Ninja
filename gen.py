import sys
from data import hm

print('Please enter job description.')

s = ''  # Add input to string
for line in sys.stdin:
    if 'e' == line.rstrip(): break  # Press 'e' to continue
    s += line

# Remove unwanted characters from string
to_remove_hs = {':', '!', ',', '(', ')', '{', '}', '[', ']', ';', '+', '-', '#', '$', '%', '&', '*', '@', '?'}
s = ''.join(c for c in s if c not in to_remove_hs)

ar = ["\nFor the skills listed in the job description, I've aced the corresponding LinkedIn Skills Assessments. "
      "You may verify this on my profile. \n\n"]

words_hs = set(s.split())  # Split the string by whitespaces and add result to hashset

for word in words_hs:  # If the word is a key in the hashmap, add its corresponding values to the array
    if word in hm:
        ar.append(word)
        ar.append(': Top ')
        ar.append(hm[word][0])
        ar.append('\n')
        ar.append('    ')
        ar.append(hm[word][1])
        ar.append('\n')

ar.append(" \nMy app Job Description Ninja created the above report. "
          "For you it's FOSS - Free and Open Source Software. "
          "Available here -> https://github.com/zeusAlgo/Jd_Ninja")
print(''.join(ar))

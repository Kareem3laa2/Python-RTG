import re
emails = []
fullNames = []
phoneNumber = []

file = open('Test.txt', 'r')
sentence = file.readline()

# E-mails Extraction

# emails_pattern = re.compile('[a-zA-Z0-9_.-]+@[a-zA-Z-]+\.[a-zA-Z]+')
# email_matches = emails_pattern.finditer(sentence)
# for match in email_matches:
# emails.append(match)

# FullNames Extraction

# fullName_pattern = re.compile('[A-Z]\w+\s[A-Z]\w+')
# fullName_matches = fullName_pattern.finditer(sentence)
# for match in fullName_matches:
#         fullNames.append(match)

# phoneNumber Extraction

# phoneNumber_pattern = re.compile('\d{10}')
# phoneNumber_matches = phoneNumber_pattern.finditer(sentence)
# for match in phoneNumber_matches:
#     phoneNumber.append(match)

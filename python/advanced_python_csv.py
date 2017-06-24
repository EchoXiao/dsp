import csv
import re

f = list(csv.reader(open('faculty.csv', 'r')))

email_list = []
for email in f:
    email_list.append(email[3].strip())

email_list = email_list[1:]
    
with open('email_list_output.csv', 'w') as f:
    writer = csv.writer(f, delimiter = ',',  lineterminator = '\r\n')
    for email in email_list:
        writer.writerow([email])
                         
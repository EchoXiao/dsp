# Regular Expression
import csv
f = list(csv.reader(open('faculty.csv', 'r')))

#1
#initialize all the degrees found in f
Phd = 0
ScD = 0
MPH = 0
MS = 0
BSEd = 0
JD = 0
MA = 0
MD = 0

for degs in f:
    if re.search('PhD|Ph.D.|Ph.D', degs[1].strip()) != None:
        Phd += 1
    if re.search('Sc.D.|ScD', degs[1].strip()) != None:
        ScD += 1
    if re.search('MPH', degs[1].strip()) != None:
        MPH += 1
    if re.search('M.S.|MS', degs[1].strip()) != None:
        MS += 1
    if re.search('B.S.Ed.', degs[1].strip()) != None:
        BSEd += 1
    if re.search('JD', degs[1].strip()) != None:
        JD += 1
    if re.search('MA', degs[1].strip()) != None:
        MA += 1
    if re.search('MD', degs[1].strip()) != None:
        MD += 1
print('Number of Phd: ' + str(Phd))
print('Number of ScD: ' + str(ScD))
print('Number of MPH: ' + str(MPH))
print('Number of MS: ' + str(MS))
print('Number of B.S.Ed: ' + str(BSEd))
print('Number of JD: ' + str(JD))
print('Number of MA: ' + str(MA))
print('Number of MD: ' + str(MD))

#2
#Looking at the dataset, there are total of 3 titles starting with their own key words
Prof = 0
Asso = 0
Assi = 0

for title in f:
    if re.search('^Prof', title[2].strip()) != None:
        Prof += 1
    if re.search('^Asso', title[2].strip()) != None:
        Asso += 1
    if re.search('^Assi', title[2].strip()) != None:
        Assi += 1
print('Number of Professor of Biostatistics: ' + str(Prof))
print('Number of Associate Professor of Biostatistics: ' + str(Asso))
print('Number of Assistant Professor of Biostatistics: ' + str(Assi))

#3
email_list = []
for email in f:
    email_list.append(email[3].strip())
email_list = email_list[1:]
print(email_list)

#4
#4
domain_list = []
for item in email_list:
    domain_list.append(item.split('@'))

unique_list = []
domain_list = domain_list[1:]
for domain in domain_list:
    unique_list.append(domain[1])
print(set(unique_list))
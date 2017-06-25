#Q6
name_list = [x[0] for x in f][1:]
info_list = [y[1:] for y in f][1:]

lname_list = []
fname_list = []
fullname_list = []
for name in name_list:
    lname_list.append(name.split(' ')[-1])
    fname_list.append(name.split(' ')[:-1])
    fullname_list.append(tuple(name.split(' ')[:-1] + [name.split(' ')[-1]]))

faculty_dict = {}
for lname, info in zip(lname_list, info_list):
    if lname not in faculty_dict:
        faculty_dict[lname] = []
        faculty_dict[lname].append(info)
    else:
        faculty_dict[lname].append(info)

#to get the first three key and value pairs of the dictionary
from itertools import islice

def take(n, iterable): return list(islice(iterable, n))

first3pairs = take(3, faculty_dict.items())
first3pairs


#Q7
modify_faculty_dict = {}
for fullname, info in zip(fullname_list, info_list):
    modify_faculty_dict[fullname] = info

mod_first3pairs = take(3, modify_faculty_dict.items())
mod_first3pairs

#Q8
sorted_name = sorted(modify_faculty_dict.keys(), key = lambda x: x[-1])

for k in range(3):
    print(sorted_name[k])
    print(modify_faculty_dict[sorted_name[k]])
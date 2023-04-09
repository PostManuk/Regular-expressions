import csv
import re
from collections import OrderedDict

with open('phonebook_raw.csv', 'rt', encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

title = contacts_list[0]
del contacts_list[0]

for contact in contacts_list:
    lastname = contact[0]
    firstname = contact[1]
    surname = contact[2]

    count = 0
    name = contact[0].split()
    for partname in lastname.split():
        contact[count] = partname
        count += 1
    if count < 3:
        for partname in firstname.split():
            contact[count] = partname
            count += 1
    if count < 3:
        for partname in surname.split():
            contact[count] = partname
            count += 1
    contact[5] = re.sub(r"(\+7|8) ?\(?(\d{3})\)?[ -]?(\d{3})-?(\d{2})-?(\d{2})(?:[ (]*(доб\.)? (\d{4})\)?)?",
                        r"+7(\2)\3-\4-\5 \6\7", contact[5]).strip()

contacts_list_ok = []

for i in range(len(contacts_list)):
    add_line = True
    for j in range(len(contacts_list_ok)):
        if contacts_list[i][0].strip() == contacts_list_ok[j][0].strip():
            contacts_list_ok[j] = (list(OrderedDict.fromkeys(contacts_list_ok[j] + contacts_list[i])))
            add_line = False
            print(list(OrderedDict.fromkeys(contacts_list_ok[j] + contacts_list[i])))
    if add_line:
        contacts_list_ok.append(contacts_list[i])

print(contacts_list_ok)

with open("phonebook_new.csv", "w", encoding='utf-8', newline='') as f:
    datawriter = csv.writer(f, delimiter=',')

    datawriter.writerow(title)
    datawriter.writerows(contacts_list_ok)
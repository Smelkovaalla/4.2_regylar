from pprint import pprint
import csv
import re

with open("phonebook_raw.csv", "r", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)


def number(pattern, subst, list):
    x = 0
    for i in list:
      y = 0
      for n in i:
        list[x][y] = re.sub(pattern, subst, n)
        y = y + 1
      x = x + 1
number(r"(\+7|8)\s*?\(?(\d{3})\)?\-?\s?(\d{3})\-?(\d{2})\-?(\d{2})", r"+7(\2)\3-\4-\5", contacts_list)
number(r"\(?\доб.\s+(\d+)\)?", r"доб.\1", contacts_list)

contacts_list2 = []
for contacts in contacts_list:
    contacts[:3] = [' '.join(contacts[:3])]
    contacts[0] = contacts[0].split(' ')
    del contacts[0][3:]
    contacts = contacts[0] + contacts[1:]
    contacts_list2.append(contacts)
contacts_list = contacts_list2

def mergeDict(dict1, dict2):
    for k, v in dict2.items():
        if dict1.get(k):
            if dict1[k] == v:
                dict1[k] = dict1[k]
            elif dict1[k] == '':
                dict1[k] = [v]
            elif v == '':
                dict1[k] = dict1[k]
        else:
            dict1[k] = v
    return dict1

# pprint(contacts_list)
new_list = []
new_list = [contacts_list[0]]
contact_document = []
contacts_dict = {}

for i in contacts_list[0]:
    contacts_dict[i] = ''
del contacts_list[0]
contacts_dict_new = {}
x = 0
for contact in contacts_list:
    x = 0
    for name in contacts_dict:
        contacts_dict_new[name] = contact[x]
        x = x + 1
    contact_document.append(contacts_dict_new)
    contacts_dict_new = {}
# pprint(contact_document)
# pprint(new_list)


directories_dict = {}
x = 0
result = []
for i in contact_document:
    for res in directories_dict.values():
        result.extend(res)
    if i['lastname'] and i['firstname'] not in result:
        directories_dict[x] = [i['lastname'], i['firstname']]
        x = x + 1
        new_list.append(list(i.values()))
    else:
        for k, v in directories_dict.items():
            if v == [i['lastname'], i['firstname']]:
                m = k
        print(m)
        z = mergeDict(contact_document[m], i)
        new_list.append(list(z.values()))
        с = m + 1
        del new_list[с]
        directories_dict[x] = [i['lastname'], i['firstname']]
        x = x + 1


# pprint(directories_dict)
# pprint(new_list)


with open('phonebook_new.csv', 'w', encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(new_list)

print('Текст записан в файл phonebook_new.csv')
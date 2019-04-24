fname = input('Enter File: ')
print(' ')
if len(fname) < 1:
    fname = 'studyprogramme.txt'

try:
    hand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()
fi = open('cleanedtext.txt', 'w')
# di = dict()
# for line in hand:
#     line = line.strip()
#     # if not line.startswith('1. ID'):
#     #     continue
#     wds = line.split()
#     # print(wds)
#     for w in wds:

#         # if w in di:
#         #     di[w] = di[w] + 1
#         # else:
#         #     di[w] = 1

#         di[w] = di.get(w, 0) + 1

# # Long way of getting the most common word
# # largest = -1
# # word = None

# # for k, v in di.items():
# #     if v > largest:
# #         largest = v
# #         word = k

# # print(word, largest)

# # x = sorted(di.items())

# tmp = list()
# for k, v in di.items():
#     newtuple = (v, k)
#     tmp.append(newtuple)

# tmp = sorted(tmp, reverse=False)

# for v, k in tmp:
#     print(k, v)

maininfo = list()
descinfo = list()


skip = False
# nomb = False
# desc = False
# countident = 0
# for line in hand:
#     line = line.strip()

#     if line.startswith('SZR'):
#         skip = True
#     if 'Osorio' in line or 'Cesar' in line:
#         skip = False
#         continue
#     if skip:
#         continue

#     if 'IDENT' in line:
#         nomb = True
#         countident += 1
#     if 'DESC' in line:
#         nomb = False

#     if nomb and line != "":
#         maininfo.append(line)

#     if '2. DESC' in line:
#         desc = True
#         countident += 1
#     if line.lower().startswith('3.'):
#         desc = False

#     if desc and line != "":
#         descinfo.append(line)


def getName(description):
    words = description.split()
    ind = 0
    for word in words:
        if word.isupper():
            ind = words.index(word)
            break
    name = words[ind:]
    return " ".join(name)


# def getDescription():
#     pass
for line in hand:
    maininfo.append(line.strip())

for index, line in enumerate(maininfo):
    line = line.strip()
    if line.startswith('SZR'):
        skip = True
    if 'Osorio' in line or 'Cesar' in line:
        skip = False
        continue
    if skip:
        continue
    if 'NOMBRE' in line and not 'PROFESOR' in line:
        nombremateria = ''
        if maininfo[index + 5].startswith('No'):
            if len(maininfo[index + 7]) < 31:
                nombremateria = (maininfo[index + 9])

            else:
                if 'NOMBRE' in maininfo[index + 7]:
                    nombremateria = (getName(maininfo[index + 14]))

                elif maininfo[index + 7].startswith('!'):
                    nombremateria = (getName(maininfo[index + 8]))

                else:
                    nombremateria = (getName(maininfo[index + 7]))

        elif len(maininfo[index + 5]) < 9:
            if 'REQU' in maininfo[index + 1]:
                if len(maininfo[index + 4]) < 5:
                    nombremateria = (getName(maininfo[index + 3]))

                else:
                    nombremateria = (getName(maininfo[index + 4]))

            else:
                nombremateria = (getName(maininfo[index + 1]))
        else:
            nombremateria = (getName(maininfo[index + 5]))

        line = nombremateria

    if line != "":
        fi.write(line)
        fi.write('\n')


# for item in maininfo:
#     print(item)
# countnombre = 0
# for index, line in enumerate(maininfo):

#     if 'NOMBRE' in line and not 'PROFESOR' in line:
#         nombremateria = ''
#         if maininfo[index + 5].startswith('No'):
#             if len(maininfo[index + 7]) < 31:
#                 nombremateria =(maininfo[index + 9])

#             else:
#                 if 'NOMBRE' in maininfo[index + 7]:
#                     nombremateria =(getName(maininfo[index + 14]))

#                 elif maininfo[index + 7].startswith('!'):
#                     nombremateria =(getName(maininfo[index + 8]))

#                 else:
#                     nombremateria =(getName(maininfo[index + 7]))

#         elif len(maininfo[index + 5]) < 9:
#             if 'REQU' in maininfo[index + 1]:
#                 if len(maininfo[index + 4]) < 5:
#                     nombremateria =(getName(maininfo[index + 3]))

#                 else:
#                     nombremateria =(getName(maininfo[index + 4]))

#             else:
#                 nombremateria =(getName(maininfo[index + 1]))
#         else:
#             nombremateria =(getName(maininfo[index + 5]))

#         print(nombremateria)
#         print('')
#         # print(descinfo[countnombre])
#         countnombre += 1
#         # print('')

# for line in descinfo:
#     print(line)
#     print('')
# print('Numero de IDENT: ', countident)
# print('Numero de NOMBRE: ', countnombre)

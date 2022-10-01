# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = 'Мы неабв любим изучатьабв Питон'
lst = text.split()
print(lst)
substring = 'абв'
lst2 = []
for i in range(len(lst)):
    if substring in lst[i]:
        lst2.append(lst[i])
print(lst2)
for i in lst2:
    lst.remove(i)
print(lst)


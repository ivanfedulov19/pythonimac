# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных
# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open ('task_5_4_1.txt','r') as file1:
    example = file1.read()

lst = []
counter = 1
counter_2 = 1
for i in range(1,len(example)):
    if example[i] == example[i-1]:
        counter += 1
    else:
        lst.append(example[i-1])
        lst.append(counter)
        counter = 1
lst2 = []
for j in range(len(example) - 1, 1, -1):
    if example[j-1] == example[j]:
        counter_2 += 1
    elif example[j-1] != example[j]:
        lst2.append(example[j])
        lst2.append(counter_2)
        break

lst3 = lst + lst2
for i in range(len(lst3)):
    lst3[i] = str(lst3[i])
compression = ''.join(lst3)

with open ('task_5_4_2.txt','w') as file2:
    file2.write(compression)

lst4 = []
for i in range(len(compression)):
    lst4.append(compression[i])

lst5 = []
recovery = ''
for i in range(1,len(lst4),2):
    recovery += int(lst4[i]) * lst4[i-1]

with open ('task_5_4_3.txt','w') as file3:
    file3.write(recovery)




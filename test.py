'''import random
from tkinter import *
root = Tk()
lb = Label(root)
lb2 = Label(root)
r_number = random.sample(range(1, 49), 6)
r_number.sort()
print(r_number)
lb.config(text=r_number[0])
lb2.config(text=r_number[1])
#
# for x in r_number:
#     print(x)
#     lb.config(text=x)
lb.pack()
lb2.pack()
# from tkinter import *  # from tkinter import *
#
# lst = ['a', 'b', 'c', 'd']
#
# root = Tk()
# t = Text(root)
# for x in lst:
#     t.insert(END, x + '\n')
# t.pack()
root.mainloop()
'''


'''def Diff(li1, li2):
    return (list(list(set(li1) - set(li2)) + list(set(li2) - set(li1))))
# Driver Code
li1 = [13, 6, 19, 12, 25, 18]
li2 = [13, 19, 20, 25, 34, 40]
print(Diff(li1, li2))'''

'''list1 = [1,2,3,4,5,6]
list2 = [3, 5, 7, 9]
res = list(set(list1).intersection(list2))
print(len(res))'''


'''def common_elements(list1, list2):
    result = []
    for element in list1:
        if element in list2:
            result.append(element)
    return result
print(common_elements(list1,list2))'''

from datetime import date


def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    return age


# Driver code
print(calculateAge(date(2002, 11, 26)), "years")

#1 Напишите программу, которая по данному числу n от 1 до 9 выводит на экран n домов. 
#Между двумя соседними домами также имеется пустой (из пробелов) столбец. 
#Разрешается вывести пустой столбец после последнего дома. Для упрощения рисования скопируйте дом из примера в среду разработки.


while True:
    try:
        dom=['  ~~~~~   ',
            ' /_____\  ',
            ' | []  |  ',
            '  -----   ']
        n=int(input("Majade arv(1-9): "))
        if n>0 and n<10:
            for k in dom:
                print(k * n)
        elif n>=10:
            print("Liiga suur!")
        elif n<=0:
            print("Liiga väike!")
        break
    except:
        print("Vale Andmetüüp")



#2 Известны оценки по физике каждого ученика двух классов. Определить среднюю оценку в каждом классе. Количество учащихся в каждом классе одинаковое.



print("Klassides on 10 õpilased")
õpilased=10
hinnad=[3, 4, 5, 2, 4, 5, 5, 4, 3, 5]
hinnad2=[4, 5, 4, 3, 4, 2, 1, 3, 5, 5]
klass=0
klass2=0
for i in range(õpilased):
    klass+=hinnad[i]
    klass2+=hinnad2[i]
keskmine_hind=klass/õpilased
keskmine_hind2=klass2/õpilased
print("Esimesel klassis keskmine hind: ",keskmine_hind)
print("Teisel klassis keskmine hind: ",keskmine_hind2)


#3 Известны средние оценки каждого из  учеников класса. Определить минимальную и максимальную оценки. 
#(Оценки и количество учеников получаем случайным образом). 
#Использовать только цикл и сравнительные операторы. max() и min() не использвать.


from math import*
from random import*


num_students = 10 
min_grade = 100 
max_grade = 0 
for i in range(num_students):
    grade = randint(0, 100) 
    if grade < min_grade:
        min_grade = grade
    if grade > max_grade:
        max_grade = grade

print("Minimum grade:", min_grade)
print("Maximum grade:", max_grade)




#4


s2=0
n2=0
for x in range(1,13):
    S=randint(5,10)
    n=randint(20000,50000)
    print(f"Maakond {x}:\nElanikud: {n}\nVäljak: {S} km2")
    print()
    s2=s2+S
    n2=n2+n
p=n2//s2
print(f"Piirkondlik rahvastikutihedus: {p}")




##5
while True:
    try:
        min=int(input("Sisesta minimaalne väärtus: "))
        max=int(input("Sisesta maksimaalne väärtus: "))
        s=int(input("Sisesta samm: "))
        print("y=-0.5x+x")
        print()
        for x in range(min, max, s):
            y=-0.5*x+x
            print(f"x={x}\ny={y}")
            print()
            break
    except:
        print("Vale Andmetüüp")

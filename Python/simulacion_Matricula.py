# For moments this file is in development, follow i try to give solution to this excersice
# This File is about  a little Tuition's System, a simulation, practice of python
# The problem is because the variables do not work
from os import system

print("Tuition's System")
print("1 - Economy")
print("2 - Administration")
print("3 - Accounting")
print("4 - Computer Engineering")
N = int(input("Insert the students to enroll: "))

system("cls")

for i in range(N):
   career = int(input("Enroll the career chosen: "))
   semester = int(input("Choose a semester to enroll: "))

   if career == 1:
       economy = 0
       economy = economy + 1
   elif career == 2:
       administration = 0
       administration = administration + 1
   elif career == 3:
       accounting = 0
       accounting = accounting + 1
   elif career == 4:
       compu = 0
       compu = compu + 1

system("cls")
print(f"Total of Economy: {economy}")
print(f"Total of Administration: {administration}")
print(f"Total of Accounting: {accounting}")
print(f"Total of Computer Engineering: {compu}")
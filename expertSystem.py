#expertSystem.py

import production_rules as pr
import output as op

print("\t\tProgramming Language Recommendation Tool")
print("\nSo you want to learn programming. But don't know") 
print("what is the first language that you should learn?")
print("Well, there are a lot of programming languages out")
print("and choosing one is not easy.")
print("But don't worry, we got you covered!")
print("\nYou can use this expert system to recommend the first")
print("programming language that you should learn, based on your")
print("preferences, your reason to learn programming, etc.")

start = input("Start?\nYes/No: ")
if (start == 'Yes' or start == 'y' or start == 'yes'):
    pr.start()
else:
    "Quitting. Bye"
    exit()


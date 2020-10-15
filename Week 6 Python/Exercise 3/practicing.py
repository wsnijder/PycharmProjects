horsemen = ["war", "famine", "pestilence", "death"]
for i in range(len(horsemen)):
    print(horsemen[i])

for words in horsemen:
    print(words)

students = [("John", ["CompSci", "Physics"]),("Vusi", ["Maths", "CompSci", "Stats"]),("Jess", ["CompSci", "Accounting",
"Economics", "Management"]),("Sarah", ["InfSys", "Accounting", "Economics", "CommLaw"]),("Zuki", ["Sociology",
"Economics", "Law", "Stats", "Music"])]

counter = 0
for name, subjects in students:
    if "Economics" in subjects:
        counter += 1

print("The number of students taking Economics is", counter)

deel1 = ["alpha", "beta", "gamma"]
deel2 = ["is niks"]
samen = deel1 + deel2
print(samen)

friends = ["Ren", "Den", "maatje"]
for friend in friends:
    print(friend)


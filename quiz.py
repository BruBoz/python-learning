score = 0
answer = input("Which planet is the eighth planet from the Sun?")
if answer.lower() == "Neptune":
    print("Correct! ✅")
    score += 1
else: 
    print("Incorrect! ❌ The correct answer is Neptune.")
answer = input("Which planet in the Solar System is the biggest?")
if answer.lower() == "Jupiter":
    print("Correct! ✅")
    score += 1
else:
    print ("Incorrect! ❌ The correct answer is Jupiter")
answer = input("Which planet has the second biggest amount of moons in the Solar System?")
if answer.lower() == "Saturn":
    print("Correct! ✅")
    score += 1
else:
    print ("Incorrect! ❌ The correct answer is Saturn")
print(f"\nTwój wynik: {score}/3")
    
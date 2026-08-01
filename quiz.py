score = 0
answer = input("Which planet is the eighth planet from the Sun?")
if answer.lower() == " neptune":
    print("Correct! ✅")
    score += 1
else: 
    print("Incorrect! ❌ The correct answer is Neptune.")
answer = input("Which planet has the most volcanoes?")
if answer.lower() == " venus":
    print("Correct! ✅")
    score += 1
else:
    print ("Incorrect! ❌ The correct answer is Jupiter")
answer = input("Which planet has the second biggest amount of moons in the Solar System?")
if answer.lower() == " jupiter":
    print("Correct! ✅")
    score += 1
else:
    print ("Incorrect! ❌ The correct answer is Saturn")
print(f"\nTwój wynik: {score}/3")
    
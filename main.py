#Mood indicator program 😄

score = int(input("Enter your mood score (1-5): "))

if score == 5:
    print("😁 You're feeling AWESOME! Keep shining ✨")
elif score == 4:
    print("😊 You seem happy today!")
elif score == 3:
    print("😐 You’re neutral — not bad, not great!")
elif score == 2:
    print("☹️ Seems like a dull day, Dnyaneshwar. Cheer up 💪")
elif score == 1:
    print("😭 Rough day, huh? Take a break and relax 🧘‍♂️")
else:
    print("⚠️ Please enter a number between 1 and 5.")
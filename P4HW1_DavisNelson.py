#Nelson Davis
#P4HW1
#October 21

scores = []

num_scores = int(input("How many scores do you want to enter? "))

for i in range(num_scores):
    score = float(input(f"Enter score #{i + 1}: "))

    while score < 0 or score > 100:
        print("\nINVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input("Enter score again: "))

    scores.append(score)

lowest_score = min(scores)
scores.remove(lowest_score)

average = sum(scores) / len(scores)

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

print("\n------------Results------------")
print(f"Lowest Score  : {lowest_score}")
print(f"Modified List : {scores}")
print(f"Scores Average: {average:.2f}")
print(f"Grade         : {grade}")
print("--------------------------------")
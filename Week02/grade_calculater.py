scores = []

while True:
    name = input("Enter student name (or q to quit): ").strip()
    
    if name.lower() == 'q':
        break
    
    score = float(input("Enter score: "))

    if score < 0 or score > 100:
        print("Invalid score. Please enter a number between 0 and 100.")
        continue

    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    formatted_score = int(score) if score.is_integer() else score
    print(f"{name}: {formatted_score} -> {grade}")
    
    scores.append(score)
  
if len(scores) == 0:
    print("No students entered.")
else:
    total_students = len(scores)
    avg_score = sum(scores) / total_students
    print(f"Total students: {total_students}")
    print(f"Average score: {avg_score:.2f}")

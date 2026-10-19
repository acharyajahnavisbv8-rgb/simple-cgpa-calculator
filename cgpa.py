print("--- Simple CGPA Calculator ---")

try:
    num_subjects = int(input("Enter number of subjects: "))
    total_grade_points = 0.0

    for i in range(num_subjects):
        grade = float(input(f"Enter Grade Point for subject {i+1} (e.g., 8.0, 9.5): "))
        total_grade_points += grade

    cgpa = total_grade_points / num_subjects
    print("-" * 30)
    print(f"Your Final CGPA is: {cgpa:.2f}")

except ValueError:
    print("Error: Please enter numbers only!")

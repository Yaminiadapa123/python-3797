student_id = 201
student_name = "yamini"
student_age = 21
maths_score = 98
science_score = 87
english_score = 95
telugu_score = 94
social_score = 92
hindi_score = 56

# Total and Average
total_score = maths_score + science_score + english_score + telugu_score + social_score + hindi_score
average_score = total_score / 6

# Pass Check
student_passed = average_score >= 75

# Display Output
print("Student ID:", student_id)
print("Name:", student_name)
print("Age:", student_age)
print("Total Score:", total_score)
print("Average Score:", average_score)
print("Passed:", student_passed)

students = [
    {"name": "Ava", "grade_level": 12, "activities": ["coding", "robotics", "math"]},
    {"name": "Hayden", "grade_level": 11, "activities": ["music", "robotics"]},
    {"name": "Lincoln", "grade_level": 11, "activities": ["chess"]},
    {"name": "Grant", "grade_level": 11, "activities": ["robotics", "drama", "sports", "drawing"]}
]
# Printing all student names and their grade levels
print("1. Student names:")
for s in students:
    print(s["name"])

print("\n2. Grade 12 students:")
for s in students:
    if s["grade_level"] == 12:
        print(s["name"])

# The number of activites the school offers
unique_activities = set()
for s in students:
    for activity in s["activities"]:
        unique_activities.add(activity)
print("\n3. Unique activities offered:", unique_activities)

# Finding the student with the longest activities list
most_active = students[0]
for s in students:
    if len(s["activities"]) > len(most_active["activities"]):
        most_active = s
print("\n4. Student with the most activities:", most_active["name"])

# Who is in robotics?
robotics_count = 0
for s in students:
    if "robotics" in s["activities"]:
        robotics_count += 1
print("5. Number of students in robotics:", robotics_count)
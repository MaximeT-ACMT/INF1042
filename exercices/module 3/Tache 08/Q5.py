slices = int(input("Number of pizza slices: "))
students = int(input("Number of students: "))

per_student = slices // students
leftovers = slices % students

print("Each student receives:", per_student, "slices.")
print("Number of slices that cannot be distributed equally:", leftovers)
from new_student import Student

# Test case 1: Normal initialization
student = Student(name="Edward", surname="agle")
print(student)

# Test case 2: Attempting to initialize login and id (should raise error)
try:
    student = Student(name="Edward", surname="agle", id="toto")
    print(student)
except TypeError as e:
    print(e) 
student = {"name": "Sai", "age": 22, "course": "QA Automation"}

for key in student:
    print(key, ":", student[key])

for key, value in student.items():
    print(f"{key} --> {value}")
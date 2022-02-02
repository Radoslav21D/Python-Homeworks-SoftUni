
command = input()
total_courses = {}

while not command == "end":
    course = command.split(" : ")
    course_name = course[0]
    course_student = course[1]
    if course_name not in total_courses:
        total_courses[course_name] = []
    total_courses[course_name].append(course_student)
    command = input()
# sorting
sorted_total = sorted(total_courses.items(), key=lambda kvp: -len(kvp[1]))

for key, value in sorted_total:
    print(f"{key}: {len(value)}")
    value = sorted(value)
    for val in value:
        print(f"-- {val}")

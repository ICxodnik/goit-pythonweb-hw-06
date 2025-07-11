import asyncio
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import my_select

async def main():
    # 1. Top 5 students by average grade
    print("1. Top 5 students by average grade:")
    result = await my_select.select_1()
    print(result)

    # 2. Best student in a specific subject (subject_id=1)
    print("\n2. Best student in subject 1:")
    result = await my_select.select_2(subject_id=1)
    print(result)

    # 3. Average grade in each group for a specific subject (subject_id=1)
    print("\n3. Average grade in each group for subject 1:")
    result = await my_select.select_3(subject_id=1)
    print(result)

    # 4. Average grade across all grades
    print("\n4. Average grade across all grades:")
    result = await my_select.select_4()
    print(result)

    # 5. Courses taught by a specific teacher (teacher_id=1)
    print("\n5. Courses taught by teacher 1:")
    result = await my_select.select_5(teacher_id=1)
    print(result)

    # 6. Students in a specific group (group_id=1)
    print("\n6. Students in group 1:")
    result = await my_select.select_6(group_id=1)
    print(result)

    # 7. Grades of students in a group for a subject (group_id=1, subject_id=1)
    print("\n7. Grades of students in group 1 for subject 1:")
    result = await my_select.select_7(group_id=1, subject_id=1)
    print(result)

    # 8. Average grade given by a teacher (teacher_id=1)
    print("\n8. Average grade given by teacher 1:")
    result = await my_select.select_8(teacher_id=1)
    print(result)

    # 9. Courses attended by a student (student_id=1)
    print("\n9. Courses attended by student 1:")
    result = await my_select.select_9(student_id=1)
    print(result)

    # 10. Courses taught to a student by a teacher (student_id=1, teacher_id=1)
    print("\n10. Courses taught to student 1 by teacher 1:")
    result = await my_select.select_10(student_id=1, teacher_id=1)
    print(result)

    # 11. Average grade given by a teacher to a student (teacher_id=1, student_id=1)
    print("\n11. Average grade given by teacher 1 to student 1:")
    result = await my_select.select_11(teacher_id=1, student_id=1)
    print(result)

    # 12. Grades of students in a group for a subject at the last lesson (group_id=1, subject_id=1)
    print("\n12. Grades of students in group 1 for subject 1 at the last lesson:")
    result = await my_select.select_12(group_id=1, subject_id=1)
    print(result)

if __name__ == "__main__":
    asyncio.run(main()) 
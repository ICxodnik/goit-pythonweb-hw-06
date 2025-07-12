import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import repository.my_select as my_select
import asyncio

# Helper function for pretty printing
def print_section(title):
    print("\n" + "=" * 60)
    print(f"{title}")
    print("=" * 60)

def pretty_print_result(result):
    if isinstance(result, list):
        if not result:
            print("No results.")
        for row in result:
            if isinstance(row, tuple):
                print("  - " + ", ".join(str(item) for item in row))
            else:
                print(f"  - {row}")
    elif isinstance(result, tuple):
        print("  - " + ", ".join(str(item) for item in result))
    elif result is None:
        print("No result.")
    else:
        print(f"  {result}")

async def main():
    # 1. Top 5 students by average grade
    print_section("1. Top 5 students by average grade:")
    result = await my_select.select_1()
    pretty_print_result(result)

    # 2. Best student in a specific subject (subject_id=1)
    print_section("2. Best student in subject 1:")
    result = await my_select.select_2(subject_id=1)
    pretty_print_result(result)

    # 3. Average grade in each group for a specific subject (subject_id=1)
    print_section("3. Average grade in each group for subject 1:")
    result = await my_select.select_3(subject_id=1)
    pretty_print_result(result)

    # 4. Average grade across all grades
    print_section("4. Average grade across all grades:")
    result = await my_select.select_4()
    pretty_print_result(result)

    # 5. Courses taught by a specific teacher (teacher_id=1)
    print_section("5. Courses taught by teacher 1:")
    result = await my_select.select_5(teacher_id=1)
    pretty_print_result(result)

    # 6. Students in a specific group (group_id=1)
    print_section("6. Students in group 1:")
    result = await my_select.select_6(group_id=1)
    pretty_print_result(result)

    # 7. Grades of students in a group for a subject (group_id=1, subject_id=1)
    print_section("7. Grades of students in group 1 for subject 1:")
    result = await my_select.select_7(group_id=1, subject_id=1)
    pretty_print_result(result)

    # 8. Average grade given by a teacher (teacher_id=1)
    print_section("8. Average grade given by teacher 1:")
    result = await my_select.select_8(teacher_id=1)
    pretty_print_result(result)

    # 9. Courses attended by a student (student_id=1)
    print_section("9. Courses attended by student 1:")
    result = await my_select.select_9(student_id=1)
    pretty_print_result(result)

    # 10. Courses taught to a student by a teacher (student_id=1, teacher_id=1)
    print_section("10. Courses taught to student 1 by teacher 1:")
    result = await my_select.select_10(student_id=1, teacher_id=1)
    pretty_print_result(result)

    # 11. Average grade given by a teacher to a student (teacher_id=1, student_id=1)
    print_section("11. Average grade given by teacher 1 to student 1:")
    result = await my_select.select_11(teacher_id=1, student_id=1)
    pretty_print_result(result)

    # 12. Grades of students in a group for a subject at the last lesson (group_id=1, subject_id=1)
    print_section("12. Grades of students in group 1 for subject 1 at the last lesson:")
    result = await my_select.select_12(group_id=1, subject_id=1)
    pretty_print_result(result)

if __name__ == "__main__":
    asyncio.run(main()) 
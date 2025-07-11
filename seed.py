import asyncio
from random import randint, choice, sample
from faker import Faker
from database.models import Group, Teacher, Subject, Student, Grade
from database.db import sessionmanager
from datetime import datetime, timedelta

fake = Faker()

NUM_GROUPS = 3
NUM_TEACHERS = randint(3, 5)
NUM_SUBJECTS = randint(5, 8)
NUM_STUDENTS = randint(30, 50)
MAX_GRADES_PER_STUDENT = 20

async def seed():
    async with sessionmanager.session() as session:
        # 1. Groups
        groups = [Group(name=fake.unique.bothify(text='Group-??')) for _ in range(NUM_GROUPS)]
        session.add_all(groups)
        await session.flush()  # Get ids

        # 2. Teachers
        teachers = [Teacher(name=fake.name()) for _ in range(NUM_TEACHERS)]
        session.add_all(teachers)
        await session.flush()

        # 3. Subjects (assign a random teacher to each subject)
        subjects = [Subject(name=fake.unique.word().capitalize(), teacher_id=choice(teachers).id) for _ in range(NUM_SUBJECTS)]
        session.add_all(subjects)
        await session.flush()

        # 4. Students (assign a group to each student)
        students = [Student(name=fake.name(), group_id=choice(groups).id) for _ in range(NUM_STUDENTS)]
        session.add_all(students)
        await session.flush()

        # 5. Grades (each student gets grades for different subjects)
        grades = []
        for student in students:
            subjects_for_student = sample(subjects, k=randint(1, len(subjects)))
            for subject in subjects_for_student[:MAX_GRADES_PER_STUDENT]:
                for _ in range(randint(1, 2)):
                    grade = Grade(
                        student_id=student.id,
                        subject_id=subject.id,
                        grade=randint(60, 100),
                        date_received=fake.date_time_between(start_date='-1y', end_date='now')
                    )
                    grades.append(grade)
        session.add_all(grades)
        await session.commit()
    print("Seeding complete!")

if __name__ == "__main__":
    asyncio.run(seed()) 
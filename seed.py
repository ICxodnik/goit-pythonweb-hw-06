import asyncio
from random import randint, choice, sample
from faker import Faker
from database.models import Group, Teacher, Subject, Student, Grade
from database.db import sessionmanager
from datetime import datetime, timedelta
from sqlalchemy import select, func, exists

fake = Faker()

NUM_GROUPS = 3
NUM_TEACHERS = randint(3, 5)
NUM_SUBJECTS = randint(5, 8)
NUM_STUDENTS = randint(30, 50)
MAX_GRADES_PER_STUDENT = 20

async def is_database_empty():
    """Checks if the database is empty"""
    async with sessionmanager.session() as session:
        # Check for existence of records in any table
        query = select(
            exists().where(Group.id) |
            exists().where(Teacher.id) |
            exists().where(Subject.id) |
            exists().where(Student.id) |
            exists().where(Grade.id)
        )
        result = await session.execute(query)
        return not result.scalar()

async def seed():
    """Fills the database with test data if it's empty"""
    async with sessionmanager.session() as session:
        # Check if database is empty
        if not await is_database_empty():
            print("Database already contains data. Seeding skipped.")
            return
        
        print("Database is empty. Starting seeding...")
        
        # 1. Groups
        groups = [Group(name=fake.unique.bothify(text='Group-??')) for _ in range(NUM_GROUPS)]
        session.add_all(groups)
        await session.flush()  # Get ids
        print(f"Created {NUM_GROUPS} groups")

        # 2. Teachers
        teachers = [Teacher(name=fake.name()) for _ in range(NUM_TEACHERS)]
        session.add_all(teachers)
        await session.flush()
        print(f"Created {NUM_TEACHERS} teachers")

        # 3. Subjects (assign a random teacher to each subject)
        subjects = [Subject(name=fake.unique.word().capitalize(), teacher_id=choice(teachers).id) for _ in range(NUM_SUBJECTS)]
        session.add_all(subjects)
        await session.flush()
        print(f"Created {NUM_SUBJECTS} subjects")

        # 4. Students (assign a group to each student)
        students = []
        for _ in range(NUM_STUDENTS):
            student = Student(
                name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.unique.email(),
                phone=fake.numerify(text='###-###-####'),
                birthday=fake.date_of_birth(minimum_age=16, maximum_age=25),
                group_id=choice(groups).id
            )
            students.append(student)
        session.add_all(students)
        await session.flush()
        print(f"Created {NUM_STUDENTS} students")

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
        print(f"Created {len(grades)} grades")
        print("Seeding completed successfully!")

if __name__ == "__main__":
    asyncio.run(seed()) 
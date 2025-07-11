import asyncio
from sqlalchemy import select, func, desc
from sqlalchemy.orm import selectinload
from database.models import Student, Group, Teacher, Subject, Grade
from database.db import sessionmanager

# 1. Top 5 students with the highest average grade across all subjects
async def select_1():
    """Return 5 students with the highest average grade across all subjects."""
    async with sessionmanager.session() as session:
        result = await session.execute(
            select(Student.name, func.avg(Grade.grade).label('avg_grade'))
            .join(Grade, Student.id == Grade.student_id)
            .group_by(Student.id)
            .order_by(desc('avg_grade'))
            .limit(5)
        )
        return result.all()

# 2. Student with the highest average grade in a specific subject
async def select_2(subject_id: int):
    """Return the student with the highest average grade in a specific subject."""
    async with sessionmanager.session() as session:
        result = await session.execute(
            select(Student.name, func.avg(Grade.grade).label('avg_grade'))
            .join(Grade, Student.id == Grade.student_id)
            .where(Grade.subject_id == subject_id)
            .group_by(Student.id)
            .order_by(desc('avg_grade'))
            .limit(1)
        )
        return result.first()

# 3. Average grade in each group for a specific subject
async def select_3(subject_id: int):
    """Return the average grade in each group for a specific subject."""
    async with sessionmanager.session() as session:
        result = await session.execute(
            select(Group.name, func.avg(Grade.grade).label('avg_grade'))
            .join(Student, Student.group_id == Group.id)
            .join(Grade, Grade.student_id == Student.id)
            .where(Grade.subject_id == subject_id)
            .group_by(Group.id)
        )
        return result.all()

# 4. Average grade across all grades (entire stream)
async def select_4():
    """Return the average grade across all grades (entire stream)."""
    async with sessionmanager.session() as session:
        result = await session.execute(
            select(func.avg(Grade.grade))
        )
        return result.scalar()

# 5. List of courses taught by a specific teacher
async def select_5(teacher_id: int):
    """Return the list of courses taught by a specific teacher."""
    async with sessionmanager.session() as session:
        result = await session.execute(
            select(Subject.name)
            .where(Subject.teacher_id == teacher_id)
        )
        return [row[0] for row in result.all()]

# 6. List of students in a specific group
async def select_6(group_id: int):
    """Return the list of students in a specific group."""
    async with sessionmanager.session() as session:
        result = await session.execute(
            select(Student.name)
            .where(Student.group_id == group_id)
        )
        return [row[0] for row in result.all()]

# 7. Grades of students in a specific group for a specific subject
async def select_7(group_id: int, subject_id: int):
    """Return the grades of students in a specific group for a specific subject."""
    async with sessionmanager.session() as session:
        result = await session.execute(
            select(Student.name, Grade.grade)
            .join(Grade, Student.id == Grade.student_id)
            .where(Student.group_id == group_id, Grade.subject_id == subject_id)
        )
        return result.all()

# 8. Average grade given by a specific teacher across their subjects
async def select_8(teacher_id: int):
    """Return the average grade given by a specific teacher across their subjects."""
    async with sessionmanager.session() as session:
        result = await session.execute(
            select(func.avg(Grade.grade))
            .join(Subject, Subject.id == Grade.subject_id)
            .where(Subject.teacher_id == teacher_id)
        )
        return result.scalar()

# 9. List of courses attended by a specific student
async def select_9(student_id: int):
    """Return the list of courses attended by a specific student."""
    async with sessionmanager.session() as session:
        result = await session.execute(
            select(Subject.name)
            .join(Grade, Subject.id == Grade.subject_id)
            .where(Grade.student_id == student_id)
            .distinct()
        )
        return [row[0] for row in result.all()]

# 10. List of courses taught to a specific student by a specific teacher
async def select_10(student_id: int, teacher_id: int):
    """Return the list of courses taught to a specific student by a specific teacher."""
    async with sessionmanager.session() as session:
        result = await session.execute(
            select(Subject.name)
            .join(Grade, Subject.id == Grade.subject_id)
            .where(Grade.student_id == student_id, Subject.teacher_id == teacher_id)
            .distinct()
        )
        return [row[0] for row in result.all()]


# 11. Average grade given by a specific teacher to a specific student
async def select_11(teacher_id: int, student_id: int):
    """Return the average grade given by a specific teacher to a specific student across all their subjects."""
    async with sessionmanager.session() as session:
        result = await session.execute(
            select(func.avg(Grade.grade))
            .join(Subject, Subject.id == Grade.subject_id)
            .where(Subject.teacher_id == teacher_id, Grade.student_id == student_id)
        )
        return result.scalar()

# 12. Grades of students in a group for a subject at the last lesson
async def select_12(group_id: int, subject_id: int):
    """Return the grades of students in a group for a subject at the last lesson (latest date_received)."""
    async with sessionmanager.session() as session:
        # Find the latest lesson date for this subject and group
        subq = (
            select(func.max(Grade.date_received))
            .join(Student, Student.id == Grade.student_id)
            .where(Student.group_id == group_id, Grade.subject_id == subject_id)
        )
        latest_date = (await session.execute(subq)).scalar()
        if not latest_date:
            return []
        # Get grades for that date
        result = await session.execute(
            select(Student.name, Grade.grade)
            .join(Grade, Student.id == Grade.student_id)
            .where(Student.group_id == group_id, Grade.subject_id == subject_id, Grade.date_received == latest_date)
        )
        return result.all() 

## Features

- **Database Management**: PostgreSQL with SQLAlchemy ORM
- **Async Operations**: Full async/await support for database operations
- **Data Seeding**: Automatic generation of test data with Faker
- **Migration System**: Alembic for database schema management
- **Docker Support**: Complete containerization with Docker Compose
- **Advanced Queries**: 12 complex SQL queries for data analysis

## Database Schema

The system includes the following entities:
- **Students**: Student information with group assignments
- **Teachers**: Teacher information
- **Subjects**: Course subjects with teacher assignments
- **Groups**: Student groups
- **Grades**: Student grades for subjects with timestamps

## Requirements

- Python 3.10+
- PostgreSQL 17.3
- Docker & Docker Compose (for containerized setup)

**Main packages:**
- sqlalchemy[asyncio]
- asyncpg
- alembic
- python-dotenv
- faker

## Quick Start with Docker

1. **Clone the repository**
2. **Create `.env` file** (copy from `exemple.env`):
   ```env
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=yourpassword
   POSTGRES_DB=todo_app
   POSTGRES_HOST=localhost
   POSTGRES_PORT=5432
   ```
3. **Run with Docker Compose:**
   ```sh
   docker-compose up --build
   ```

The system will automatically:
- Start PostgreSQL database
- Run database migrations
- Seed the database with test data (if empty)
- Execute all 12 sample queries

## Manual Setup

1. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

2. **Configure database** (update `.env` for local PostgreSQL)

3. **Run migrations:**
   ```sh
   alembic upgrade head
   ```

4. **Seed database:**
   ```sh
   python seed.py
   ```

5. **Run queries:**
   ```sh
   python main.py
   ```

## Available Queries

The system includes 12 complex queries:

1. **Top 5 students** by average grade across all subjects
2. **Best student** in a specific subject
3. **Average grade** in each group for a specific subject
4. **Overall average grade** across all grades
5. **Courses taught** by a specific teacher
6. **Students** in a specific group
7. **Grades** of students in a group for a specific subject
8. **Average grade** given by a specific teacher
9. **Courses attended** by a specific student
10. **Courses taught** to a student by a specific teacher
11. **Average grade** given by a teacher to a specific student
12. **Grades** of students in a group for a subject at the last lesson

## Example Output

```
============================================================
1. Top 5 students by average grade:
============================================================
  - ('Jenna Solis', Decimal('99.0000000000000000'))
  - ('Casey Faulkner', Decimal('97.5000000000000000'))
  - ('Brandi Roy', Decimal('93.0000000000000000'))
  - ('Erica Harmon', Decimal('93.0000000000000000'))
  - ('Blake Johnson', Decimal('89.0000000000000000'))

============================================================
2. Best student in subject 1:
============================================================
  ('Louis Alvarez', Decimal('98.0000000000000000'))

============================================================
3. Average grade in each group for subject 1:
============================================================
  - ('Group-Nw', Decimal('76.4166666666666667'))
  - ('Group-TA', Decimal('81.3571428571428571'))
  - ('Group-BJ', Decimal('78.6250000000000000'))

============================================================
4. Average grade across all grades:
============================================================
  80.8391304347826087

============================================================
5. Courses taught by teacher 1:
============================================================
  - Recently
  - Especially
  - Few

============================================================
6. Students in group 1:
============================================================
  - Jason Joseph
  - Louis Alvarez
  - Andrea Schroeder
  - Janet Manning
  - Kimberly White
  - Cynthia Smith
  - Sandra Williams
  - Leah Vaughn
  - Casey Faulkner
  - Jenna Solis
  - Brandi Roy
  - Dr. James Smith MD
  - Nicholas Madden
  - Charlotte Tucker

============================================================
7. Grades of students in group 1 for subject 1:
============================================================
  - ('Jason Joseph', 92)
  - ('Jason Joseph', 96)
  - ('Louis Alvarez', 98)
  - ('Janet Manning', 81)
  - ('Janet Manning', 97)
  - ('Kimberly White', 62)
  - ('Kimberly White', 68)
  - ('Cynthia Smith', 71)
  - ('Cynthia Smith', 65)
  - ('Leah Vaughn', 92)
  - ('Leah Vaughn', 91)
  - ('Dr. James Smith MD', 64)
  - ('Dr. James Smith MD', 100)
  - ('Nicholas Madden', 62)

============================================================
8. Average grade given by teacher 1:
============================================================
  79.1666666666666667

============================================================
9. Courses attended by student 1:
============================================================
  - Especially
  - Few
  - Leader
  - Public
  - Recently
  - War

============================================================
10. Courses taught to student 1 by teacher 1:
============================================================
  - Especially
  - Few
  - Recently

============================================================
11. Average grade given by teacher 1 to student 1:
============================================================
  68.5000000000000000

============================================================
12. Grades of students in group 1 for subject 1 at the last lesson:
============================================================
  - ('Jason Joseph', 96)
  
```

## Database Seeding

The system automatically seeds the database with realistic test data:
- **3 groups** with random names
- **3-5 teachers** with fake names
- **5-8 subjects** assigned to random teachers
- **30-50 students** assigned to random groups
- **Grades** for students across various subjects

The seeding process includes intelligent checks to avoid duplicate data and only runs when the database is empty.

## Development

### Adding New Queries

1. Add query function to `repository/my_select.py`
2. Import and call in `main.py`
3. Update this README with new query description

### Database Changes

1. Update models in `database/models.py`
2. Generate migration: `alembic revision --autogenerate -m "description"`
3. Apply migration: `alembic upgrade head`
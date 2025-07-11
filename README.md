
## Requirements
- Python 3.10+
- PostgreSQL
- pip install -r requirements.txt (see below)

**Main packages:**
- sqlalchemy[asyncio]
- asyncpg
- alembic
- python-dotenv
- faker

## Setup Instructions

1. **Clone the repository**
2. **Create and configure `.env`** (see `exemple.env` for example):
   ```
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=yourpassword
   POSTGRES_DB=todo_app
   POSTGRES_HOST=localhost
   POSTGRES_PORT=5432
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Run Alembic migrations:**
   ```sh
   alembic upgrade head
   ```
5. **Seed the database with random data:**
   ```sh
   python seed.py
   ```
6. **Run example select queries:**
   ```sh
   python repository/example_select_usage.py
   ```
## Exemple Result

   ```sh
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
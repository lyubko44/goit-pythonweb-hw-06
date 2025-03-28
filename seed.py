import random
from faker import Faker
from sqlalchemy.orm import sessionmaker
from models import engine, Student, Group, Teacher, Subject, Grade

fake = Faker()

Session = sessionmaker(bind=engine)
session = Session()


groups = [Group(name=f"Group {i+1}") for i in range(3)]
session.add_all(groups)
session.commit()


teachers = [Teacher(name=fake.name()) for _ in range(5)]
session.add_all(teachers)
session.commit()


subjects = [
    Subject(name=fake.word(), teacher=random.choice(teachers)) for _ in range(8)
]
session.add_all(subjects)
session.commit()

students = [Student(name=fake.name(), group=random.choice(groups)) for _ in range(50)]
session.add_all(students)
session.commit()

for student in students:
    for subject in subjects:
        for _ in range(random.randint(1, 20)):
            grade = Grade(
                student=student,
                subject=subject,
                grade=random.randint(1, 100),
                date_received=fake.date_this_year(),
            )
            session.add(grade)

session.commit()

print("Database seeded successfully!")

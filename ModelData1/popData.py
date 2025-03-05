import os
import django
import random
from datetime import time

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from testServer.models import Teacher, Class

def populate_data():
    teachers_data = [
        {"name": "Alice Smith", "email": "alice@example.com"},
        {"name": "Bob Johnson", "email": "bob@example.com"},
        {"name": "Charlie Brown", "email": "charlie@example.com"},
        {"name": "David Lee", "email": "david@example.com"},
        {"name": "Eve Wilson", "email": "eve@example.com"},
    ]

    classes_data = [
        {"name": "Math 101", "location": "Room 101", "time": time(9, 0)},
        {"name": "Science 202", "location": "Lab A", "time": time(10, 30)},
        {"name": "English 303", "location": "Library", "time": time(13, 0)},
        {"name": "History 404", "location": "Auditorium", "time": time(14, 30)},
        {"name": "Art 505", "location": "Studio B", "time": time(16, 0)},
    ]

    for teacher_data in teachers_data:
        teacher = Teacher.objects.create(**teacher_data)
        for class_data in classes_data:
            Class.objects.create(
                name=class_data["name"],
                teacher=teacher,
                location=class_data["location"],
                time=class_data["time"],
            )

if __name__ == "__main__":
    populate_data()
    print("Data populated successfully!")
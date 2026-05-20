from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class Student(BaseModel):
    name: str = 'nitish'
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10, default=5, description='A decimal value representing the cgpa of the student')


new_student = {'name': 'Arjun', 'age': 22, 'email': 'abc@example.com', 'cgpa': 8.5}

student = Student(**new_student)

student_dict = student.model_dump()

print(student_dict)

student_json = student.model_dump_json()

print(student_json)
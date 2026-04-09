from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str
    age: int = 18
    city: Optional[str] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10, default=5, description="decimal value for student sgpa")

# new_student = {'name':22, 'age': 25}  # error
# new_student = {'name':'Tushar', 'age': 25}
# new_student = {'name':'Tushar', 'age': '25'}  # pydantic can do implicit type coarsing if possible
new_student = {'name':'Tushar', 'email': 'a.bc@efr.com', 'cgpa': 15}
# new_student: Student = {'name':'Tushar', 'email': 'a.bc@efr.com', 'cgpa': 15}

student = Student(**new_student)

print(student)
print(student.name)
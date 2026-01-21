from pydantic import BaseModel, Field
from typing import Optional
class Student(BaseModel):

    name: str
    age: Optional[int]
    cgpa: float = Field(gt=0,lt=10)

new_student = {'name':'amir','age':21, 'cgpa':'7.25'}

student = Student(**new_student)
student_dict = dict(student)
print(student_dict['age'])
student_json = student.model_dump_json()

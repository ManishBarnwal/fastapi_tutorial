from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()  # create an instance of the FastAPI class

students = {
    1: {
        "name": "john",
        "age": 17,
        "year": "year 12"
    },
    2: {
        "name": "jane",
        "age": 16,
        "year": "year 11"
    }
}

class Student(BaseModel):
    name: str
    age: int
    year: str

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None


# what is an endpoint?
# one end point of a communication channel

# localhost/delete-user  # delete-user is the end-pint
# amazon.com/create-user # create-user is the end-point

# different types of end-point methods
# GET - get an information from the server
# POST - create a new resource/object (in the database)
# PUT - update an existing resource
# DELETE - delete a resource (example delete a user)

@app.get("/")  # / is the home-page
def index():
    return {"name": "First Data"}

# endpoint parameters
    # path parameters
    # query parameters 
    # both query parameters and path parameters are used to pass data to the server but there are some differences between them.
    
    # path parameters are part of the URL path and are used to identify a specific resource. They are defined in the URL using curly braces {}.
        # Path parameters are required and must be included in the URL to access the resource. They are typically used for mandatory parameters, such as an ID or a username.
    
    # Query parameters are optional parameters that are added to the URL after a ? symbol. They are used to filter, sort, or paginate resources.


# path parameters -- used to pass parameters as part of the url
# google.com/get-student/{path_parameter}

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(..., description="The ID of the student you want to view")):
    return students[student_id]

# query parameters
# google.com/results?search=Python&limit=10

@app.get("/get-by-name")
def get_student(name : str):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not Found"}


# you can also combine path and query parameters

# ------------------------------
# Request body and the post method

# post method -- to create a new object
@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student exists"}
    
    students[student_id] = student

    return students[student_id]

# Put method -- to update something that already exists
@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Student does not exist"}

    if student.name != None:
        students[student_id] = student.name
    
    if student.age != None:
        students[age] = student.age
    
    if student.year != None:
        students[year] = student.year

    return students[student_id] 

# delete method -- to delete something

@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in student:
        return {"Error": "Student does not exist."}

    del students[student_id]

    return {"Message": "Student deleted successfully."}



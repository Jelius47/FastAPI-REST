# A REST API, or Representational State Transfer API, 
# is a software architectural style that defines a set of constraints to
#  be used for creating web services. It uses standard HTTP methods 
# like GET, POST, PUT, and DELETE to enable communication between clients
#  and servers. 
# REST APIs are designed to be simple, flexible, and lightweight, 
# making them suitable for internet usage.
#  They are widely used to make data, media, content, and other
#  digital resources available through the web, allowing different 
# software applications to communicate with each other and exchange 
# data efficiently


from fastapi import FastAPI,Query,HTTPException,Path
from pydantic import BaseModel
from typing import Optional # this will help to give a hint of required data type 
from fuzzywuzzy import process # This function is to match the words in my dictionary
import json

app = FastAPI()

class Person(BaseModel):
    id: Optional[int] = None
    name: str
    age: str
    gender: str

# Interacting with our json file
with open('people.json','r') as f:
    people = json.load(f)

# print(people)

# Creating a function to acess people 
@app.get('/person/{p_id}',status_code=200)
def get_person(p_id: int):
    person = [p for p in people if p["id"]==p_id]
    return person[0] if len(person)> 0 else {}

# Else to get the documentation we have to write 127.0.0.1/docs
# Query -- Helps to filter values also to make documentation easier
@app.get("/search/",status_code=200) #For because of the Query keyword we are going not to specify the the id or name in the route 

def search_person(
    age: Optional[int] = Query(None, title="Age", description="The age to filter for"),
    name: Optional[str] = Query(None, title="Name", description="The name to filter for")):
    # Start with the full list of people
    filtered_people = people

    # Filter by age if age is provided
    if age is not None:
        filtered_people = [p for p in filtered_people if p["age"] == age]

    # If both age and name are not provided, return a message
    if age is None and name is None:
        return "No filters were provided. Please provide an age or a name."

    # Filter by name if name is provided
    if name is not None:
        # Use fuzzy matching to find names similar to the input name
        name_matches = process.extract(name, [p["name"] for p in filtered_people], limit=2)
        # Extract names with a high enough match score (e.g., >= 70)
        matched_names = [match[0] for match in name_matches if match[1] >= 70]
        # Filter the list by the matched names
        filtered_people = [p for p in filtered_people if p["name"] in matched_names]

    # Return a message if no matches are found
    if not filtered_people:
        return "No matching person found."

    return filtered_people
@app.post("/addperson",status_code=201)
def add_person(person:Person):
    # calculation of the id
    p_id = max([p["id"] for p in people])+1
    new_person = {
        "id": p_id,
        "name":person.name,
        "age":person.age,
        "gender":person.gender
    }
    people.append(new_person)
    # writtinng people.json

    with open('people.json', 'w') as f:
        json.dump(people,f)
    return new_person

# Changing person
@app.put("/changeperson",status_code=204)
def change_person(person:Person):
       new_person = {
        "id": person.id,
        "name":person.name,
        "age":person.age,
        "gender":person.gender
    }
       person_list = [p for p in people if p["id"]== person.id]
       if len(person_list)>0:
           people.remove(person_list[0])
           people.append((new_person))
             
           with open('people.json', 'w') as f:
                json.dump(people,f)
                return new_person
           return new_person
       else:
           return HTTPException(status_code=404,detail=f"Person with id {person.id} does not exist")

@app.delete("/deleteperson/{p_id}",status_code=204)
def delete_person(p_id:int= Path(title="id",description="The id of a person to be acessed")):
    person = [p for p in people if p["id"] == p_id]

    if len(person)>0:
        people.remove(person[0])
        with open('people.json','w') as f:
            json.dump(people,f)
        return "Successfully deleted a person with id {p_id}" 
    else:
        raise HTTPException(status_code=404,detail=f"The person with id {p_id} was not found")
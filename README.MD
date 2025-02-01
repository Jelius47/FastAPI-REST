# REST API for Managing People Data

This project is a RESTful API built using **FastAPI**, a modern Python web framework for building APIs. The API allows you to perform CRUD (Create, Read, Update, Delete) operations on a dataset of people stored in a JSON file (`people.json`). The API is designed to be simple, flexible, and lightweight, making it suitable for internet usage.

## Features

1. **Get a Person by ID**:
   - Retrieve details of a specific person by their unique `id`.
   - Endpoint: `GET /person/{p_id}`

2. **Search for People**:
   - Search for people by `age` or `name`. Supports fuzzy matching for names to handle slight misspellings.
   - Endpoint: `GET /search/`

3. **Add a New Person**:
   - Add a new person to the dataset. The `id` is automatically generated.
   - Endpoint: `POST /addperson`

4. **Update a Person**:
   - Update the details of an existing person by providing their `id`.
   - Endpoint: `PUT /changeperson`

5. **Delete a Person**:
   - Delete a person from the dataset by their `id`.
   - Endpoint: `DELETE /deleteperson/{p_id}`

## Technologies Used

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python.
- **Pydantic**: Used for data validation and settings management using Python type annotations.
- **FuzzyWuzzy**: A library for fuzzy string matching, used to handle slight misspellings in names.
- **JSON**: The dataset is stored in a JSON file (`people.json`), which is read and updated by the API.

## How It Works

1. **Data Storage**:
   - The dataset is stored in a JSON file (`people.json`). Each person is represented as a JSON object with the following fields:
     - `id`: Unique identifier for the person.
     - `name`: Name of the person.
     - `age`: Age of the person.
     - `gender`: Gender of the person.

2. **API Endpoints**:
   - The API provides endpoints to interact with the dataset:
     - **GET `/person/{p_id}`**: Retrieve a person by their `id`.
     - **GET `/search/`**: Search for people by `age` or `name` (with fuzzy matching for names).
     - **POST `/addperson`**: Add a new person to the dataset.
     - **PUT `/changeperson`**: Update an existing person's details.
     - **DELETE `/deleteperson/{p_id}`**: Delete a person by their `id`.

3. **Error Handling**:
   - The API handles errors gracefully:
     - If a person is not found, a `404 Not Found` error is returned.
     - If no filters are provided in the search endpoint, a message is returned asking for filters.

4. **Automatic ID Generation**:
   - When adding a new person, the `id` is automatically generated as the maximum `id` in the dataset plus one.

## Example Usage

# Testing the REST API

This section provides instructions on how to test the REST API using **cURL** commands and directly in the **browser**. The API endpoints can be tested using either method, depending on your preference.

---

## 1. Testing with cURL

cURL is a command-line tool used to send HTTP requests. Below are examples of how to test each endpoint using cURL.

### Get a Person by ID
```bash

curl -X GET "http://127.0.0.1:8000/person/1"
```
### Explanation:

    This sends a GET request to retrieve the person with id=1.

### Expected Response:
```json

{
    "id": 1,
    "name": "Jelius",
    "age": "24",
    "gender": "M"
}
```

### Search for People
```bash


curl -X GET "http://127.0.0.1:8000/search/?name=Jelious"
```
### Explanation:

    This sends a GET request to search for people with a name similar to Jelious (using fuzzy matching).

### Expected Response:
```json


[
    {
        "id": 1,
        "name": "Jelius",
        "age": "24",
        "gender": "M"
    }
]
```

### Add a New Person
```bash


curl -X POST "http://127.0.0.1:8000/addperson" -H "Content-Type: application/json" -d '{"name": "Alice", "age": "30", "gender": "F"}'
```
### Explanation:

    This sends a POST request to add a new person with the provided details.

    The -H flag specifies the Content-Type as application/json.

    The -d flag includes the JSON data for the new person.

### Expected Response:
```json


{
    "id": 5,
    "name": "Alice",
    "age": "30",
    "gender": "F"
}
```
### Update a Person
```bash


curl -X PUT "http://127.0.0.1:8000/changeperson" -H "Content-Type: application/json" -d '{"id": 1, "name": "Jelius Updated", "age": "25", "gender": "M"}'
```
### Explanation:

    This sends a PUT request to update the person with id=1.

    The -H flag specifies the Content-Type as application/json.

    The -d flag includes the JSON data for the updated person.

### Expected Response:
```json


{
    "id": 1,
    "name": "Jelius Updated",
    "age": "25",
    "gender": "M"

}
```
### Delete a Person
```bash


curl -X DELETE "http://127.0.0.1:8000/deleteperson/1"
```
### Explanation:

    This sends a DELETE request to delete the person with id=1.

### Expected Response:
```json


"Successfully deleted a person with id 1"
```
### 2. Testing in the Browser

You can also test the API directly in your browser using the FastAPI interactive documentation (Swagger UI).
Steps to Test in the Browser

#### Run the API:
    ```bash
    

    uvicorn main:app --reload
    ```

    ---Open the Documentation:

        Go to http://127.0.0.1:8000/docs in your browser.

        You will see the interactive API documentation (Swagger UI).

    ---Test Each Endpoint:

        Expand the endpoint you want to test (e.g., GET /person/{p_id}).

        Click the Try it out button.

        Enter the required parameters (e.g., p_id=1 for GET /person/{p_id}).

        Click Execute to send the request.

        View the response in the Responses section.

### Example: Testing GET /person/{p_id} in the Browser

    Open http://127.0.0.1:8000/docs.

    Expand the GET /person/{p_id} endpoint.

    Click Try it out.

    Enter p_id=1.

    Click Execute.

### View the response:
    ```json
    

    {
        "id": 1,
        "name": "Jelius",
        "age": "24",
        "gender": "M"
    }
    ```

Example: Testing POST /addperson in the Browser

    Open http://127.0.0.1:8000/docs.

    Expand the POST /addperson endpoint.

    Click Try it out.

### Enter the request body:
    ```json
    

    {
        "name": "Alice",
        "age": "30",
        "gender": "F"
    }
    ```

    --Click Execute.

### View the response:
    ```json
    

    {
        "id": 5,
        "name": "Alice",
        "age": "30",
        "gender": "F"
    }
```
### Conclusion

You can test the API using either cURL commands or the FastAPI interactive documentation in your browser. Both methods provide an easy way to interact with the API and verify its functionality.

    Use cURL for quick command-line testing.

    Use the browser for an interactive and visual testing experience.

Regards: Jelius H.
Tutorial and more stuffs:[NeuralNine](https://youtu.be/VSQZl43jFzk)
Lets develop Brains :)

Happy testing! 🚀
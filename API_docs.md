
# NER Flask Service API Documentation

This document outlines the RESTful API endpoints available in the NER Flask Service. This service provides Named Entity Recognition (NER) functionalities, user management, including signup and signin, and operations to manipulate NER requests.

## Base URL

All URLs referenced in the documentation have the base path `http://0.0.0.0:3000/api/`.

## Authentication

### Signup

- **Endpoint:** `/auth/signup`
- **Method:** POST
- **Description:** Registers a new user.
- **Body:**

```json
{
  "firstname": "John",
  "lastname": "Doe",
  "email": "john.doe@example.com",
  "password": "password123"
}
```

- **Success Response:** Status Code: 200

```json
{
  "message": "User Sign up Successful",
  "status": "success",
  "token": "<JWT Token>"
}
```

### Signin

- **Endpoint:** `/users/signin`
- **Method:** POST
- **Description:** Authenticates a user and returns a JWT token.
- **Body:**

```json
{
  "email": "john.doe@example.com",
  "password": "password123"
}
```

- **Success Response:** Status Code: 200

```json
{
  "message": "Authentication Successful",
  "status": "success",
  "token": "<JWT Token>"
}
```

## User Management

### Get User

- **Endpoint:** `/users/get_user`
- **Method:** GET
- **Description:** Retrieves the currently authenticated user's information.
- **Headers:** `Authorization: Bearer <JWT Token>`
- **Success Response:** Status Code: 200

```json
{
  "data": {
    "created_at": "Wed, 03 Apr 2024 19:54:10 GMT",
    "email": "ajw@gmail.com",
    "firstname": "klsa",
    "id": "1a0f6b89-4329-4ee6-bba3-93aff4a11796",
    "lastname": "head",
    "role": "user"
  }
}

```

### Update Account

- **Endpoint:** `/users/update_user`
- **Method:** PUT
- **Description:** Updates user information.
- **Headers:** `Authorization: Bearer <JWT Token>`
- **Body:**

```json
{
  "id": "1",
  "firstname": "Jane"
}
```

- **Success Response:** Status Code: 200

```json
{
  "message": "User update Successful",
  "status": "success"
}
```

### Delete User

- **Endpoint:** `/users/delete_user`
- **Method:** DELETE
- **Description:** Deletes the specified user.
- **Headers:** `Authorization: Bearer <JWT Token>`
- **Body:**

```json
{
  "id": "1"
}
```

- **Success Response:** Status Code: 200

```json
{
  "message": "User deletion Successful",
  "status": "success"
}
```

## NER Operations

### Submit NER Request

- **Endpoint:** `/ner/ner_post`
- **Method:** POST
- **Description:** Submits a text for NER processing.
- **Headers:** `Authorization: Bearer <JWT Token>`
- **Body:**

```json
{
  "text": "Apple is a company."
}
```

- **Success Response:** Status Code: 200

```json
{
  "message": "NER Successful",
  "status": "success",
  "text_id": "48ab9a7d-c610-4519-a393-b33d97b30ca5",
  "entities": [
    {
      "end_char": 5,
      "label": "ORG",
      "start_char": 0,
      "text": "Apple"
    }
  ]
}
```

### Get NER Results

- **Endpoint:** `/ner/ner_get`
- **Method:** GET
- **Description:** Retrieves NER results using a specific text ID.
- **Headers:** `Authorization: Bearer <JWT Token>`
- **Body:**

```json
{
  "text_id": "48ab9a7d-c610-4519-a393-b33d97b30ca5"
}
```

- **Success Response:** Status Code: 200

```json
{
  "message": "NER Successful",
  "status": "success",
  "entities": [
    {
      "entity_end": 5,
      "entity_id": "48fa98ef-ff2a-4725-b2a9-d24c3364f4f4",
      "entity_start": 0,
      "entity_type": "ORG",
      "entity_value": "Apple"
    }
  ]
}
```

### Delete NER Request

- **Endpoint:** `/ner/ner_delete`
- **Method:** DELETE
- **Description:** Deletes a specific NER request and its results.
- **Headers:** `Authorization: Bearer <JWT Token>`
- **Body:**

```json
{
  "text_id": "b3159283-7cde-4e06-a6e9-b7a364f83fae"
}
```

- **Success Response:** Status Code: 200

```json
{
  "message": "NER request deletion Successful",
  "status": "success"
}
```

## Errors

All error responses follow a consistent format:

```json
{
  "status": "error",
  "message": "<Error Message>"
}
```
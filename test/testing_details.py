signup_request_valid_1 = {
    "id": "9825855d-f883-47dd-a776-28708e237313",
    "firstName": "John",
    "lastName": "Doe",
    "email": "john.doe@example.com",
    "password": "StrongPass123!"
}

signup_request_invalid_1 = {
    "id": "9825855d-f883-47dd-a776-28708e237313",
    "firstName": "John",
    "lastName": "Doe",
    "email": "invalid-email",
    "password": "123"
}

signup_request_invalid_2 = {
    "id": "9825855d-f883-47dd-a776-28708e237313",
    "firstName": "",
    "lastName": "Doe",
    "email": "john.doe@example.com",
    "password": "StrongPass123!"
}

signup_request_invalid_3 = {
    "id": "9825855d-f883-47dd-a776-28708e237313",
    "firstName": "John",
    "lastName": "Doe",
    "email": "john.doe@example.com",
    "password": ""
}

signup_request_invalid_4 = {
    "id": "00000000-0000-0000-0000-000000000004",
    "firstName": "",
    "lastName": "",
    "email": "john.doe@example.com",
    "password": "StrongPass123!"
}

login_valid_1 = {
  "email": "john.doe@example.com",
  "password": "StrongPass123!"
}

login_invalid_1 = {
  "email": "invalid-email",
  "password": "StrongPass123!"
}

login_invalid_2 = {
  "email": "john.doe@example.com",
  "password": ""
}

login_invalid_3 = {
  "email": "",
  "password": "StrongPass123!"
}
# Python MongoDB Auth API

A secure authentication API built with FastAPI and MongoDB. This API provides JWT-based authentication, user management, and role-based access control.

## Features

- User registration and authentication
- JWT token-based security
- Password hashing with bcrypt
- Role-based access control
- MongoDB integration
- Comprehensive error handling
- Logging system
- CORS support
- Swagger UI documentation

## Tech Stack

- **FastAPI**: Modern, fast web framework for building APIs
- **MongoDB**: NoSQL database for storing user data
- **PyMongo**: MongoDB driver for Python
- **JWT (JSON Web Tokens)**: For secure authentication
- **Pydantic**: Data validation and settings management
- **Passlib & Bcrypt**: Secure password hashing
- **Python-Jose**: JWT token creation and validation

## Project Structure

```
python-auth/
├── app/
│   ├── __init__.py         # Package definition and version info
│   ├── auth.py             # Authentication functions
│   ├── config.py           # Application configuration
│   ├── database.py         # Database operations
│   ├── models.py           # Data models
│   └── main.py             # Main application and API endpoints
├── venv/                   # Virtual environment
├── .env                    # Environment variables
├── .gitignore              # Git ignore file
├── README.md               # Project documentation
└── requirements.txt        # Dependencies
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/CemWebDev/fastapi-mongodb-authentication.git
   cd python-auth
   ```

2. Create and activate a virtual environment
   ```bash
   # Windows
    python -m venv venv
    venv\Scripts\activate

    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory with the following variables
    ```bash
    SECRET_KEY=your-secret-key-change-in-production
    ALGORITHM=HS256
    ACCESS_TOKEN_EXPIRE_MINUTES=30
    MONGO_URI=mongodb://localhost:27017
    DATABASE_NAME=auth_api_db
    CORS_ORIGINS=["http://localhost:3000", "http://localhost:8000"]
   ```

5. Start the server
    ```bash
    uvicorn app.main:app --reload
   ```

6. Access the API documentation at:
    ```bash
    http://localhost:8000/docs
   ```


## API Endpoints

### Authentication

- **POST /register**: Register a new user
  ```json
  {
    "username": "testuser",
    "email": "test@example.com",
    "password": "securepassword",
    "full_name": "Test User"    
  }

- **POST /token**: Login and get access token


### User Management

- **GET /users/me**: Get current user information
- **PUT /users/me**: Update current user information
```json
{
  "email": "newemail@example.com",
  "full_name": "Updated Name",
  "password": "newpassword"
}
```

### Protected Resources

- **GET /protected-resource**: Example of a protected resource

## Security

- Passwords are hashed using bcrypt
- Authentication is handled via JWT tokens
- Role-based access control for different endpoints
- CORS protection
- Environment variables for sensitive information

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request



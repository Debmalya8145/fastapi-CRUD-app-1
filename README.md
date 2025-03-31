# FastAPI Application for CRUD operations

## Overview
This project is a RESTful API built using FastAPI for managing users. It provides CRUD operations (Create, Read, Update, Delete) for user data and follows best practices for system design and scalability.

## Features
- **User Registration:** Create a new user.
- **Retrieve User:** Get user details by ID.
- **Update User:** Modify user information.
- **Delete User:** Remove a user from the database.
- **Database Integration:** Uses SQLAlchemy with PostgreSQL.
- **Validation & Serialization:** Pydantic for request and response validation.
- **Dependency Injection:** Efficient resource management.

## Technologies Used
- **FastAPI** (API framework)
- **SQLAlchemy** (ORM for database interactions)
- **PostgreSQL** (Database)
- **Pydantic** (Data validation & serialization)
- **Uvicorn** (ASGI server for FastAPI)
- **Alembic** (Database migrations)

## Installation

### Prerequisites
- Python 3.10+
- PostgreSQL installed and running

### Setup
1. **Clone the Repository**
   ```bash
   git clone https://github.com/Debmalya8145/fastapi-CRUD-app-1.git
   cd fastapi-CRUD-app-1
   ```
2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```
3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure Environment Variables**
   Create a `.env` file with the following:
   ```env
   DATABASE_URL=postgresql://user:password@localhost/db_name
   ```

## API Endpoints
| Method | Endpoint         | Description          |
|--------|-----------------|----------------------|
| GET    | `/`             | to see all users     |
| POST   | `/users`        | Create a new user   |
| GET    | `/users    `   | Get user by ID      |
| PUT    | `/users    `   | Update user         |
| DELETE | `/users    `   | Delete user         |

## Run the app
There are multiple options available when running the app.
The way you're likely going to want to do it is by running the command
```bash
uvicorn main:app --reload
```
If you would like to choose a specific port (if 8000 is already occupied by another program), then you can run
```bash
uvicorn main:app --reload --port <PORT>
```
where the `<PORT>` is a number of your choosing.
For the rest of the options when running a uvicorn app, visit https://www.uvicorn.org/#command-line-options.

## Testing the API
Use **FastAPI-Swagger UI** to test endpoints.
```bash
http://127.0.0.1:8000/docs#
```

## Contributing
1. Fork the repo
2. Create a feature branch (`git checkout -b feature-branch`)
3. Commit changes (`git commit -m 'Add new feature'`)
4. Push to your branch (`git push origin feature-branch`)
5. Open a Pull Request

## License
This project is licensed under the MIT License.


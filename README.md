# 🏥 SmartClinic API

A secure and scalable backend API for a modern healthcare clinic, enabling management of patients, doctors, appointments, and lab reports with JWT-based authentication. Built using FastAPI, SQLite, and other production-grade components.

---

## 🚀 Project Status

✅ FastAPI app initialized  
✅ `.env` configuration using `python-dotenv`  
✅ JWT-based user authentication (register/login)  
✅ Pydantic schemas for input/output models  
✅ SQLAlchemy ORM models & SQLite DB setup  
✅ CRUD API for Doctors  
✅ CRUD API for Patients  
🔄 Appointments & Lab Reports (WIP)  
🔄 Postman Collection  
🔄 Test automation using `pytest`  
🔄 Deployment planning (e.g., Render, Railway)

---


## 📁 Project Structure (So Far)

```text
smartclinic-api/
├── app/
│   ├── main.py               # FastAPI app entry point
│   ├── config.py             # Loads environment variables from .env
│   ├── db.py                 # SQLAlchemy DB setup
│   ├── models.py             # SQLAlchemy ORM models
│   ├── schemas.py            # Pydantic schemas for validation/serialization
│   ├── dependencies/
│   │   └── auth.py           # Dependency for token-based auth
│   └── routes/
│       ├── auth.py           # User registration & login
│       ├── doctors.py        # CRUD operations for doctors
│       └── patients.py       # CRUD operations for patients
├── .env.example              # Sample environment file (safe to share)
├── requirements.txt          # Python dependencies
├── .gitignore                # Git ignore rules
└── README.md                 # You are here!

```

---

## 🔧 How to Run Locally

### 🛠️ 1. Clone the repo

```bash

git clone https://github.com/anitta-antony-92/smartclinic-api.git
cd smartclinic-api
```
### 🐍 2. Set up virtual environment
```bash

python -m venv venv
.\venv\Scripts\Activate.ps1     # PowerShell
```
### 📦 3. Install dependencies
```bash

pip install -r requirements.txt
```
### 🧪 4. Create your .env file
```ini

# Create a .env file and fill in your own values
APP_NAME=SmartClinicAPI
JWT_SECRET=your_secret_here
JWT_ALGORITHM=HS256
```
### ▶️ 5. Run the API
```bash

uvicorn app.main:app --reload
```
Now visit: http://127.0.0.1:8000

Swagger docs: http://127.0.0.1:8000/docs

### 🧪 Swagger Testing Guide
- Register a user → POST /register

- Payload: {"username": "john", "email": "john@email.com", "password": "secret"}

- Login → POST /login

- Returns: JWT token

- Authorize using token → Click Authorize and use Bearer <your_token>

- Use doctor & patient routes → Authenticated access required


## ✅ Features Implemented

- [x] FastAPI setup and root endpoint
- [x] `.env` configuration using `python-dotenv`
- [x] Config class for accessing environment variables
- [x] User registration & login (coming soon)
- [x] Appointments & patient records
- [x] JWT Authentication & protected routes
- [ ] Testing with pytest
- [ ] Postman collection
- [ ] Deployment to Render


## 🛡️ Tech Stack
- Python 3.11+

- FastAPI

- Uvicorn

- Dotenv for config

- PostgreSQL (coming soon)

- JWT Authentication (coming soon)

## 👩‍💻 Author
Anitta Antony

GitHub: anitta-antony-92

📍 Based in Qatar | Open to remote opportunities


---


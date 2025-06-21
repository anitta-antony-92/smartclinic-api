# 🏥 SmartClinic API

A FastAPI-powered backend system simulating a smart clinic’s API functionalities — including patient registration, doctor management, appointment booking, and secure authentication.

---

## 🚀 Project Status

✅ Basic project setup complete  
✅ Secure environment configuration added  
🔜 Authentication & user management coming up

---


## 📁 Project Structure (So Far)

```text
smartclinic-api/
├── app/
│   ├── main.py           # FastAPI app entry point
│   ├── config.py         # Loads environment variables
│   └── routes/
│       └── auth.py       # Authentication routes (coming soon)
├── .env.example          # Sample environment variables file
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation

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

## ✅ Features Implemented

- [x] FastAPI setup and root endpoint
- [x] `.env` configuration using `python-dotenv`
- [x] Config class for accessing environment variables
- [ ] User registration & login (coming soon)
- [ ] Appointments & patient records
- [ ] JWT Authentication & protected routes
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

## ✅ Next Step

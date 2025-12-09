# 🌦️ Django Weather Data App (REST API + Supabase + OpenWeather + Dashboard)

This is a complete full-stack demo web application built using **Django**, **Django REST Framework**, **PostgreSQL (Supabase)**, and **OpenWeather API**.  
It demonstrates:

✅ REST CRUD APIs  
✅ Live Third-party API Integration  
✅ PostgreSQL Cloud Database (Supabase)  
✅ Data Visualization with Chart.js  
✅ Deployment on Render  

---

## ✅ FEATURES

### ✅ 1. City CRUD REST APIs
- Create City  
- View All Cities  
- Update City  
- Delete City  

### ✅ 2. Live Weather API Integration
- Fetches **real-time weather** using **OpenWeather API**

### ✅ 3. PostgreSQL Database (Supabase)
- Cloud-hosted database
- Secure environment variable connection

### ✅ 4. Weather Dashboard (Visualization)
- User enters city name
- Live temperature displayed
- Bar chart generated using **Chart.js**

### ✅ 5. Production Deployment
- Hosted on **Render**
- Public Live URL available

---

## 🔗 API ENDPOINTS

### 📍 City CRUD APIs
| Method | Endpoint |
|--------|----------|
| GET | `/api/cities/` |
| POST | `/api/cities/` |
| GET | `/api/cities/{id}/` |
| PUT | `/api/cities/{id}/` |
| DELETE | `/api/cities/{id}/` |

---

### 🌦️ Live Weather API
-OpenWeather API

- Enter a city
- Click **Get Weather**
- Temperature & chart will be displayed

---

## ⚙️ TECH STACK

| Layer | Technology |
|--------|------------|
| Backend | Python, Django |
| API | Django REST Framework |
| Database | PostgreSQL (Supabase) |
| External API | OpenWeatherMap |
| Frontend | HTML, JavaScript |
| Charts | Chart.js |
| Deployment | Render |

---

## 🛠️ LOCAL SETUP INSTRUCTIONS

### ✅ 1️⃣ Clone Repository
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME


Create Virtual Environment & Install Dependencies
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt


Create .env File (Project Root)
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=YOUR_SUPABASE_PASSWORD
DB_HOST=YOUR_SUPABASE_HOST
DB_PORT=5432

SECRET_KEY=django-insecure-dev-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

OPENWEATHER_API_KEY=YOUR_OPENWEATHER_API_KEY

Apply Migrations
python manage.py migrate

Create Admin (Optional)
python manage.py createsuperuser

Run Development Server
python manage.py runserver

Open in browser:
http://127.0.0.1:8000/api/dashboard/


👨‍💻 DEVELOPED BY
Piyush Zore
Computer Science Graduate | Full Stack & Data Engineering Aspirant
India

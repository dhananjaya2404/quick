## QuickHire – Job Post & Apply API

QuickHire is a one-day Django + DRF API project that provides a simple job portal with JWT authentication, role-based access, and endpoints for employers and applicants.

### Tech Stack

- **Backend**: Django, Django REST Framework
- **Auth**: JWT via `djangorestframework-simplejwt`
- **Database**: SQLite (default Django DB)

---

## 1. Project Setup

### 1.1. Clone & Move Into Project

```bash
cd quickhire_project/quickhire
```

### 1.2. (Recommended) Create Virtual Environment

```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# Windows cmd
.venv\Scripts\activate.bat
# Linux / macOS
source .venv/bin/activate
```

### 1.3. Install Dependencies

```bash
pip install django djangorestframework djangorestframework-simplejwt
```

### 1.4. Run Migrations

```bash
python manage.py migrate
```

### 1.5. Create Superuser (Admin)

```bash
python manage.py createsuperuser
```

Follow the prompts to set username, email, and password.

### 1.6. Run Development Server

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`.

---

## 2. Auth & Roles

### Roles

The custom `User` model has a `role` field:

- `employer`
- `applicant`

### Auth Flow

1. **Register** (`POST /api/register/`)
2. **Login** (`POST /api/token/`) – returns `access` and `refresh` tokens
3. Use `Authorization: Bearer <access_token>` header for authenticated requests.

---

## 3. API Endpoints

Base URL: `http://127.0.0.1:8000/api/`

### 3.1. Auth & Users

- **Register**  
  - **POST** ` /api/register/`  
  - Body:

    ```json
    {
      "username": "john",
      "email": "john@example.com",
      "password": "password123",
      "role": "employer"   // or "applicant"
    }
    ```

- **Login (JWT)**  
  - **POST** `/api/token/`  
  - Body:

    ```json
    {
      "username": "john",
      "password": "password123"
    }
    ```

  - Response contains `access` and `refresh` tokens.

- **Refresh Token**  
  - **POST** `/api/token/refresh/`

---

### 3.2. Jobs (Employer & Authenticated)

- **List Jobs (Authenticated)**  
  - **GET** `/api/jobs/`  
  - Query params:
    - `?title=developer`
    - `?location=remote`

- **Create Job (Employer only)**  
  - **POST** `/api/jobs/`  
  - Body:

    ```json
    {
      "title": "Backend Developer",
      "description": "Django/DRF backend role",
      "salary": "80000.00",
      "location": "Remote"
    }
    ```

- **Retrieve Job (Authenticated)**  
  - **GET** `/api/jobs/<id>/`

- **Update Job (Owner Employer only)**  
  - **PUT** `/api/jobs/<id>/`

- **Delete Job (Owner Employer only)**  
  - **DELETE** `/api/jobs/<id>/`

- **View Applicants of a Job (Employer only)**  
  - **GET** `/api/employer/applicants/<job_id>/`

---

### 3.3. Applications (Applicant only)

- **Apply for a Job**  
  - **POST** `/api/apply/`  
  - Body:

    ```json
    {
      "job": 1,
      "resume_link": "https://example.com/my-resume.pdf"
    }
    ```

- **View My Applications**  
  - **GET** `/api/myapplications/`

Applicants can see:

- Job title
- Resume link
- Current status (`Applied`, `Reviewed`, `Accepted`, `Rejected`)

---

## 4. Admin Panel

- URL: `http://127.0.0.1:8000/admin/`
- Login with the superuser credentials.
- You can manage:
  - Users (`role`, email, etc.)
  - Jobs
  - Applications

---

## 5. Postman Collection

A Postman collection is provided in `quickhire_postman_collection.json`.  
Import it into Postman to quickly test:

- Register
- Login & get JWT
- Create jobs (employer)
- Apply for jobs (applicant)
- View job listings, applicants, and application statuses

---

## 6. Notes

- Ensure that when creating users, the `role` is set correctly (`employer` vs `applicant`), as permissions depend on this.
- All authenticated endpoints require `Authorization: Bearer <access_token>` header.



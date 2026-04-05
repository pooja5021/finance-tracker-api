# Finance Tracker API

A backend system built using **FastAPI** to manage and analyze personal financial transactions with role-based access control.

---

## Features

### Authentication
- User Registration
- Login with JWT Token
- Secure API access using Swagger Authorization

### Role-Based Access
- **Admin** → Full access (create, update, delete, analytics)
- **Analyst** → Create + view + analytics
- **Viewer** → Read-only access

---

### Transaction Management
- Create transactions (income/expense)
- View transactions (user-specific)
- Update & delete (admin only)
- Filter by:
  - Type (income/expense)
  - Category
  - Date range

---

### Analytics
- Total income
- Total expenses
- Current balance
- Category-wise breakdown
- Monthly summary
- Recent transactions

---

## Tech Stack

- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- JWT Authentication

---

## Project Structure
## API Base URL

http://127.0.0.1:8000

## Authentication

Use Swagger UI:
- Click "Authorize"
- Enter username & password

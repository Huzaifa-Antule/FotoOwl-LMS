# Library Management System - Tasks Completed

This repo includes Backend code of FotoOwl Tasks for a Library Management System built using Django and Django Rest Framework (DRF) / Python , with an Sqlite3 database. It allows librarians to manage users and book requests, while library users can request and view book borrowing details.

## I've Sucessfully Implemented Following Features:

### **Librarian APIs:**
- **Create a new library user** with an email and password.
- **View all book borrow requests.**
- **Approve or deny a borrow request.**
- **View a user’s book borrow history.**

### **Library User APIs:**
- **Get a list of books.**
- **Submit a request** to borrow a book for specific dates (date1 to date2).
- **View personal book borrow history.**
- **Download borrow history as a CSV file**.

### Considering Following **Key Rules:**
- A book cannot be borrowed by more than one user during the same period.
- Edge cases handled:
  - Invalid or incomplete requests.
  - Overlapping borrow dates.
  - Requests for non-existent users or books.

### **Database Schema:**
The database schema is designed to support the following entities:
- **Users** (Librarian and Library Users)
- **Books**
- **Borrow Requests**

### **Technologies Used:**
- **Python**: Django, Django REST Framework
- **Database**: SQLite (can be easily changed to MySQL or PostgreSQL)
- **Authentication**: Basic Authentication
- **CSV**: For downloading borrow history as a CSV file

### **Setup and Installation**

1. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Mac/Linux
   venv\Scripts\activate     # For Windows
   ```
2. **Clone the repository**:
   ```bash
   git clone https://github.com/Huzaifa-Antule/FotoOwl-LMS.git
   cd library-management-system
   ```

3. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Migrate the database**:
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (for librarian access)**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the API**:
   - API documentation can be explored via the Django admin panel or directly using the endpoints.
   - Librarians can create new users, view borrow requests, and approve/deny requests via the APIs.

### **API Endpoints**

- **POST** `/users/` – Create a new user (Librarian).
- **GET** `/borrow-requests/` – View all book borrow requests (Librarian).
- **PATCH** `/borrow-requests/{id}/` – Approve or deny a borrow request (Librarian).
- **GET** `/borrow-requests/download-history/` – Download borrow history as CSV (Library User).
- **POST** `/borrow-requests/` – Submit a borrow request for a book (Library User).

### **Testing**

You can use **Postman** to test the endpoints.  

#### **Librarian APIs**
1. **Create User**:  
   **POST** `/users/`  
   Data:  
   ```json
   {"email": "user@example.com", "password": "password"}
   ```

2. **View Borrow Requests**:  
   **GET** `/borrow-requests/`  

3. **Approve/Deny Request**:  
   **PATCH** `/borrow-requests/{id}/`  
   Data:  
   ```json
   {"status": "Approved"}
   ```

4. **View User History**:  
   **GET** `/borrow-requests/history/{user_id}/`  

#### **Library User APIs**
1. **List Books**:  
   **GET** `/books/`  

2. **Submit Borrow Request**:  
   **POST** `/borrow-requests/`  
   Data:  
   ```json
   {"book_id": 1, "start_date": "2024-02-01", "end_date": "2024-02-07"}
   ```
3. **View Borrow History**:  
   **GET** `/borrow-requests/history/`  

4. **Download Borrow History (CSV)**:  
   **GET** `/borrow-requests/download-history/`  

### **Pending Features that are not implemented:**
- **JWT-based Authentication** is not implemented (currently using Basic Authentication).
- **API documentation** has not been included.

### Note:
- I've Completed the tasks, some tasks are little bit complicated so i took suggestions/code from Chatgpt and Django REST Framework Documentation for the reference.

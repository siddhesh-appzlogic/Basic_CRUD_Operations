# 📚 Books Data API 

A RESTful API built using **Django** and **Django REST Framework (DRF)** for performing **CRUD operations** on book data.

---

## 🚀 Features

- Add new book entries 📘
- Retrieve all books or individual book details 🔍
- Update book information ✏️
- Delete book records 🗑️
- MySQL database integration
- Environment variable support using `.env` for secure settings

---

## 🛠️ Tech Stack

- **Backend**: Django 5.2.1, Django REST Framework
- **Database**: MySQL
- **Other**: Python 3.x, `django-environ` for environment variables

---

## 🚀 Setup Instructions

### 1. Clone the Repository

    ```bash
    git clone https://github.com/siddhesh-appzlogic/Basic_CRUD_Operations.git
    cd Basic_CRUD_Operations
    ```

### 2. Create and Activate Virtual Environment

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

### 3. Install Dependencies

    ```bash
    pip install -r requirements.txt
    ```

### 4. Set Up `.env` File

    Create a `.env` file in the project root with the following content:

    ```env
    SECRET_KEY=your_django_secret_key
    DEBUG=True
    ALLOWED_HOSTS=127.0.0.1,localhost

    DB_NAME=your_db_name
    DB_USER=your_mysql_username
    DB_PASSWORD=your_mysql_password
    DB_HOST=127.0.0.1
    DB_PORT=3306
    ```

### 5. Configure the Database

    Ensure MySQL is installed and create a database:

    ```sql
    CREATE DATABASE your_db_name;
    ```

### 6. Run Migrations

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

### 7. Import Sample Database (Optional)
    A file named `django_db_dump.sql` is included with sample data.

    ```bash
    mysql -u your_username -p your_db_name < django_db_dump.sql
    ```

    > 🔐 Replace `your_username` and `your_db_name` with your actual MySQL credentials.

### 8. Run the Server

    ```bash
    python manage.py runserver
    ```

    Visit: [http://127.0.0.1:8000/api/]

### 9. API Endpoints

    | Method | Endpoint               | Description          |
    |--------|------------------------|----------------------|
    | POST   | `/api/create/`         | Create a new book    |
    | GET    | `/api/read/`           | Get all books        |
    | PUT    | `/api/update/<pk>/`    | Update a book by ID  |
    | DELETE | `/api/delete/<pk>/`    | Delete a book by ID  | 
           
 ## 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 🧑‍💻 Author

**Mr. Siddhesh Walunj**  
GitHub: [@siddhesh-appzlogic](https://github.com/siddhesh-appzlogic)

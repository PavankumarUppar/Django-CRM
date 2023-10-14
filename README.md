# Django CRM Project

This is a simple Customer Relationship Management (CRM) web application built using Django. It allows users to register, log in, manage customer records, add new records, update existing records, and delete records. The project also utilizes Bootstrap for a clean and responsive user interface.

## Features

- User Registration
- User Login
- User Logout
- Customer Record Management
  - View Customer Records
  - Add New Customer Records
  - Update Existing Customer Records
  - Delete Customer Records

## Setup

Follow these steps to set up and run the project on your local machine:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/PavankumarUppar/Django-CRM.git
   cd Django-CRM
   ```
   
2. **Create a Vurtual Environment**

  ```bash
  python -m venv venv
  ```

3. **Activate the Virtual Environment**

  On Windows:
  ```bash
  venv\Scripts\activate
  ```

  On macOS and Linux:
  ```bash
  source venv/bin/activate
  ```

4. **Install Dependencies**

  ```bash
  pip install -r requirements.txt
  ```

5. **Apply Database Migrations**

  ```bash
  python manage.py migrate
  ```

6. **Create a Superuser (Admin User)**
   
  You can create an admin user to access the Django admin panel:
  ```bash
  python manage.py createsuperuser
  ```
  Follow the prompts to create your admin account.

7. **Run the Development Server**

  ```bash
  python manage.py runserver
  ```
  The development server will start, and you can access the CRM application at (http://127.0.0.1:8000/)

8. **Access the Admin Panel**

   
  You can access the Django admin panel at (http://127.0.0.1:8000/admin/) and log in with the superuser account you created.


## Usage

1. Registration
   - Visit (http://127.0.0.1:8000/register/) to register a new user account.

2. Login
   - Visit (http://127.0.0.1:8000/) to log in using your registered account.

3. Customer Records
   - Once logged in, you can view, add, update, and delete customer records.

4. Logout
   - You can log out of your account by visiting (http://127.0.0.1:8000/logout/).


## Technologies Used

- Python
- Django
- Bootstrap


## Dependencies

- asgiref==3.7.2
- Django==4.2.6
- mysql-connector==2.2.9
- mysql-connector-python==8.1.0
- mysqlclient==2.2.0
- protobuf==4.21.12
- sqlparse==0.4.4
- typing_extensions==4.8.0
- tzdata==2023.3

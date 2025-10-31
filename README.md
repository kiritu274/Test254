# Management Web Application

A responsive web application for managing projects, tasks, and users built with Django, HTML, CSS, and JavaScript.

## Features

- **User Authentication**: Secure registration, login, and logout system
- **Role-Based Access Control**: Three user roles (Admin, Manager, User) with different permissions
- **Project Management**: Create, read, update, and delete projects with status tracking
- **Task Management**: Assign tasks to users with priority levels, due dates, and status tracking
- **Dashboard**: Interactive charts and visualizations using Chart.js
- **Responsive Design**: Mobile-friendly interface using Bootstrap

## Technologies Used

- **Backend**: Django 5.2.6
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: SQLite (default Django database)
- **UI Framework**: Bootstrap 4
- **Charts**: Chart.js
- **Python Version**: 3.13.7

## Installation

1. **Clone or download the project**:
   ```bash
   cd management_app
   ```

2. **Create and activate virtual environment**:
   ```bash
   py -m venv venv
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser**:
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to create an admin account.

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the application**:
   Open your browser and go to `http://127.0.0.1:8000/`

## Deployment

### Fly.io Deployment (Recommended)

Fly.io provides fast, secure deployment with a generous free tier.

1. **Install Fly CLI** from https://fly.io/docs/getting-started/installing-flyctl/

2. **Login to Fly.io**:
   ```bash
   fly auth login
   ```

3. **Launch the app** (skip the auto-generated config):
   ```bash
   cd management_app
   fly launch --no-deploy
   ```
   Follow the prompts to configure your app name and region.

4. **Set environment variables**:
   ```bash
   fly secrets set DEBUG=False
   fly secrets set SECRET_KEY=your-secret-key-here
   fly secrets set ALLOWED_HOSTS=your-app-name.fly.dev
   ```

5. **Deploy to Fly.io**:
   ```bash
   fly deploy
   ```

6. **Run migrations on Fly.io**:
   ```bash
   fly ssh console
   python manage.py migrate
   python manage.py createsuperuser
   exit
   ```

7. **Access your deployed app**:
   Your app will be available at `https://your-app-name.fly.dev/`

### Heroku Deployment (Alternative)

1. **Install Heroku CLI** from https://devcenter.heroku.com/articles/heroku-cli

2. **Login to Heroku**:
   ```bash
   heroku login
   ```

3. **Create Heroku app**:
   ```bash
   heroku create your-app-name
   ```

4. **Add PostgreSQL database** (optional, for production):
   ```bash
   heroku addons:create heroku-postgresql:hobby-dev
   ```

5. **Set environment variables**:
   ```bash
   heroku config:set DEBUG=False
   heroku config:set SECRET_KEY=your-secret-key-here
   heroku config:set ALLOWED_HOSTS=your-app-name.herokuapp.com
   ```

6. **Deploy to Heroku**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   heroku git:remote -a your-app-name
   git push heroku main
   ```

7. **Run migrations on Heroku**:
   ```bash
   heroku run python manage.py migrate
   ```

8. **Create superuser on Heroku**:
   ```bash
   heroku run python manage.py createsuperuser
   ```

9. **Access your deployed app**:
   Your app will be available at `https://your-app-name.herokuapp.com/`

## Default Admin Account

- **Username**: admin
- **Password**: admin123

## User Roles

- **Admin**: Full access to all features, can manage users, projects, and tasks
- **Manager**: Can create and manage projects, assign tasks to users
- **User**: Can view assigned tasks, update task status, view projects

## Project Structure

```
management_app/
├── management_project/          # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── user_app/                    # User authentication and management
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/
├── project_app/                 # Project management
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/
├── task_app/                    # Task management
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/
├── templates/                   # Global templates
├── static/                      # Static files (CSS, JS)
├── db.sqlite3                   # Database file
├── manage.py                    # Django management script
└── README.md
```

## Usage

1. **Register a new account** or login with existing credentials
2. **Create projects** (if you have manager or admin role)
3. **Add tasks** to projects and assign them to users
4. **View dashboard** for project and task statistics
5. **Update task status** as work progresses
6. **Manage users** (admin only) through the admin panel

## API Endpoints

The application provides the following main endpoints:

- `/` - Home page
- `/register/` - User registration
- `/login/` - User login
- `/logout/` - User logout
- `/dashboard/` - User dashboard with charts
- `/projects/` - Project list and management
- `/tasks/` - Task list and management
- `/admin/` - Django admin panel

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License.

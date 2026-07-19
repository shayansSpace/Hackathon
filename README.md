# Campus Book & Lab Equipment Exchange System

A streamlined, full-stack Django web application designed to help students seamlessly exchange academic resources. The platform features a dual-flow architecture allowing users to either search for items they need (**Seek**) or list items they want to distribute (**Offer**), utilizing locked-in department-specific engineering categorizations.

🔗 **Live Deployment:** [View the Live App on Railway](https://determined-charm-production-616b.up.railway.app/)

---

## 🚀 Features

*   **Dynamic Dual-Flow Interface:** Manages both resource discovery and item listing workflows within a single, state-aware HTML view using unified template routing.
*   **Targeted Department Dropdowns:** Replaces prone-to-error text fields with a strict, validation-friendly dropdown selection covering core academic departments:
    *   `CIS` (Computer Systems Engineering)
    *   `EL` (Electronics Engineering)
    *   `EE` (Electrical Engineering)
    *   `ME` (Mechanical Engineering)
    *   `ENL` (English Linguistics)
*   **Safe Database Commits:** Implements server-side intercepted form processing using Django's `commit=False` save method, guaranteeing data integrity and fallback values for automated tracking fields.
*   **PaaS Optimized Architecture:** Fully configured for production environments, utilizing efficient web service routing suited perfectly for continuous hosting environments.

---

## 🛠️ Tech Stack

*   **Backend Framework:** Python / Django
*   **Database:** SQLite (Development) / PostgreSQL compatible (Production)
*   **Frontend Rendering:** HTML5 / Django Template Language (DTL)
*   **Production WSGI Server:** Gunicorn

---

## 💻 Local Development Setup

Follow these steps to pull down the project and run it locally:

### Prerequisites
*   Python 3.8 or higher installed on your machine.

### Installation Steps

1. **Clone the Repository:**
   ```
   git clone [https://github.com/your-username/your-repo-name.git](https://github.com/shayansSpace/Hackathon)
   cd Hackathon
1. Set Up a Virtual Environment:
Bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/activate

2. Install Core Dependencies:
Bash
pip install -r requirements.txt

3. Initialize Database Tables:
Compile the database schema instructions and migrate them into your local database tracker:
Bash
python manage.py makemigrations
python manage.py migrate

4. Run the Server:
Bash
python manage.py runserver
Navigate to http://127.0.0.1:8000/ in your browser to test the local system.

🌐 Railway Cloud Deployment Configuration
This project is optimized for automated cloud deployments. When connecting your repository to Railway, use the following specifications:

Environment Variables: Add your production secrets (e.g., SECRET_KEY, DEBUG=False) under the Variables settings tab in Railway.

Build Command Chaining: Configure Railway to execute migrations and static aggregation step-by-step during construction:

Bash
pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput
Start Command: Tell the platform to launch using the production-ready WSGI web server container instead of the development runtime:

Bash
gunicorn your_project_name.wsgi:application

👥 Engineering & Development Team
Backend & Systems Architecture: [Shayan Ahmed]

Project Teammates & Collaborators: Abdur Rehman Khalid, Danish Khan
---

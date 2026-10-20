# Job Application Tracker 📋

A Python-based web application to help job seekers organize, track, and manage their job applications in one place.

## Overview

The Job Application Tracker allows users to record job applications, monitor their application status, and view their job-search progress through a dashboard.

This project was developed as a hands-on learning project to practice Python programming, database operations, and web application development.

## Features

- **Add applications:** Record company name, job role, location, application date, job link, and notes.
- **Dashboard:** View total applications, applications submitted, interviews, and offers.
- **Status chart:** Visualize application progress using a bar chart.
- **Filter applications:** Filter records by application status.
- **Manage applications:** View saved records and delete applications with confirmation.
- **Persistent storage:** Store application data in a local SQLite database.

## Technologies Used

- Python
- Streamlit
- SQLite
- Pandas

## Project Structure

```text
job-tracker-project/
├── app.py
├── database.py
├── requirements.txt
├── README.md
└── .gitignore
```

The `jobs.db` database file is created locally when the application runs.

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd job-tracker-project
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your repository's actual URL.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the application

```bash
python -m streamlit run app.py
```

Open the local URL displayed in your terminal.

## What I Learned

- Building interactive web applications using Streamlit.
- Creating and managing SQLite database tables.
- Performing database operations using SQL queries.
- Separating database logic from application interface code.
- Displaying and filtering tabular data with Pandas.
- Creating dashboard metrics and charts.
- Validating user input and confirming destructive actions.

## Future Improvements

- Add application editing functionality.
- Add search by company name or job role.
- Add resume uploads for each application.
- Add email notifications for new job opportunities.
- Deploy the application online.

## Author

Developed as a personal portfolio project to strengthen Python development skills.
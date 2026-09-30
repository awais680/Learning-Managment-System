# 📚 LMS REST API (11th & 12th Grade Learning Management System)

A lightweight and robust RESTful API built with *Django REST Framework (DRF)* designed to manage course content for 11th and 12th-grade students. It features nested serialization for course lessons, custom endpoints for class filtering, and dynamic user enrollment.

---

## 🚀 Features

- 🎯 *Class-Based Filtering*: Easy access to courses filtered specifically by 11th or 12th class levels.
- 📖 *Nested Lessons/Chapters*: Fetches chapters and content directly nested within each subject.
- 🔒 *User Enrollment*: Secure endpoint for authenticated students to enroll in their chosen subjects.
- 🛡️ *Dynamic Permissions*: Restricts enrollment views so logged-in students can only access their own registrations.
- ⚡ *DRF Browsable UI*: Interactive web views for easy testing and endpoint verification.

---

## 🛠️ Tech Stack

- *Backend Framework*: Python 3, Django
- *API Framework*: Django REST Framework (DRF)
- *Database*: SQLite3
- *Authentication*: Session Authentication / DRF Inbuilt Auth

---

## 📌 API Endpoints Overview

| Method | Endpoint | Description | Access |
| :--- | :--- | :--- | :--- |
| *GET* | /school/courses/ | List all available courses/subjects | Public |
| *GET* | /school/courses/11th/ | List Class 11th courses | Public |
| *GET* | /school/courses/12th/ | List Class 12th courses | Public |
| *GET* | /school/courses/<id>/ | View course details along with nested lessons | Public |
| *GET* | /school/lessons/<id>/ | Read specific chapter/lesson notes | Public |
| *GET* | /school/enrollments/ | View logged-in student's enrollments | Authenticated |
| *POST* | /school/enrollments/ | Enroll current user into a course | Authenticated |

---

## ⚙️ Quick Setup & Local Run

1. *Clone the Repository*:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/lms_project.git](https://github.com/lms_project/lms_project.git)
   cd lms_project
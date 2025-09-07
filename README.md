# 📖 Library Book Allocation System

A full-stack web app that allocates library books across branches based on **demand** and **capacity**.  
It uses Flask for the backend with two allocation strategies (**Brute Force & Balanced**) and a modern interactive frontend for easy visualization.

---

## ⚡ Demo

<p align="center">
  <img src="demo/website.gif" alt="Website Demo" width="600"/>
</p>

---

## 🚀 Features
### Frontend (HTML, CSS, JavaScript)
- Interactive UI to add book demand and branch capacities.
- Beautiful animated loader and modern responsive design.
- Displays allocation plans in a clean, visual format.
### Backend (Flask, Python)
- REST API for handling allocation requests.
- Implements two allocation algorithms (Brute Force & Balanced).
- Supports JSON input/output for easy integration.
### Styling
- Two themes included (dark glowing style + pastel gradient theme).
- Clean, user-friendly interface with dynamic updates.

---

## 🛠 Tech Stack
- Backend: Python, Flask, Flask-CORS
- Frontend: HTML, CSS, JavaScript
- Styling: Custom CSS (light & dark themes)
- Deployment: Runs locally with Flask server (port 3001)

---

## 🔮 Future Improvements
- User Authentication – Add login and roles (e.g., admin, librarian, branch manager) for secure access.
- Database Integration – Store book demand, branch capacities, and allocations in a database (SQLite/MySQL/PostgreSQL).
- Persistent Data – Keep demand/capacity records across sessions instead of resetting on refresh.
- Advanced Allocation Algorithms – Implement optimized strategies like:
   - Greedy + fairness constraints
   - Linear programming (e.g., with PuLP)
   - Machine learning–based predictions
- Export Options – Allow users to download allocation results as PDF, CSV, or Excel.
- Interactive Visualizations – Show charts/graphs for demand vs. capacity, allocation distribution, etc.
- Error Handling & Validation – More user-friendly messages for invalid inputs or missing data.
- Mobile-Friendly UI – Improve responsiveness for better experience on tablets/phones.
- Dark/Light Mode Toggle – Let users switch between themes.
- Demo Data Button – Pre-fill with example demand/capacity to quickly try the tool.
- Deployment – Host the app on a public server (Heroku, Render, or GitHub Pages + API backend).

---

## Run Locally
1. Start the backend:
   ```bash
   pip install flask flask-cors
   python server.py

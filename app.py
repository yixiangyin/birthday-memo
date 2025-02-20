import os
import sqlite3
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Database file path
DATABASE = "birthdays.db"

def get_db():
    """Open a new database connection"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Allows us to access columns by name
    return conn

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Add the user's entry into the database
        name = request.form.get("name")
        month = request.form.get("month")
        day = request.form.get("day")

        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO birthdays (name, month, day) VALUES (?, ?, ?)", (name, month, day))
        conn.commit()
        conn.close()

        return redirect("/")

    else:
        # Display the entries in the database on index.html
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM birthdays")
        birthdays = cursor.fetchall()
        conn.close()
        return render_template("index.html", birthdays=birthdays)

if __name__ == "__main__":
    app.run(debug=True)

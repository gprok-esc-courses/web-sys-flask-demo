from flask import Flask, render_template, jsonify, request, redirect
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect("company.db")
conn.execute("""CREATE TABLE IF NOT EXISTS services 
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT)
             """)

@app.route("/")
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    # services = ['Web Design', 'AI support', 'Server Maintenance', 'Mobile Development']
    db = sqlite3.connect("company.db")
    cursor = db.cursor()
    services = cursor.execute("SELECT * FROM services")
    return render_template('about.html', services=services)

@app.route("/api/services")
def api_services():
    db = sqlite3.connect("company.db")
    cursor = db.cursor()
    services = cursor.execute("SELECT * FROM services")
    return jsonify({"services": services.fetchall()})


@app.route("/add/service", methods=['GET', 'POST'])
def add_service():
    if request.method == 'POST':
        data = request.form
        service = data['service']
        db = sqlite3.connect("company.db")
        cursor = db.cursor()
        services = cursor.execute("INSERT INTO SERVICES (name) VALUES ('" + service + "')")
        db.commit()
        return redirect("/about")

    return render_template('add_service.html')



@app.route("/contact")
def contact():
    return render_template('contact.html')


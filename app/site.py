from flask import Flask, jsonify, render_template
import psycopg2
from dotenv import load_dotenv
import os
import subprocess
import ipaddress

# Load environment variables from .env
load_dotenv()

app = Flask(__name__, template_folder='/var/www/myapp/html')

# Get PostgreSQL credentials from the .env file
db_host = os.getenv('POSTGRES_HOST')
db_name = os.getenv('POSTGRES_DB')
db_user = os.getenv('POSTGRES_USER')
db_password = os.getenv('POSTGRES_PASSWORD')

# Connect to PostgreSQL
def connect_to_db():
    
    return psycopg2.connect(
        host=db_host,
        database=db_name,
        user=db_user,
        password=db_password
    )

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/B22')
def personal():
    return render_template('practice.html')

@app.route('/data')
def get_data():

    conn = connect_to_db()
    cursor = conn.cursor()
    
    sort_ip = "awk {'print $1'} /var/log/nginx/access.log | sort -u"
    output = [subprocess.run(sort_ip, shell=True, capture_output=True, text=True)]
    
    for ip in output:
        if bool(ipaddress.IPv4Address(ip)) == True:  
          cursor.execute(f"INSERT INTO webserver.ip (ip) VALUES ('{ip}');")
        else:
            print(f"This IP {ip} is not IPv4.")
    
    cursor.execute(f"SELECT * FROM webserver.ip LIMIT 100;")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(rows, sort_ip)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    
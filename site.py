from flask import Flask, jsonify, render_template
from flask_login import LoginManager
import psycopg2
from dotenv import load_dotenv
import os
import subprocess
import ipaddress
import re

# Load environment variables from .env
load_dotenv()

#3/12/2025 add login manger init - B
login_manager = LoginManager() 
app = Flask(__name__, template_folder='/var/www/myapp/html')


# Get PostgreSQL credentials from the .env file
db_host = os.getenv('POSTGRES_HOST')
db_name = os.getenv('POSTGRES_DB')
db_user = os.getenv('POSTGRES_USER')
db_password = os.getenv('POSTGRES_PASSWORD')
sudo = os.getenv('SUDO')
key = os.getenv('KEY')

#3/12 define secret after .env & login manager - b
app.secret_key(key)
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

class User:
    def 

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

#ONLY RUN TO UPDATE DB IP TABLE
# @app.route('/data')
# def get_data():

#     conn = connect_to_db()
#     cursor = conn.cursor()
    
#     sort_ip = f"echo {sudo} | sudo -S awk {{'print $1'}} /var/log/nginx/access.log | sort -u"
#     output = subprocess.run(sort_ip, shell=True, capture_output=True, text=True)
    
#     ip_list = re.split("\n", output.stdout)
#     ip_list.remove("")
#     for ip in ip_list:
#       if ipaddress.IPv4Address(ip):
#         cursor.execute(f"INSERT INTO webserver.ip (ip) VALUES ('{ip}');")
#       else:
#         print(f"This {ip} is not a valid IP address.")
           
    
#     cursor.execute(f"SELECT * FROM webserver.ip LIMIT 100;")
#     rows = cursor.fetchall()
#     cursor.close()
#     conn.close()
#     return jsonify(rows)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    

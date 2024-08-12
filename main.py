from flask import Flask, jsonify
from datetime import datetime
import socket
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
import os
from dotenv import load_dotenv

app = Flask(__name__)
auth = HTTPBasicAuth()
load_dotenv()


# Just Saving User and Password that will be used for login for my testing.
auth_user = os.getenv('AUTH_USER', 'user')
auth_password = os.getenv('AUTH_PASSWORD', 'password')

print(f"AUTH_USER: {auth_user}")
print(f"AUTH_PASSWORD: {auth_password}")

USERS = {
    auth_user: generate_password_hash(auth_password)
}

@auth.verify_password
def verify_password(username, password):
    if username in USERS:
        is_verified = check_password_hash(USERS.get(username), password)
        print(f"Username: {username}, Password: {password}, Verified: {is_verified}")
        return is_verified
    return False

@app.route('/info', methods=['GET'])
@auth.login_required
def get_timestamp():
    try:
        # Get current timestamp
        current_timestamp = datetime.now().isoformat()
        # Get hostname
        hostname = socket.gethostname()
        # Return as JSON response
        return jsonify({
            'timestamp': current_timestamp,
            'hostname': hostname
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

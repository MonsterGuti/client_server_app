import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
from .db import create_user, get_user_by_email, update_user
from .auth import verify_password, hash_password, is_valid_password, is_valid_email, is_valid_name

def load_html(template_name):
    path = os.path.join("..", "frontend", "templates", template_name)
    with open(path, "r") as f:
        return f.read()


class RegistrationHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/register":
            from .auth import create_captcha
            captcha = create_captcha()
            html_with_captcha = load_html("register.html").replace("{captcha}", captcha)
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(html_with_captcha.encode())

        elif self.path == "/login":
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(load_html("login.html").encode())

        elif self.path == "/logout":
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(load_html("logout.html").encode())

        elif self.path == "/profile":
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(load_html("profile.html").encode())

    def do_POST(self):
        def respond(message):
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(f"<h3>{message}</h3>".encode("utf-8"))

        if self.path == "/register":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length).decode()
            data = parse_qs(post_data)
            email = data.get("email", [""])[0]
            first_name = data.get("first_name", [""])[0]
            last_name = data.get("last_name", [""])[0]
            password = data.get("password", [""])[0]
            captcha_value = data.get("captcha_value", [""])[0]
            captcha_input = data.get("captcha_input", [""])[0]
            if captcha_value.upper() != captcha_input.upper():
                respond(f"Invalid captcha: {captcha_input}")
                return

            if not is_valid_email(email):
                respond("Invalid email!")
                return
            if not is_valid_password(password):
                respond("Invalid password!")
                return
            if not is_valid_name(first_name) or not is_valid_name(last_name):
                respond("Invalid first name or last name!")
                return
            if get_user_by_email(email):
                respond("Email already registered!")
                return
            password_hash = hash_password(password)
            create_user(email, first_name, last_name, password_hash)
            respond("User created successfully!")

        elif self.path == "/login":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length).decode()
            data = parse_qs(post_data)
            email = data.get("email", [""])[0]
            password = data.get("password", [""])[0]

            current_user = get_user_by_email(email)
            if not current_user:
                respond("User not found!")
                return
            if verify_password(password, current_user["password_hash"]):
                respond("Login successful!")
            else:
                respond("Invalid password!")

        elif self.path == "/profile":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length).decode()
            data = parse_qs(post_data)
            email = data.get("email", [""])[0]
            password = data.get("password", [""])[0]
            first_name = data.get("first_name", [""])[0]
            last_name = data.get("last_name", [""])[0]

            current_user = get_user_by_email(email)
            if not current_user:
                respond("User not found!")
                return

            if not is_valid_name(first_name) or not is_valid_name(last_name):
                respond("Invalid first name or last name!")
                return
            if not is_valid_password(password):
                respond("Invalid password!")
                return

            hashed_password = hash_password(password)
            update_user(email, first_name, last_name, hashed_password)
            respond("User updated successfully!")


def main():
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, RegistrationHandler)
    print("The server works on http://localhost:8000/register")
    httpd.serve_forever()

if __name__ == "__main__":
    main()


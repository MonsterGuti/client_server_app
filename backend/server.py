import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
from .db import create_user, get_user_by_email, update_user
from .auth import verify_password, hash_password, is_valid_password, is_valid_email, is_valid_name

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, "..", "frontend", "templates")

def load_html(template_name):
    """
    Load an HTML file from the template directory.
    :param template_name: Name of the HTML file.
    :return: The content of the HTML file as a string.
    """
    path = os.path.join(TEMPLATE_DIR, template_name)
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


class RegistrationHandler(BaseHTTPRequestHandler):
    """
    HTTP handler for client requests.
    Manages registration, login, logout, and profile.
    """

    def send_html(self, content, status=200):
        """Sends an HTML response to the client."""
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(content.encode("utf-8"))

    def do_GET(self):
        """Process GET request and return the corresponding HTML page."""
        if self.path == "/register":
            from .auth import create_captcha
            captcha = create_captcha()
            html_with_captcha = load_html("register.html").replace("{captcha}", captcha)
            self.send_html(html_with_captcha)

        elif self.path == "/login":
            self.send_html(load_html("login.html"))

        elif self.path == "/logout":
            self.send_html(load_html("logout.html"))

        elif self.path == "/profile":
            self.send_html(load_html("profile.html"))

    def do_POST(self):
        """Handle POST requests for register, login, and profile forms."""
        def respond(message):
            self.send_html(f"<h3>{message}</h3>")

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
    """
    Starts the HTTP server and waits for requests from the browser.
    """
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, RegistrationHandler)
    print("The server works on http://localhost:8000/register")
    httpd.serve_forever()

if __name__ == "__main__":
    main()
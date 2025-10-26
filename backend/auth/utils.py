import re
import hashlib
import string
import random

EMAIL_RE = re.compile(r"^[A-Za-z0-9._]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")

def is_valid_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    return bool(EMAIL_RE.match(email.strip()))

def is_valid_name(name: str) -> bool:
    if not isinstance(name, str):
        return False
    name = name.strip()
    if len(name) < 2 or len(name) > 50:
        return False
    return bool(re.fullmatch(r"[A-Za-zА-Яа-я\- ]+", name))

def is_valid_password(password: str) -> bool:
    if not isinstance(password, str):
        return False
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"\d", password):
        return False
    return True

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(password: str, hashed_password: str) -> bool:
    return hashed_password == hashlib.sha256(password.encode()).hexdigest()

def create_captcha(length = 6) -> str:
    all_symbols = string.ascii_uppercase + string.digits
    return ''.join(random.choices(all_symbols, k = length))
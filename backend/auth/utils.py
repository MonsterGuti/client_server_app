import re
import hashlib
import string
import random

EMAIL_RE = re.compile(r"^[A-Za-z0-9._]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")

def is_valid_email(email: str) -> bool:
    """
    Checks if the submitted email is valid.
    :param email: Email address to check.
    :return: True if the email is valid, False otherwise.
"""
    if not isinstance(email, str):
        return False
    return bool(EMAIL_RE.match(email.strip()))

def is_valid_name(name: str) -> bool:
    """
    Checks if the submitted name is valid.
    :param name: Name to check.
    :return: True if the name is valid, False otherwise.
    """
    if not isinstance(name, str):
        return False
    name = name.strip()
    if len(name) < 2 or len(name) > 50:
        return False
    return bool(re.fullmatch(r"[A-Za-zА-Яа-я\- ]+", name))

def is_valid_password(password: str) -> bool:
    """
    Checks if the submitted password is valid.
    :param password: Password to check.
    :return: True if the password is valid, False otherwise.
    """
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
    """
    Hash the submitted password.
    :param password: Password to hash.
    :return: Hashed password.
    """
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(password: str, hashed_password: str) -> bool:
    """
    Checks if the submitted password matches the hashed password.
    :param password: Password to check.
    :param hashed_password: Hashed password.
    :return: True if the password matches the hashed password, False otherwise.
    """
    return hashed_password == hashlib.sha256(password.encode()).hexdigest()

def create_captcha(length = 6) -> str:
    """
    Creates a random captcha.
    :param length: Captcha length.
    :return: Captcha.
    """
    all_symbols = string.ascii_uppercase + string.digits
    return ''.join(random.choices(all_symbols, k = length))
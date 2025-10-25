from auth import is_valid_email, is_valid_name, is_valid_password, hash_password, verify_password

def test_valid_email():
    assert is_valid_email("martin@gmail.com")
    assert is_valid_email("gogulanov.martin@abv.bg")

def test_invalid_email():
    assert not is_valid_email("")
    assert not is_valid_email("milenov.com")
    assert not is_valid_email("martin@bg")
    assert not is_valid_email("petrov@")
    assert not is_valid_email(None)
    assert not is_valid_email(123)

def test_valid_name():
    assert is_valid_name("Martin Gogulanov")
    assert is_valid_name("Martin")
    assert is_valid_name("Martin-Gogulanov")

def test_invalid_name():
    assert not is_valid_name("")
    assert not is_valid_name("05Martin")
    assert not is_valid_name("M")
    assert not is_valid_name(None)
    assert not is_valid_name(123)

def test_valid_password():
    assert is_valid_password("abc12345")
    assert is_valid_password("MyPassw0rd")

def test_invalid_password():
    assert not is_valid_password("short1")
    assert not is_valid_password("password")
    assert not is_valid_password("")
    assert not is_valid_password(None)
    assert not is_valid_password([])

def test_hash_and_verify_password():
    my_pass = "marti123"
    hashed_pass = hash_password(my_pass)
    assert verify_password(my_pass, hashed_pass)
    assert not verify_password("abc", hashed_pass)

def test_hash_returns_string():
    my_pass = "martin123"
    hashed_pass = hash_password(my_pass)
    assert isinstance(hashed_pass, str)
    assert len(hashed_pass) == 64

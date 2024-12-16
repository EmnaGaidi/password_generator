import pytest
import string  # Add this import
from password_generator import generate_password, show_passwords, passwords


@pytest.fixture(autouse=True)
def reset_passwords():
    passwords.clear()  # Reset the list before each test


def test_generate_password_default():
    password = generate_password()
    assert len(password) == 12
    assert any(c.isupper() for c in password)
    assert any(c.isdigit() for c in password)
    assert any(
        c in string.punctuation for c in password
    )  # Special characters should exist


def test_generate_password_no_special():
    password = generate_password(use_special=False)
    assert len(password) == 12
    assert all(c not in string.punctuation for c in password)


def test_generate_password_no_numbers():
    password = generate_password(use_numbers=False)
    assert len(password) == 12
    assert all(c not in string.digits for c in password)


def test_generate_password_no_special_no_numbers():
    password = generate_password(use_special=False, use_numbers=False)
    assert len(password) == 12
    assert all(c not in string.punctuation for c in password)
    assert all(c not in string.digits for c in password)


def test_generate_password_min_length():
    with pytest.raises(ValueError):
        generate_password(length=5)


def test_generate_password_exact_length():
    length = 20
    password = generate_password(length=length)
    assert len(password) == length


def test_generate_password_edge_cases():
    # Case: length == 6
    password = generate_password(length=6)
    assert len(password) == 6
    # Case: length == 10
    password = generate_password(length=10)
    assert len(password) == 10


def test_generate_password_with_large_length():
    password = generate_password(length=100)
    assert len(password) == 100
    assert any(c.isupper() for c in password)
    assert any(c.isdigit() for c in password)
    assert any(c in string.punctuation for c in password)


def test_show_passwords_empty():
    assert show_passwords() == "Aucun mot de passe généré pour l'instant."


def test_show_passwords_non_empty():
    generate_password()
    output = show_passwords()
    assert "1." in output
    assert len(output.splitlines()) == 1  # Only one password should exist


def test_show_passwords_multiple():
    generate_password()
    generate_password()
    output = show_passwords()
    assert "1." in output
    assert "2." in output
    assert len(output.splitlines()) == 2  # Two passwords should exist

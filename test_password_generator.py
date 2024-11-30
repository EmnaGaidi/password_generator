import pytest
from password_generator import generate_password, show_passwords, passwords


@pytest.fixture(autouse=True)
def reset_passwords():
    passwords.clear()  # Réinitialise la liste avant chaque test


def test_generate_password_default():
    password = generate_password()
    assert len(password) == 12
    assert any(c.isupper() for c in password)
    assert any(c.isdigit() for c in password)


def test_generate_password_no_special():
    password = generate_password(use_special=False)
    assert all(c not in "!@#$%^&*()" for c in password)


def test_generate_password_min_length():
    with pytest.raises(ValueError):
        generate_password(length=5)


def test_show_passwords_empty():
    assert show_passwords() == "Aucun mot de passe généré pour l'instant."


def test_show_passwords_non_empty():
    generate_password()
    assert "1." in show_passwords()

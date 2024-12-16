import pytest
from password_generator import (
    generate_password,
    show_passwords,
    check_password_strength,
    save_passwords_to_file,
    retrieve_password,
    passwords,
)
import string


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
    assert all(c not in string.punctuation for c in password)


def test_generate_password_no_numbers():
    password = generate_password(use_numbers=False)
    assert all(c not in string.digits for c in password)


def test_generate_password_min_length():
    with pytest.raises(ValueError):
        generate_password(length=5)


def test_generate_password_with_large_length():
    password = generate_password(length=100)
    assert len(password) == 100


def test_check_password_strength():
    assert check_password_strength("abc") == "Faible"  # Only length < 8
    assert check_password_strength("abcd1234") == "Moyenne"  # Length >= 8, has digits
    assert (
        check_password_strength("Abcd1234") == "Forte"
    )  # Length >= 8, has uppercase and digits
    assert (
        check_password_strength("Abcd1234!") == "Très Forte"
    )  # Length >= 8, has uppercase, digits, and special char


def test_show_passwords_empty():
    assert show_passwords() == "Aucun mot de passe généré pour l'instant."


def test_show_passwords_non_empty():
    generate_password()
    assert "1." in show_passwords()


def test_save_passwords_to_file(tmp_path):
    passwords.extend(["pass1", "pass2"])
    file = tmp_path / "passwords.txt"
    message = save_passwords_to_file(file)
    assert file.exists()
    assert "Les mots de passe ont été sauvegardés" in message
    with open(file) as f:
        lines = f.readlines()
        assert len(lines) == 2


def test_retrieve_password():
    passwords.extend(["pass1", "pass2"])
    assert retrieve_password(1) == "pass1"
    assert retrieve_password(2) == "pass2"
    with pytest.raises(IndexError):
        retrieve_password(3)

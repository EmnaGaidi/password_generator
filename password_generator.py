import secrets
import string

# Liste des mots de passe générés (stockage en mémoire)
passwords = []


def generate_password(length=12, use_special=True, use_numbers=True):
    if length < 6:
        raise ValueError(
            "La longueur du mot de passe doit être au moins de 6 caractères."
        )

    # Caractères disponibles
    chars = string.ascii_lowercase  # Lettres minuscules uniquement par défaut
    password = []

    # Ajout d'un caractère obligatoire pour chaque catégorie activée
    if use_numbers:
        chars += string.digits
        password.append(secrets.choice(string.digits))
    if use_special:
        chars += string.punctuation
        password.append(secrets.choice(string.punctuation))
    # Ajout d'au moins une lettre majuscule
    chars += string.ascii_uppercase
    password.append(secrets.choice(string.ascii_uppercase))

    # Compléter le mot de passe pour atteindre la longueur spécifiée
    password += [secrets.choice(chars) for _ in range(length - len(password))]
    secrets.SystemRandom().shuffle(password)  # Mélanger pour éviter un ordre prévisible

    password = "".join(password)
    passwords.append(password)
    return password


# Fonction pour afficher les mots de passe générés
def show_passwords():
    if not passwords:
        return "Aucun mot de passe généré pour l'instant."
    return "\n".join(f"{i + 1}. {pw}" for i, pw in enumerate(passwords))


# Menu principal
def main():
    print("Bienvenue dans le générateur de mots de passe sécurisé !")
    while True:
        print("\nOptions :")
        print("1. Générer un nouveau mot de passe")
        print("2. Afficher les mots de passe générés")
        print("3. Quitter")
        choice = input("Choisissez une option : ").strip()

        if choice == "1":
            try:
                length = int(input("Entrez la longueur du mot de passe (min 6) : "))
                use_special = (
                    input("Inclure des caractères spéciaux ? (oui/non) : ")
                    .strip()
                    .lower()
                    == "oui"
                )
                use_numbers = (
                    input("Inclure des chiffres ? (oui/non) : ").strip().lower()
                    == "oui"
                )
                password = generate_password(length, use_special, use_numbers)
                print(f"Mot de passe généré : {password}")
            except ValueError as e:
                print(f"Erreur : {e}")
        elif choice == "2":
            print("\nMots de passe générés :")
            print(show_passwords())
        elif choice == "3":
            print("Au revoir !")
            break
        else:
            print("Option invalide, veuillez réessayer.")


if __name__ == "__main__":
    main()

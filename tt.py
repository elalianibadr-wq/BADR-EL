import json
import os

FICHIER = "stagiaires.json"


# =========================
# Charger les stagiaires
# =========================
def charger_stagiaires():
    if not os.path.exists(FICHIER):
        return []

    try:
        with open(FICHIER, "r", encoding="utf-8") as fichier:
            return json.load(fichier)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


# =========================
# Sauvegarder les stagiaires
# =========================
def sauvegarder_stagiaires(stagiaires):
    with open(FICHIER, "w", encoding="utf-8") as fichier:
        json.dump(stagiaires, fichier, indent=4, ensure_ascii=False)


# =========================
# Générer un nouvel ID
# =========================
def nouvel_id(stagiaires):
    if not stagiaires:
        return 1

    return max(s["id"] for s in stagiaires) + 1


# =========================
# Ajouter un stagiaire
# =========================
def ajouter_stagiaire(stagiaires):
    print("\n--- Ajouter un stagiaire ---")

    nom = input("Nom : ").strip()
    prenom = input("Prénom : ").strip()
    age = input("Âge : ").strip()
    formation = input("Formation : ").strip()
    entreprise = input("Entreprise : ").strip()
    email = input("Email : ").strip()

    stagiaire = {
        "id": nouvel_id(stagiaires),
        "nom": nom,
        "prenom": prenom,
        "age": age,
        "formation": formation,
        "entreprise": entreprise,
        "email": email
    }

    stagiaires.append(stagiaire)
    sauvegarder_stagiaires(stagiaires)

    print("\n✅ Stagiaire ajouté avec succès !")


# =========================
# Afficher les stagiaires
# =========================
def afficher_stagiaires(stagiaires):
    print("\n--- Liste des stagiaires ---")

    if not stagiaires:
        print("Aucun stagiaire enregistré.")
        return

    for s in stagiaires:
        print("-" * 40)
        print(f"ID          : {s['id']}")
        print(f"Nom         : {s['nom']} {s['prenom']}")
        print(f"Âge         : {s['age']}")
        print(f"Formation   : {s['formation']}")
        print(f"Entreprise  : {s['entreprise']}")
        print(f"Email       : {s['email']}")


# =========================
# Rechercher un stagiaire
# =========================
def rechercher_stagiaire(stagiaires):
    print("\n--- Rechercher un stagiaire ---")

    recherche = input("Entrez le nom ou prénom : ").lower().strip()

    resultats = [
        s for s in stagiaires
        if recherche in s["nom"].lower()
        or recherche in s["prenom"].lower()
    ]

    if not resultats:
        print("❌ Aucun stagiaire trouvé.")
        return

    for s in resultats:
        print("-" * 40)
        print(f"ID         : {s['id']}")
        print(f"Nom        : {s['nom']} {s['prenom']}")
        print(f"Formation  : {s['formation']}")
        print(f"Entreprise : {s['entreprise']}")
        print(f"Email      : {s['email']}")


# =========================
# Modifier un stagiaire
# =========================
def modifier_stagiaire(stagiaires):
    print("\n--- Modifier un stagiaire ---")

    try:
        id_stagiaire = int(input("ID du stagiaire : "))
    except ValueError:
        print("❌ ID invalide.")
        return

    for s in stagiaires:
        if s["id"] == id_stagiaire:

            print("Laissez vide pour conserver l'ancienne valeur.")

            nom = input(f"Nom [{s['nom']}] : ").strip()
            prenom = input(f"Prénom [{s['prenom']}] : ").strip()
            age = input(f"Âge [{s['age']}] : ").strip()
            formation = input(f"Formation [{s['formation']}] : ").strip()
            entreprise = input(f"Entreprise [{s['entreprise']}] : ").strip()
            email = input(f"Email [{s['email']}] : ").strip()

            if nom:
                s["nom"] = nom

            if prenom:
                s["prenom"] = prenom

            if age:
                s["age"] = age

            if formation:
                s["formation"] = formation

            if entreprise:
                s["entreprise"] = entreprise

            if email:
                s["email"] = email

            sauvegarder_stagiaires(stagiaires)

            print("\n✅ Stagiaire modifié avec succès !")
            return

    print("❌ Stagiaire introuvable.")


# =========================
# Supprimer un stagiaire
# =========================
def supprimer_stagiaire(stagiaires):
    print("\n--- Supprimer un stagiaire ---")

    try:
        id_stagiaire = int(input("ID du stagiaire : "))
    except ValueError:
        print("❌ ID invalide.")
        return

    for s in stagiaires:
        if s["id"] == id_stagiaire:

            confirmation = input(
                f"Supprimer {s['prenom']} {s['nom']} ? (o/n) : "
            ).lower()

            if confirmation == "o":
                stagiaires.remove(s)
                sauvegarder_stagiaires(stagiaires)
                print("✅ Stagiaire supprimé.")
            else:
                print("Suppression annulée.")

            return

    print("❌ Stagiaire introuvable.")


# =========================
# Menu principal
# =========================
def menu():
    stagiaires = charger_stagiaires()

    while True:
        print("\n")
        print("=" * 45)
        print("       GESTION DES STAGIAIRES")
        print("=" * 45)
        print("1. Ajouter un stagiaire")
        print("2. Afficher les stagiaires")
        print("3. Rechercher un stagiaire")
        print("4. Modifier un stagiaire")
        print("5. Supprimer un stagiaire")
        print("6. Quitter")
        print("=" * 45)

        choix = input("Votre choix : ")

        if choix == "1":
            ajouter_stagiaire(stagiaires)

        elif choix == "2":
            afficher_stagiaires(stagiaires)

        elif choix == "3":
            rechercher_stagiaire(stagiaires)

        elif choix == "4":
            modifier_stagiaire(stagiaires)

        elif choix == "5":
            supprimer_stagiaire(stagiaires)

        elif choix == "6":
            print("👋 Au revoir !")
            break

        else:
            print("❌ Choix invalide.")


# =========================
# Lancement du programme
# =========================
if __name__ == "__main__":
    menu()
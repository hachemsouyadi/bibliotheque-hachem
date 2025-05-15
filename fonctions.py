def afficher_livres(bibliotheque):
    if not bibliotheque:
        print("📭 La bibliothèque est vide.")
    for livre in bibliotheque:
        statut = "✅ Lu" if livre["Lu"] else "❌ Non lu"
        print(f'{livre["ID"]}: {livre["Titre"]} - {livre["Auteur"]} ({livre["Année"]}) - {statut}')

def ajouter_livre(bibliotheque):
    titre = input("Titre : ")
    auteur = input("Auteur : ")
    annee = input("Année : ")
    identifiant = max([livre["ID"] for livre in bibliotheque], default=0) + 1
    nouveau_livre = {
        "ID": identifiant,
        "Titre": titre,
        "Auteur": auteur,
        "Année": int(annee),
        "Lu": False,
        "Note": None
    }
    bibliotheque.append(nouveau_livre)
    print("✅ Livre ajouté avec succès !")

def supprimer_livre(bibliotheque):
    try:
        id_livre = int(input("ID du livre à supprimer : "))
        for livre in bibliotheque:
            if livre["ID"] == id_livre:
                confirmation = input(f"Confirmer la suppression de '{livre['Titre']}' ? (o/n) : ")
                if confirmation.lower() == 'o':
                    bibliotheque.remove(livre)
                    print("🗑️ Livre supprimé.")
                else:
                    print("Suppression annulée.")
                return
        print("Livre non trouvé.")
    except ValueError:
        print("ID invalide.")

def rechercher_livre(bibliotheque):
    mot_cle = input("Mot-clé à rechercher (dans le titre ou l'auteur) : ").lower()
    resultats = [livre for livre in bibliotheque if mot_cle in livre["Titre"].lower() or mot_cle in livre["Auteur"].lower()]
    if resultats:
        for livre in resultats:
            print(f'{livre["ID"]}: {livre["Titre"]} - {livre["Auteur"]}')
    else:
        print("Aucun résultat trouvé.")

def marquer_comme_lu(bibliotheque):
    try:
        id_livre = int(input("ID du livre que vous avez lu : "))
        for livre in bibliotheque:
            if livre["ID"] == id_livre:
                livre["Lu"] = True
                note = input("Note sur 10 (facultatif) : ")
                if note:
                    try:
                        livre["Note"] = float(note)
                    except:
                        print("Note invalide.")
                print("📘 Livre marqué comme lu.")
                return
        print("Livre non trouvé.")
    except:
        print("Erreur d’entrée.")

def filtrer_livres(bibliotheque):
    etat = input("Voulez-vous afficher les livres 'lu' ou 'non lu' ? ").lower()
    if etat == "lu":
        livres = [l for l in bibliotheque if l["Lu"]]
    elif etat == "non lu":
        livres = [l for l in bibliotheque if not l["Lu"]]
    else:
        print("Entrée invalide.")
        return
    for livre in livres:
        print(f'{livre["ID"]}: {livre["Titre"]} - {livre["Auteur"]}')

def trier_livres(bibliotheque):
    print("1. Par année")
    print("2. Par auteur")
    print("3. Par note")
    choix = input("Choix : ")
    if choix == "1":
        livres = sorted(bibliotheque, key=lambda x: x["Année"])
    elif choix == "2":
        livres = sorted(bibliotheque, key=lambda x: x["Auteur"])
    elif choix == "3":
        livres = sorted(bibliotheque, key=lambda x: x["Note"] if x["Note"] else 0, reverse=True)
    else:
        print("Choix invalide.")
        return
    for livre in livres:
        note = livre["Note"] if livre["Note"] is not None else "-"
        print(f'{livre["ID"]}: {livre["Titre"]} - {livre["Auteur"]} ({livre["Année"]}) Note: {note}')

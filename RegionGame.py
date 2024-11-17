import random
import string

def quiz_regions():
    regions_cote_divoire = {
        "district_autonome_abidjan": "Abidjan",
        "district_autonome_yamoussoukro": "Yamoussoukro",
        "belier": "Toumodi",
        "ifou": "Daoukro",
        "n_zi": "Dimbokro",
        "sud_comoe": "Aboisso",
        "indénie_djuablin": "Abengourou",
        "agneby_tiassa": "Agboville",
        "la_me": "Adzopé",
        "grands_ponts": "Dabou",
        "san_pedro": "San-pédro",
        "gbokle": "Sassandra",
        "nawa": "Soubré",
        "gontougo": "Bondoukou",
        "bounkani": "Bouna",
        "hambol": "Katiola",
        "gbeleke": "Bouaké",
        "worodougou": "Séguéla",
        "bere": "Mankono",
        "bafing": "Touba",
        "tonkpi": "Man",
        "guemon": "Duékoué",
        "cavally": "Guiglo",
        "bagoue": "Boundiali",
        "tchologo": "Ferkessédougou",
        "poro": "Korhogo",
        "kabadougou": "Odienné",
        "folon": "Minignan",
        "goh": "Gagnoa",
        "loh_djiboua": "Divo",
        "haut_sassandra": "Daloa",
        "marahoue": "Bouaflé"
    }

    # Liste pour stocker les meilleurs scores
    best_scores = []
    while True:
        # Affichage des 5 meilleurs scores au début
        print("\n=== Les 5 meilleurs scores ===")
        if not best_scores:
            print("Pas encore de scores enregistrés.")
        else:
            for score in sorted(best_scores, reverse=True)[:5]:
                print(f"{score}/100")

        # Commencer une nouvelle partie
        print("\n=== Nouvelle Partie ===")
        score = 0
        good = 0
        # Sélection de 10 questions aléatoires
        questions = random.sample(list(regions_cote_divoire), 10)

        for key in questions:
            reponse = input(f"\nQuel est le chef-lieu de la région {key} ? ").strip()
            if string.capwords(reponse) == regions_cote_divoire[key]:
                print("Bonne réponse! \U0001F60A")
                score += 10
                good += 1
            else:
                print(f"Réponse incorrecte \U0001F622")
                print(f"Le chef-lieu de {key} est {regions_cote_divoire[key]}")

        print("\n=== Partie Terminée ===")
        print(f"Vous avez obtenu {good} réponse(s) correcte(s) sur 10.")
        print(f"Score: {score} points")

        # Ajouter le score à la liste des meilleurs scores
        best_scores.append(score)

        # Demander si le joueur veut rejouer
        rejouer = input("\nVeux-tu essayer une autre partie ? (o/n) : ").strip().lower()
        if rejouer != 'o':
            print("Merci d'avoir joué ! À bientôt !")
            break

quiz_regions()

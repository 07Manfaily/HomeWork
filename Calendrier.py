def afficher_calendrier(nombre_jours):
    print("LUN MAR MER JEU VEN SAM DIM")
    jour = 1
    while jour <= nombre_jours:
        ligne = ""
        for i in range(7):  # 7 jours par semaine
            if jour <= nombre_jours:
                ligne += f"{jour:3d} "
                jour += 1
        print(ligne)

# Demande et validation du nombre de jours
while True:
    try:
        n = int(input("Entrez le nombre de jours du moi : "))
        if 27 <= n <= 31:
            afficher_calendrier(n)
            break
        else:
            print("Erreur : Le nombre de jours doit être entre 27 et 31.")
    except ValueError:
        print("Erreur : Veuillez entrer un nombre valide.")
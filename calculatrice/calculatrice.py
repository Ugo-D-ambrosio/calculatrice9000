def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        raise ValueError("Division par zéro")

def calculatrice():
    historique = []

    while True:
        try:

            nombre1 = input("Entrez le premier nombre (ou 'q' pour quitter) : "))

            # quitter la calculatrice
            if nombre1 == 'q':
                break

            operateur = input("Entrez l'opérateur (+, -, *, /) : ")
            nombre2 = float(input("Entrez le deuxième nombre : "))
            
            if operateur == '+':
                resultat = addition(nombre1, nombre2)
            elif operateur == '-':
                resultat = soustraction(nombre1, nombre2)
            elif operateur == '*':
                resultat = multiplication(nombre1, nombre2)
            elif operateur == '/':
                resultat = division(nombre1, nombre2)
            else:
                raise ValueError("Opérateur non valide")

            # resultat
            print(f"Le résultat de {nombre1} {operateur} {nombre2} est : {resultat}")

            historique.append(f"{nombre1} {operateur} {nombre2} = {resultat}")

        except ValueError as e:
            print(f"Erreur : {e}")
        except Exception as e:
            print(f"Une erreur inattendue s'est produite : {e}")

    # historique
    print("\nHistorique des opérations :")
    for operation in historique:
        print(operation)

calculatrice()

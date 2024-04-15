import itertools

def truth_table(boolean_function):
    # Extraire les variables de la fonction logique
    variables = sorted(set(boolean_function.replace('not', '').replace('and', '').replace('or', '').replace('(', '').replace(')', '').split()))
    num_variables = len(variables)
    
    # En-tête de la table de vérité
    table_header = ' | '.join(variables) + ' | ' + boolean_function
    table_separator = '-' * len(table_header)

    print("Table de vérité:")
    print(table_header)
    print(table_separator)

    # Générer et évaluer chaque combinaison de valeurs booléennes pour les variables
    truth_table_values = []
    for combination in itertools.product([False, True], repeat=num_variables):
        variable_dict = {variables[i]: combination[i] for i in range(num_variables)}
        boolean_value = eval(boolean_function, variable_dict)
        truth_values = ' | '.join(str(int(comb)) for comb in combination) + ' | ' + str(int(boolean_value))
        print(truth_values)
        truth_table_values.append(combination + (boolean_value,))
    
    # Formes canoniques
    print("\nFormes canoniques:")
    minterms = [idx for idx, value in enumerate(truth_table_values) if value[-1] == 1]
    maxterms = [idx for idx, value in enumerate(truth_table_values) if value[-1] == 0]
    
    print("Forme canonique en somme de produits (SOP):")
    sop_terms = [''.join(['' if value == 1 else f"not {variables[idx]}" for idx, value in enumerate(comb)]) for comb in truth_table_values if comb[-1] == 1]
    print(" + ".join(sop_terms))
    
    print("\nForme canonique en produit de sommes (POS):")
    pos_terms = ['('.join(['' if value == 0 else f"not {variables[idx]}" for idx, value in enumerate(comb)]) + ')' for comb in truth_table_values if comb[-1] == 0]
    print(" * ".join(pos_terms))

# Demander à l'utilisateur la fonction logique
boolean_function = input("Veuillez entrer la fonction logique (utilisez 'not', 'and', 'or', et les parenthèses pour la syntaxe): ")

# Afficher la table de vérité et les formes canoniques
truth_table(boolean_function)
 
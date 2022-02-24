from calculate_score import calculate_score
from random import sample

def run_algo(clients, ingredients_map):
    best_pizza = list(ingredients_map.keys())
    best_score = 0
    tentative = 0
    while tentative < len(ingredients_map)*10:
        pizza = best_pizza.copy()
        ings_del = sample(pizza, min(len(pizza), 1))
        for ing_del in ings_del:
            pizza.remove(ing_del)
        score = calculate_score(set(pizza),clients)
        if score >= best_score:
            best_score = score
            best_pizza = pizza 
        tentative += 1
    return best_pizza
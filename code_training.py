import numpy as np
import pandas as pd

filepaths = [
    'e.txt'
]


def score(pizza_ingredients, preferences):
    res = 0
    for _, p in preferences.items():
        ok = True
        for like in p['likes']:
            if like not in pizza_ingredients:
                ok = False
                break
        if not ok:
            continue
        for dislike in p['dislikes']:
            if dislike in pizza_ingredients:
                ok = False
                break
        if ok:
            res += 1
    return res


def run_algo(filepath, output_filepath):
    file1 = open(filepath, 'r')
    lines = file1.readlines()
    clients_number = 0
    preferences = {}
    ingredients = set()
    ingredient_by_customer = {}

    header = lines[0].split()
    clients_number = int(header[0])

    customer_id = 0
    for line_index in range(1, clients_number*2, 2):
        likes = lines[line_index].split()[1:]
        dislikes = lines[line_index+1].split()[1:]

        preferences[customer_id] = {
            "likes": likes,
            "dislikes": dislikes
        }

        for l in likes:
            if l not in ingredients:
                ingredients.add(l)

            if l not in ingredient_by_customer:
                ingredient_by_customer[l] = clients_number*[0]

            ingredient_by_customer[l][customer_id] = 1

        for d in dislikes:
            if d not in ingredients:
                ingredients.add(d)

            if d not in ingredient_by_customer:
                ingredient_by_customer[d] = clients_number*[0]

            ingredient_by_customer[d][customer_id] = -1

        customer_id += 1

    df = pd.DataFrame(data=ingredient_by_customer)
    # nobody likes these ingredients
    subset_df = df.loc[:, (df == 1).any()]

    # ingredients everybody appreciates
    appreciated = subset_df.loc[:, ~(subset_df == -1).any()]
    final_pizza = {*list(appreciated.columns)}

    subset_df = subset_df.loc[:, (subset_df == -1).any()]

    while len(subset_df) > 0:
        # most liked ingredients
        summed = subset_df.sum()
        max_score = summed.max()
        print("max_score", max_score)
        print("len summed", len(summed))
        print("-"*100)
        most_likeds = subset_df.loc[:, summed >= max_score].columns
        if len(most_likeds) > 0:
            most_liked = most_likeds[0]

            if (max_score > 0):
                final_pizza.add(most_liked)
                # delete clients that do not like this ingredient
                subset_df = subset_df[subset_df[most_liked] != -1]

            # delete most_liked ingredient
            del subset_df[most_liked]
        else:
            break

    final_pizza = {*final_pizza, *list(subset_df.columns)}

    file1 = open(output_filepath, 'w')
    file1.writelines(f"{len(final_pizza)} {' '.join(final_pizza)}")

    print("score", score(final_pizza, preferences))


for filepath in filepaths:
    print("Running on: ", filepath)
    run_algo(filepath, filepath+'.out')

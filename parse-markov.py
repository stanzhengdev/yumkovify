from collections import defaultdict
import os
import markovify
import json

models = {
    'NAME_MODEL': 'models/name.json',
    'INGREDIENT_MODEL': 'models/ingredient.json'
}


def files_exist():
    check = [i for i in models.values() if os.path.exists(i)]
    return True if len(check) == 2 else False

def write_json(path, data):
    with open(path, 'w') as f:
        f.write(data)

def open_file(path):
    with open(path) as data:
        return json.load(data)


def train(filename):
    if files_exist():
        with open(filename) as data:
            recipe_data = json.load(data)

            names = defaultdict(list)
            ingredients = defaultdict(list)

            # format data
            names = ' '.join([i['name'] for i in recipe_data])
            ingredients = ' '.join([' '.join(r['ingredients'].split('\n')) for r in recipe_data])
            # create models
            name_model = markovify.Text(names)
            ingredients_model = markovify.Text(ingredients)

            write_json(models['NAME_MODEL'], name_model.chain.to_json())
            write_json(models['INGREDIENT_MODEL'], ingredients_model.chain.to_json())

            return [name_model, ingredients_model]
    else:
        return [markovify.Chain.from_json(open_file(m)) for m in models.values()]



if __name__ == '__main__':
        name_model, recipe_model =  train('recipeitems-latest.json')
        # print(name_model.make_short_sentence(100))
        # print(recipe_model.make_sentence())


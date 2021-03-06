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

def load_json(path):
    with open(path) as data:
        return json.load(data)

def format_recipe(name, recipe):
    return """
{name}
-----
{recipe}
""".format(name=name, recipe=recipe)

def largest_word(sentence):
    """Determines the largest word in a sentence"""
    word = ''
    for w in sentence.split():
        if len(w) > len(word):
           word = w
    return word


def train(filename):
    if not files_exist():
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
        return [markovify.Text.from_chain(load_json(models['NAME_MODEL'])),
                markovify.Text.from_chain(load_json(models['INGREDIENT_MODEL']))
        ]

if __name__ == '__main__':
        name_model, recipe_model =  train('recipeitems-latest.json')

        # model_combo = markovify.combine([ name_model, recipe_model  ], [ 1.5, 1 ])
        for i in range(10):
            name = name_model.make_short_sentence(140)
            recipe = recipe_model.make_sentence()
            print(format_recipe(name, recipe))




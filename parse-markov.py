from collections import defaultdict
import markovify
import json

if __name__ == '__main__':
    with open('recipeitems-latest.json') as data:
        recipe_data = json.load(data)
        ingredients = defaultdict(list)
        names = {list}
        # recipes =
        names = ' '.join([i['name'] for i in recipe_data])
        recipes = ' '.join([' '.join(r['ingredients'].split('\n')) for r in recipe_data])

        # name model
        name_model = markovify.Text(names)
        recipe_model = markovify.Text(recipes)
        for i in range(5):
            # print(name_model.make_short_sentence(100))
            # print(recipe_model.make_sentence())
            print('\n\n')

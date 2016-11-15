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
        name_model = markovify.Text(names)
        recipe_model = markovify.Text(recipes)
        chain1 = []
        chain2 = []
        for i in range(100):
            c1 = name_model.make_short_sentence(100)
            c2 = name_model.make_sentence()
            if c1:
                chain1.append(c1)
            if c2:
                chain2.append(c2)

        print('Chain1: ', len(chain1))
        print('Chain2: ', len(chain2))
from flask import Flask, request, jsonify, send_from_directory
import openai
import os

app = Flask(__name__)

openai.api_key = 

@app.route('/')
def home():
    return send_from_directory('static', 'reciprepper.html')

@app.route('/expand', methods=['POST'])
def expand():
    recipe = request.json['recipe']
    expanded_recipe = expand_recipe_with_gpt(recipe)
    return jsonify(expandedRecipe=expanded_recipe)

def expand_recipe_with_gpt(recipe):
        prompt = f"You are an expert chef that parses poorly written recipes that need to be expanded, reorganized, and reformatted, and you return a perfect thorough recipe that anticipates any problems that a novice chef might have. You include all preparatory steps, add steps to combine ingredients logically, add thorough and specific steps for mise en place, and split all complex steps into as many as needed for ease of execution. Caveats: If ingredients or spices go into the pan at the same time, they can be combined during the preparatory stages. Do not include anything in your response beyond the ingredients list, the preparation steps, the mise en place steps, and the expanded cooking steps, in that order. Recipe:\n{recipe}"

        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages = [{'role': 'user', 'content': prompt}], max_tokens=2048)


        expanded_recipe = response['choices'][0]['message']['content']
        return expanded_recipe

if __name__ == '__main__':
    app.run(debug=True)


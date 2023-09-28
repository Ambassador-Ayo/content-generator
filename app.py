import os
from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Replace with your OpenAI API key
openai.api_key = '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'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_content():
    if request.method == 'POST':
        if 'input_text' in request.form:
            user_input = request.form['input_text']
            # Rest of your code
        else:
            return "No 'input_text' in the form data."

        # Make a request to OpenAI for content generation
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=user_input,
            max_tokens=150
        )   

        generated_text = response.choices[0].text

        return generated_text

if __name__ == '__main__':
    app.run(debug=True)

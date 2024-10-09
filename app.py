from flask import Flask, render_template, request, jsonify
import random
import string

app = Flask(__name__)

def generate_password(length, uppercase, lowercase, numbers, symbols):
    characters = ""
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if numbers:
        characters += string.digits
    if symbols:
        characters += string.punctuation
    
    if characters == "":
        return ""
    
    password = ''.join(random.choice(characters) for i in range(length))
    return password

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    length = data.get('length', 8)
    uppercase = data.get('uppercase', True)
    lowercase = data.get('lowercase', True)
    numbers = data.get('numbers', False)
    symbols = data.get('symbols', False)

    password = generate_password(length, uppercase, lowercase, numbers, symbols)
    return jsonify({'password': password})

if __name__ == '__main__':
    app.run(debug=True)

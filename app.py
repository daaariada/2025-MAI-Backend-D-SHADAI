import random
import string
from flask import Flask, jsonify

app = Flask(__name__)

def generate_password():
    # Минимальная и максимальная длина
    length = random.randint(8, 16)
    
    # Все возможные символы
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = '#.,!@&^%*'
    
    # Гарантируем минимум по 1 символу из каждой группы
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special)
    ]
    
    # Заполняем оставшиеся символы случайным выбором из всех групп
    all_chars = lowercase + uppercase + digits + special
    password += random.choices(all_chars, k=length - 4)
    
    # Перемешиваем символы
    random.shuffle(password)
    
    return ''.join(password)

@app.route('/generate-password')
def get_password():
    return jsonify({"password": generate_password()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
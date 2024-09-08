from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Função para criar e conectar ao banco de dados
def criar_banco():
    conn = sqlite3.connect('pets.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS pets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL,
        peso REAL NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

# Função para inserir o pet no banco
def inserir_pet(nome, idade, peso):
    conn = sqlite3.connect('pets.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO pets (nome, idade, peso) VALUES (?, ?, ?)
    ''', (nome, idade, peso))
    conn.commit()
    conn.close()

# Rota para o formulário
@app.route('/')
def formulario():
    return render_template('form.html')

@app.route('/consulta_pets')
def consulta_pets():
    conn = sqlite3.connect('pets.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM pets')
    pets = cursor.fetchall()
    conn.close()
    return render_template('consulta_pets.html', pets=pets)

# Rota para adicionar pet ao banco
@app.route('/add_pet', methods=['POST'])
def add_pet():
    nome = request.form['nome']
    idade = int(request.form['idade'])
    peso = float(request.form['peso'])

    # Inserir no banco
    inserir_pet(nome, idade, peso)
    return redirect('/')

if __name__ == '__main__':
    criar_banco()  # Cria o banco se não existir
    app.run(debug=True)

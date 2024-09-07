import sqlite3

# Função para coletar informações sobre o pet
def coletar_informacoes_pet():
    print("Por favor, insira as informações sobre seu pet.")

    # Coleta do nome do pet
    nome = input("Nome do pet: ")

    # Coleta da idade do pet, garantindo que seja um número inteiro
    while True:
        try:
            idade = int(input("Idade do pet (em anos): "))
            if idade < 0:
                print("A idade não pode ser negativa. Tente novamente.")
            else:
                break
        except ValueError:
            print("Por favor, insira um número válido para a idade.")

    # Coleta do peso do pet, garantindo que seja um número flutuante
    while True:
        try:
            peso = float(input("Peso do pet (em kg): "))
            if peso < 0:
                print("O peso não pode ser negativo. Tente novamente.")
            else:
                break
        except ValueError:
            print("Por favor, insira um número válido para o peso.")

    # Exibindo as informações coletadas
    print("\nInformações do pet:")
    print(f"Nome: {nome}")
    print(f"Idade: {idade} anos")
    print(f"Peso: {peso} kg")

    #Inserir dados no banco de dados
    inserir_pet(nome, idade, peso)
    print("As informações do pet foram salvas com sucesso no banco de dados.")

def criar_banco():
    conn = sqlite3.connect('pets.db')
    cursor = conn.cursor()

    #
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS pets(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL,
        peso REAL NOT NULL
    )                      
    ''')

    conn.commit()
    conn.close()

def inserir_pet(nome, idade, peso):
    conn = sqlite3.connect('pets.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO pets (nome, idade, peso) VALUES (?, ?, ?)
    ''', (nome, idade, peso))

    conn.commit()
    conn.close()

def exibir_pets():
    conn = sqlite3.connect('pets.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM pets')
    pets = cursor.fetchall()

    if pets:
        print("\nPets cadastrados:")
        for pet in pets:
            print(f"ID: {pet[0]}, Nome: {pet[1]}, Idade: {pet[2]} anos, Peso: {pet[3]} kg")
    else:
        print("\nNenhum pet cadastrado.")

    conn.close()

#Criar o Banco de Dados local
criar_banco()

# Chama a função para coletar e exibir as informações do pet
coletar_informacoes_pet()

#c#exibir todos os pets cadastrados
exibir_pets()

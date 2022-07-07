from flask import Flask, render_template, request


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = Jogo('Tetris', 'Puzzel', 'Atari')
jogo2 = Jogo('God of War', 'Rack and Slach', 'PS2')
jogo3 = Jogo('Mortal Kombat', 'Luta', 'PS2')
lista = [jogo1,jogo2, jogo3]

app = Flask(__name__)

#para colocar uma aplicação precisamos criar uma rota e sempre é necessario colar uma função
@app.route('/inicio')
def ola():
    #para conectar ao arquivo HTML
    #O titulo é a variavel criada no html para que possamos mudar o html no python
    return render_template('lista.html', titulo = 'Jogos', jogos = lista )

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo = 'Novo Jogo')

@app.route('/criar')
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return render_template('lista.html', titulo = 'jogos', jogos = lista)



#isso faz rodar a apricação
app.run()

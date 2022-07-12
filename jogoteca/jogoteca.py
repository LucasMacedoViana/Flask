from flask import Flask, render_template, request, redirect, session, flash


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
app.secret_key = 'alura'

#para colocar uma aplicação precisamos criar uma rota e sempre é necessario colar uma função
@app.route('/')
def index():
    #para conectar ao arquivo HTML
    #O titulo é a variavel criada no html para que possamos mudar o html no python
    return render_template('lista.html', titulo = 'Jogos', jogos = lista )

@app.route('/novo' )
def novo():
    return render_template('novo.html', titulo = 'Novo Jogo')

@app.route('/criar', methods = ['POST', ])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods = ['POST', ])
def autenticar():
    if 'alohomora' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(session['usuario_logado'] + 'Usuario logado com sucesso!')
        return redirect('/')
    else:
        flash('Usuario não logado')
        return redirect('/login')





app.run(debug=True)

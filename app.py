
import pymysql
from flask import Flask, render_template, request, redirect, session, url_for
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
import os
from dotenv import load_dotenv

pymysql.install_as_MySQLdb()

app = Flask(__name__)
load_dotenv()

app.secret_key = os.getenv("SECRET_KEY")

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'  # ou 'rafac', dependendo do que você criou
app.config['MYSQL_PASSWORD'] = '0705'
app.config['MYSQL_DB'] = 'amorzinho_rede'


mysql = MySQL(app)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome_casal = request.form['nome_casal']

        nome1 = request.form['nome1']
        email1 = request.form['email1']
        senha1 = generate_password_hash(request.form['senha1'])

        nome2 = request.form['nome2']
        email2 = request.form['email2']
        senha2 = generate_password_hash(request.form['senha2'])

        cur = mysql.connection.cursor()

        # Criar o relacionamento
        cur.execute(
            "INSERT INTO relacionamentos (nome_casal) VALUES (%s)", (nome_casal,))
        mysql.connection.commit()
        relacionamento_id = cur.lastrowid

        # Inserir os dois usuários
        cur.execute("INSERT INTO usuarios (nome, email, senha, relacionamento_id) VALUES (%s, %s, %s, %s)",
                    (nome1, email1, senha1, relacionamento_id))
        cur.execute("INSERT INTO usuarios (nome, email, senha, relacionamento_id) VALUES (%s, %s, %s, %s)",
                    (nome2, email2, senha2, relacionamento_id))

        mysql.connection.commit()
        cur.close()

        return redirect(url_for('login'))

    return render_template('cadastro.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        cur = mysql.connection.cursor()
        cur.execute(
            "SELECT id, nome, senha, relacionamento_id FROM usuarios WHERE email = %s", (email,))
        usuario = cur.fetchone()
        cur.close()

        if usuario and check_password_hash(usuario[2], senha):
            session['usuario_id'] = usuario[0]
            session['nome'] = usuario[1]
            session['relacionamento_id'] = usuario[3]
            # ou redirecionar pra página principal do app
            return redirect(url_for('conversa'))
        else:
            return "Email ou senha incorretos"

    return render_template('login.html')


@app.route('/conversa', methods=['GET', 'POST'])
def conversa():
    if 'usuario_id' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        conteudo = request.form['mensagem']
        usuario_id = session['usuario_id']
        relacionamento_id = session['relacionamento_id']

        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO mensagens (conteudo, usuario_id, relacionamento_id) VALUES (%s, %s, %s)",
            (conteudo, usuario_id, relacionamento_id)
        )
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('conversa'))  # redireciona pra mesma rota

    # Agora sempre vai pegar as mensagens, independente do método
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT mensagens.conteudo, usuarios.nome, mensagens.data_envio
        FROM mensagens
        JOIN usuarios ON mensagens.usuario_id = usuarios.id
        WHERE mensagens.relacionamento_id = %s
        ORDER BY mensagens.data_envio ASC
    """, (session['relacionamento_id'],))
    mensagens = cur.fetchall()
    cur.close()

    cur = mysql.connection.cursor()
    cur.execute("SELECT nome_casal FROM relacionamentos WHERE id = %s",
                (session['relacionamento_id'],))
    nome_casal = cur.fetchone()[0]
    cur.close()
    return render_template('conversa.html', mensagens=mensagens, nome_casal=nome_casal)


if __name__ == "__main__":
    app.run(debug=True)

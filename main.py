from flask import Flask, render_template, request, redirect
app = Flask(__name__)

contatos = []


@app.route('/')
def index():
    return render_template('index.html', contatos = contatos)

@app.route('/adicionar_contato', methods=['GET', 'POST'])
def adicionar_contato():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']
        codigo = len(contatos)
        contatos.append([codigo, nome, email, telefone])
        return redirect('/')
    else:
        return render_template ('adicionar_contato.html')

@app.route('/editar_contato/<int:codigo>', methods=['GET', 'POST'])
def editar_contato():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']
        contatos[codigo] = [codigo, nome, email, telefone]
        return redirect('/')
    else:
        contato = contatos[codigo]
        return render_template('editar_contato.html', contato = contato)


if __name__ == '__main__':
    app.run(debug=True)
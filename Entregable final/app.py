from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/trivia')
def trivia():
    return render_template('trivia.html')

@app.route('/pedidos')
def pedidos():
    return render_template('pedidos.html')

@app.route('/usql')
def usql():
    return render_template('usql.html')

if __name__ == '__main__':
    app.run(debug=True)

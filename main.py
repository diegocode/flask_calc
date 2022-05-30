from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/suma/<n1>/<n2>')
def sumar(n1, n2):
    return render_template('resultado.html', 
                           resultado=float(n1) + float(n2), 
                           operacion=f'suma {n1} + {n2}')


@app.route('/producto/<n1>/<n2>')
def multiplicar(n1, n2):
    return render_template('resultado.html', 
                           resultado=float(n1) * float(n2), 
                           operacion=f'producto {n1} x {n2}')


@app.route('/potencia/<n1>')
@app.route('/potencia/<n1>/<n2>')
def elevar(n1, n2=2):
    return render_template('resultado.html', 
                           resultado=float(n1) ** float(n2), 
                           operacion=f'{n1} a la {n2}')


app.run(host='0.0.0.0', port=81)
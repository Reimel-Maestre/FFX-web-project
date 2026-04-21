from flask import Flask, render_template

app = Flask(__name__)

# --- RUTAS DE LA APLICACIÓN ---

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/spira')
def spira():
    return render_template('spira.html')

@app.route('/legado')
def legado():
    return render_template('legado.html')

@app.route('/biblioteca')
def biblioteca():
    return render_template('biblioteca.html')

if __name__ == '__main__':
    app.run(debug=False) 

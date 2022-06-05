from flask import Flask, request,render_template,views
from matplotlib.pyplot import get
from simulacion import Simulacion
# create the Flask app
app = Flask(__name__)

@app.route('/')
def inicio(): 
    return render_template('formulario.html')

@app.route('/procesar', methods=['POST'])
def procesar():
    nombre = request.form.get("nombre")
    edad = request.form.get("edad")
    faltas= request.form.get("faltas")
    laterales= request.form.get("laterales")    
    #simulacion = Simulacion()
    return render_template("index.html", nombre=nombre, edad=edad,faltas=faltas,laterales=laterales)

@app.route('/query-example')
def query_example():
    language = request.args.get('framework')

    return '''<h1>The language value is: {}</h1>'''.format(language)
    return 'Query String Example'

@app.route('/form-example')
def form_example():
    return 'Form Data Example'

@app.route('/json-example')
def json_example():
    return 'JSON Object Example'

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
from flask import Flask, request,render_template,views
from matplotlib.pyplot import get
#from simulacion2 import Simulacions
#from torneo import Torneo
# create the Flask app
app = Flask(__name__)

@app.route('/')
def inicio(): 
    return render_template('formulario.html')

@app.route('/procesar', methods=['POST'])
def procesar():
    eventosPosibles = []
    nombre = request.form.get("nombre")
    listas = request.form.get("lista")
    print("LISTAAAAAAAAAAAAAAAAAa",listas)
    #simulacion = Simulacion(eventosPosibles)
    #torneo= Torneo(cantidadEquipos=10,nombreTorneo="nombre")
    #simu=Simulacions(torneo) 
    #simu.simular()    
    return render_template("index.html", listas= listas)
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
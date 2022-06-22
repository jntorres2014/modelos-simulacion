from flask import Flask, request,render_template,views
from matplotlib.pyplot import get
from simulacion import Simulacion
from torneo import Torneo
import pandas as pd
import matplotlib.pyplot as plt
import base64
import io 

# create the Flask app
app = Flask(__name__)

@app.route('/')
def inicio(): 
    return render_template('formulario.html')

@app.route('/procesar', methods=['POST'])
def procesar():
    cantidadEquipos = int(request.form.get("cantidadEquipos"))
    nombreTorneo = request.form.get("nombreTorneo")
    listas = request.form.getlist("lista[]")
    torneo= Torneo(cantidadEquipos=cantidadEquipos,nombreTorneo=nombreTorneo)
    simu=Simulacion(torneo) 
    datosSimulacion,datos=simu.simular(listas,cantidadEquipos,1)
    simu.obtenerGrafico(datos)
    return render_template("index.html", datos= datosSimulacion)

@app.route('/query-example')
def query_example():
    language = request.args.get('framework')

    return '''<h1>The language value is: {}</h1>'''.format(language)
    return 'Query String Example'

@app.route('/graficar')
def form_example():
    #datosHtml=Torneo(request.args.get('arg1'))
    #print(type(datosHtml.items()))

    #print ("En teoria son los datos del torneo",datosHtml)
    img = io.BytesIO()
    datos = [52.958333333333336, 84.45833333333333, 41.75, 0.0, 87.58333333333333, 24.916666666666668, 10.791666666666666, 45.791666666666664, 0.0, 0.0]
    plt.clf() 
    plt.pie(datos, autopct="%0.1f %%")
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    return render_template('graficar.html', imagen={ 'imagen': [plot_url, plot_url] })    #return render_template("graficar.html")

@app.route('/json-example')
def json_example():
    return 'JSON Object Example'


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=4000)

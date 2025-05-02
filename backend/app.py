from flask import Flask
from tsp_solver import i_hill_climbing

app = Flask(__name__)

@app.route('/')
def resolver_tsp():
    ruta, distancia = i_hill_climbing()
    ruta_str = ' → '.join(ruta)
    return f"""
    <html>
        <head><title>Resultado TSP </title></head>
        <body>
            <h1>TSP con Hill Climbing Iterativo</h1>
            <p><strong>Ruta:</strong> {ruta_str}</p>
            <p><strong>Distancia total:</strong> {distancia:.2f}</p>
            <form method='get' action='/'>
                <button type='submit'>Volver a calcular</button>
            </form>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)

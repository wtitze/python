# https://towardsdatascience.com/how-to-easily-show-your-matplotlib-plots-and-pandas-dataframes-dynamically-on-your-website-a9613eff7ae3

from flask import Flask, render_template, send_file, make_response, url_for, Response
app = Flask(__name__)

import io
import geopandas as gpd
import contextily
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

countries = gpd.read_file('/workspace/python/countries.zip')
countries = countries[countries.name == 'Italy']

@app.route('/', methods=['GET'])
def hello_world():
    return render_template('simple.html',  tables=[countries.to_html(classes='data')], titles=countries.columns.values)

@app.route('/matplot', methods=['GET'])
def plot_data():

    fig, ax = plt.subplots(figsize = (6,4))

    x = countries.name
    y = countries.gdp_md_est

    ax.bar(x, y, color = "#304C89")

    plt.xticks(rotation = 30, size = 5)
    plt.ylabel("Expected Clean Sheets", size = 5)

    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

@app.route('/geoplot', methods=['GET'])
def geoplot_data():

    fig, ax = plt.subplots(figsize = (12,8))

    countries.to_crs(epsg=3857).plot(ax=ax, alpha=0.5)
    contextily.add_basemap(ax=ax)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

@app.route('/plot.png', methods=['GET'])
def plot_png():

    fig, ax = plt.subplots(figsize = (12,8))

    countries.to_crs(epsg=3857).plot(ax=ax, alpha=0.5)
    contextily.add_basemap(ax=ax)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

@app.route('/plot', methods=("POST", "GET"))
def mpl():
    return render_template('plot.html',
                           PageTitle = "Matplotlib")

# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
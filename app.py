from flask import Flask, render_template
app = Flask(__name__)

import pandas as pd
dati1 = pd.read_csv('/workspace/python/dati1.csv')

@app.route('/', methods=['GET'])
def hello_world():
    return render_template('simple.html',  tables=[dati1.to_html(classes='data')], titles=dati1.columns.values)


# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
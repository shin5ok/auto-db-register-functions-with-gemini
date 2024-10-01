import pandas as pd
import flask

import db

app = flask.Flask(__name__)

@app.get("/")
def _get_all():
    data = db.get_all()
    df = pd.json_normalize(data, sep='_')
    return df.to_html(index=False)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

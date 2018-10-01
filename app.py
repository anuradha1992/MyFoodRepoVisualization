from flask import Flask, render_template
import json
import requests

app = Flask(__name__)


@app.route('/')
def index():
    api_path = "https://www.myfoodrepo.org/api/v1/food_case_foods/graph"
    data = json.loads(requests.get(api_path).text)
    if data['status'] == 200:
        data = data['data']['food_graph']
        data = json.dumps(data)
        return render_template("index.html", data=data, status=200)
    else:
        return render_template("index.html", status=404)


if __name__ == '__main__':
    app.run()

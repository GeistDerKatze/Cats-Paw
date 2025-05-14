from flask import Flask, render_template, request, send_file
import json
from yoink import get_first_google_result

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        search_query = request.form["search"]
        if not search_query:
            return "No query provided", 400

        data = get_first_google_result(search_query)
        # Save JSON temporarily
        filepath = "{result}.json"
        with open(filepath, "w") as f:
            json.dump(data, f, indent=2)

        return send_file(filepath, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4221, debug=True)
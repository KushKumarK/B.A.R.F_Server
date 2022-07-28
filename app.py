from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def get_data():  # put application's code here
    data = request.get_json(force=True)
    print(data["action"])

    return "Sending Data to B.A.R.F"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)

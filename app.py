from flask import Flask, request, jsonify

app = Flask(__name__)

action = ""
actions = ["LIFO",
           "Irrigation",
           "Fertilizer",
           "Plant Seed",
           "Remote Control"]



@app.route('/', methods=['GET', 'POST'])
def get_data():  # put application's code here
    data = request.get_json(force=True)
    global action
    action = data["action"]
    if action in actions:
        pass
    elif action == "":
        pass
    else:
        actions.append(action)
    return "Sending Data to B.A.R.F"


@app.route('/action', methods=["GET", 'POST'])
def send_data():
    if action == "":
        return "20"
    else:
        rec = str(actions.index(action)+1)
        return rec

@app.route("/delete_tile", methods=["GET", "POST"])
def delete_data():
    delData = request.get_json(force=True)
    global action
    if action == delData["action"]:
        action = ""
        if (actions.index(delData["action"])<6):
            return "Permission Denied"
        else:
            send_data()
            del(actions[int(delData["index"])])
            return "Deleted successfully"
    else:
        try:
            del (actions[int(delData["index"])])
            send_data()
            return "Deleted successfully"
        except IndexError:
            send_data()
            return "Encountered error, Delete Successful"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)

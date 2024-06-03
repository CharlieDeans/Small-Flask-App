from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route("/getHelloWorld")
def getHelloWorld():
    return jsonify(msg="Hello, World!")

@app.route("/getText")
def getText():
    text = request.args.get('text', "No Text Provided", type=str)
    return jsonify(msg=text)

@app.route("/")
def helloWorld():
    return render_template('page.html')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port="55055")
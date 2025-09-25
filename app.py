from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello from OpenShift (Flask) 👋</h1>"

if __name__ == "__main__":
    # When OpenShift runs with S2I it uses gunicorn, but this is fine for local tests
    app.run(host="0.0.0.0", port=8080)

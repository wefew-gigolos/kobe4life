from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/gigolos")
def gigolos():
    return "Your name is : Gigolos!"
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')

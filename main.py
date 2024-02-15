from flask import Flask

app = Flask(__name__)
# another comment
# adding another comment to main
# add a comment
@app.route("/")
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    app.run()
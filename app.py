
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home(): return render_template("index.html")

@app.route("/about")
def about():
    return """
    <html>
        <head>
            <title>About Us</title>
        </head>
        <body>
            <h1>About My First Git Project</h1>
            <p>This is my first project using Python Flask and Git.</p>
            <a href="/">Go Back Home</a>
        </body>
    </html>
    """

if __name__ == "__main__": app.run(debug=True)

from flask import Flask, render_template

from flask import Flask, send_file

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    main()

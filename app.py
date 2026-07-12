from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/assets")
def assets():
    return render_template("assets.html")

@app.route("/employees")
def employees():
    return render_template("employees.html")

@app.route("/reports")
def reports():
    return render_template("reports.html")

if __name__ == "__main__":
    app.run(debug=True)

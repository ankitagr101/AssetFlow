from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///assetflow.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
class Asset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    asset_id = db.Column(db.String(20))
    name = db.Column(db.String(100))
    category = db.Column(db.String(50))
    status = db.Column(db.String(30))
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    emp_id = db.Column(db.String(20))
    name = db.Column(db.String(100))
    department = db.Column(db.String(50))
    email = db.Column(db.String(100))
class Assignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    asset_name = db.Column(db.String(100))
    employee_name = db.Column(db.String(100))
@app.route("/")
def home():
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/assets", methods=["GET", "POST"])
def assets():

    if request.method == "POST":

        asset = Asset(
            asset_id=request.form["asset_id"],
            name=request.form["name"],
            category=request.form["category"],
            status=request.form["status"]
        )

        db.session.add(asset)
        db.session.commit()

        return redirect("/assets")

    all_assets = Asset.query.all()

    return render_template("assets.html", assets=all_assets)

@app.route("/employees", methods=["GET", "POST"])
def employees():

    if request.method == "POST":

        employee = Employee(
            emp_id=request.form["emp_id"],
            name=request.form["name"],
            department=request.form["department"],
            email=request.form["email"]
        )

        db.session.add(employee)
        db.session.commit()

        return redirect("/employees")

    employees = Employee.query.all()

    return render_template("employees.html", employees=employees)

@app.route("/assign", methods=["GET", "POST"])
def assign():

    if request.method == "POST":

        assignment = Assignment(
            asset_name=request.form["asset_name"],
            employee_name=request.form["employee_name"]
        )

        db.session.add(assignment)
        db.session.commit()

        return redirect("/assign")

    assignments = Assignment.query.all()
    assets = Asset.query.all()
    employees = Employee.query.all()

    return render_template(
        "assign.html",
        assignments=assignments,
        assets=assets,
        employees=employees
    )

@app.route("/reports")
def reports():

    total_assets = Asset.query.count()
    total_employees = Employee.query.count()
    total_assignments = Assignment.query.count()

    return render_template(
        "reports.html",
        total_assets=total_assets,
        total_employees=total_employees,
        total_assignments=total_assignments
    )

with app.app_context():
    db.create_all()
if __name__ == "__main__":
    app.run(debug=True)

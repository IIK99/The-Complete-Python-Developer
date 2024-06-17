import csv

from flask import Flask, redirect, render_template, request

app = Flask(__name__)
print(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(f"{page_name}.html")


def write_to_file(data):
    print("Writing to file")
    with open("11 Web Dev/WEB CV/data/database.txt", mode="a") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f"\n{email},{subject},{message}\n")


def write_to_csv(data):
    print("Writing to CSV")
    with open("11 Web Dev/WEB CV/data/database.csv", newline="", mode="a") as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(
            database2,
            delimiter=",",
            quotechar='"',
            quoting=csv.QUOTE_MINIMAL,
        )
        csv_writer.writerow([email, subject, message])


@app.route("/submit_form", methods=["POST", "GET"])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            print("Data received:", data)
            write_to_file(data)
            write_to_csv(data)
            return redirect("/thankyou")
        except Exception as e:
            print(f"Failed to save data: {e}")
            return "Did not save to database"
    else:
        return "something went wrong"


# @app.route("/about")
# def about():
#     return render_template("about.html")


# @app.route("/components")
# def components():
#     return render_template("components.html")


# @app.route("/contact")
# def contact():
#     return render_template("contact.html")


# @app.route("/thankyou")
# def thankyou():
#     return render_template("thankyou.html")


# @app.route("/work")
# def work():
#     return render_template("work.html")


# @app.route("/works")
# def works():
#     return render_template("works.html")


if __name__ == "__main__":
    app.run(debug=True)

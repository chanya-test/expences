from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/aa")
def home():
    return render_template("template.html")


@app.route("/salvador")
def salvador():
    return "Hello, Salvador"


@app.route("/about")
def about():
    return render_template("about.html")


@app.route('/')
def form():
    return render_template('form.html')


@app.route('/submitted', methods=['POST'])
def submitted_form():
    name = request.form['name']
    email = request.form['email']
    site = request.form['site_url']
    comments = request.form['comments']
    return render_template(
        'submitted_form.html',
        name=name,
        email=email,
        site=site,
        comments=comments)


if __name__ == "__main__":
    app.run(debug=True)

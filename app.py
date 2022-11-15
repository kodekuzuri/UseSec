from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
from consent import ConsentForm
from flask import redirect,url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'   
Bootstrap(app)



# @app.route("/")
# def home():
#     return "Kill me now :("

@app.route("/home")
def home2():
    return render_template("home.html", name = "Parth",date="12/12/2019")


@app.route("/hello")
def hello_world():
    return 'hello world' 

@app.route("/hello/<name>")
def varfunc(name):
    return 'Hello %s' % name


@app.route('/', methods=['GET', 'POST'])
def index():
    form = ConsentForm()
    message = ""
    if form.validate_on_submit():
        accept = form.accept.data
        name = form.name.data
        print(name)
        if accept:
            return redirect(url_for('home2'))
        else:
            message = "That actor is not in our database."
    return render_template('./index.html', names=form.name.data, form=form, message=message)


if __name__ == '__main__':
    app.run(debug = True) ; 
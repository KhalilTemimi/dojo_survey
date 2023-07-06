from flask import Flask, render_template, request, redirect, session
from dojo import Dojo
app = Flask(__name__)
app.secret_key="secret key"

@app.route('/')
def home():
    return render_template('index.html')

# @app.route('/create', methods=['POST'])
# def create_burger():
#     # if there are errors:
#     # We call the staticmethod on Burger model to validate
#     if not Burger.validate_burger(request.form):
#         # redirect to the route where the burger form is rendered.
#         return redirect('/')
#     # else no errors:
#     Burger.save(request.form)
#     return redirect("/burgers")

@app.route('/process', methods=['post'])
def store_info():
    if not Dojo.validate_dojo(request.form):
        return redirect('/')
    data = {
        'name' : request.form['name'],
        # session['gender']=request.form['gender']
        'location':request.form['location'],
        'language':request.form['language'],
        'comment':request.form['comment']
    }
    Dojo.save(data)
    return redirect('/result')

@app.route('/result')
def display_info():
    dojo = Dojo.show_last_user()
    return render_template('result.html', dojo = dojo)

if __name__ == '__main__':
    app.run(debug=True)
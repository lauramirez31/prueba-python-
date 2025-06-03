from flask import flask, render_template 

app=flask(_name_) 

@app.route ("/")
def index():
    return render_template ("index.html")
if  _name_ == "_main_":
    app.run()
@app.route ("/contact")
def index():
    return render_template ("contact.html")
if  _name_ == "_main_":
    app.run()



















from flask import Flask, request, render_template

app = Flask(__name__, template_folder= "templates")

@app.route("/", methods=["POST","GET"])
def home():
    if request.method=='POST':
        return render_template("index.html", Placeholder_text="Hello from  POST method")
    if request.method=="GET":
        return  render_template("index.html", Placeholder_text="Hello from  GET method")
    

@app.route("/submit")
def submit():
    return "Hello from  submit page"

@app.route("/shamanth")
def sham():
    return "Shamanth is an AI Engineer"

if __name__ == '__main__':
    app.run()

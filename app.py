from flask import Flask

app = Flask(_name_)
@app.route("/info")
def lwinfo():
	return "I am Dhananjay from India"
@app.route("/phone")
def lwphone():
	return "4564134596"
app.run(host="0.0.0.0")

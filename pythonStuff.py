from flask import Flask, request, render_template, redirect
import csv

app = Flask(__name__)

@app.route('/hello')
def home():
	with open("data.csv", mode="r") as file:
		csvFile = csv.reader(file)

		for lines in csvFile:
			return lines[1]

	return render_template('index.htm')



app.run(debug=True, port=5000)
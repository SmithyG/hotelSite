from flask import Flask, render_template
from flask import request
from datetime import datetime
import csv

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/attractions')
def attractions():
    return render_template('attractions.html')


@app.route('/bookings')
def bookings():
    return render_template('bookings.html')


@app.route('/reviews')
def reviews():
    with open('static\\reviews.csv', 'r') as inFile:
        reader = csv.reader(inFile)
        reviewList = [row for row in reader]
    return render_template('reviews.html', reviewList=reviewList)


def readFile(aFile):
    with open(aFile, 'r') as inFile:
        reader = csv.reader(inFile)
        reviewList = [row for row in reader]
    return reviewList


def writeFile(aList, aFile):
    with open(aFile, 'w',) as outFile:
        writer = csv.writer(outFile)
        writer.writerows(aList)
    return


@app.route('/addReview', methods=['POST'])
def addReview():
    reviewFile = 'static\\reviews.csv'
    reviewList = readFile(reviewFile)

    name = request.form[('name')]
    comment = request.form[('comment')]
    date = datetime.now().strftime('%d-%m-%Y')

    newReview = [name, comment, date]
    reviewList.append(newReview)

    writeFile(reviewList, reviewFile)
    return render_template('reviews.html', reviewList=reviewList)


if __name__ == '__main__':
    app.run(debug=True)

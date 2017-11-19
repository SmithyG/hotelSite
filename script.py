from flask import Flask, render_template, request
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
    with open('static\\bookings.csv', 'r') as inFile:
        reader = csv.reader(inFile)
        bookingList = [row for row in reader if '1' in row]
    return render_template('bookings.html', bookingList=bookingList)


@app.route('/reviews')
def reviews():
    with open('static\\reviews.csv', 'r') as inFile:
        reader = csv.reader(inFile)
        reviewList = [row for row in reader]
    return render_template('reviews.html', reviewList=reviewList)


def readReviewFile(aFile):
    with open(aFile, 'r') as inFile:
        reader = csv.reader(inFile)
        reviewList = [row for row in reader]
    return reviewList


def readBookingFile(aFile):
    with open(aFile, 'r') as inFile:
        reader = csv.reader(inFile)
        bookingList = [row for row in reader]
    return bookingList


def writeFile(aList, aFile):
    with open(aFile, 'w', newline='') as outFile:
        writer = csv.writer(outFile)
        writer.writerows(aList)
    return


@app.route('/addReview', methods=['POST'])
def addReview():
    reviewFile = 'static\\reviews.csv'
    reviewList = readReviewFile(reviewFile)

    name = request.form[('name')]
    comment = request.form[('comment')]
    date = datetime.now().strftime('%d-%m-%Y')

    newReview = [name, comment, date]
    reviewList.append(newReview)

    writeFile(reviewList, reviewFile)

    return render_template('reviews.html', reviewList=reviewList)


@app.route('/addBooking', methods=['POST'])
def addBooking():
    bookingFile = 'static\\bookings.csv'
    bookingList = readBookingFile(bookingFile)

    bookingName = request.form[('bookingName')]
    email = request.form[('email')]
    arrivalDate = request.form[('arrivalDate')]
    departureDate = request.form[('departureDate')]
    status = 0

    newBooking = [arrivalDate, departureDate, bookingName, email, status]
    bookingList.append(newBooking)

    writeFile(bookingList, bookingFile)

    return render_template('bookings.html', bookingList=bookingList)


@app.route('/exitForm', methods=['GET'])
def exitForm():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request
from datetime import datetime
import csv

app = Flask(__name__)

#Page controllers

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/attractions')
def attractions():
    return render_template('attractions.html')

@app.route('/confirmButton', methods=['GET'])
def confirmButton():
    return render_template('bookings.html')


@app.route('/bookings')
def bookings():
    with open('static\\bookings.csv', 'r') as inFile:
        #The file is assigned to "reader"
        reader = csv.reader(inFile)
        #the bookingList is then created and is only populated if a 1 is found at the end of the CSV row
        #This allows for only confirmed bookings to be displayed by the bookings page
        bookingList = [row for row in reader if '1' in row]
    return render_template('bookings.html', bookingList=bookingList)


@app.route('/reviews')
def reviews():
    with open('static\\reviews.csv', 'r') as inFile:
        reader = csv.reader(inFile)
        #reviewList is created and populated with data from the reviews.csv file
        reviewList = [row for row in reader]
    return render_template('reviews.html', reviewList=reviewList)


#File readers for reviews and bookings

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

#writeFile function to write reviews and bookings

def writeFile(aList, aFile):
    with open(aFile, 'w', newline='') as outFile:
        writer = csv.writer(outFile)
        writer.writerows(aList)
    return

#addReview function to handle entering new reviews
@app.route('/addReview', methods=['POST'])
def addReview():
    reviewFile = 'static\\reviews.csv'
    reviewList = readReviewFile(reviewFile)

    #Data is collected from the review form
    name = request.form[('name')]
    comment = request.form[('comment')]
    date = datetime.now().strftime('%d/%m/%Y')
    #A new review is created with the collected data
    newReview = [name, comment, date]
    #And then added to the reviewList
    reviewList.append(newReview)
    #The new review is written to the file using the writeFile function
    writeFile(reviewList, reviewFile)

    return render_template('reviews.html', reviewList=reviewList)

#addBooking function to handle entering new bookings
@app.route('/addBooking', methods=['POST'])
def addBooking():
    bookingFile = 'static\\bookings.csv'
    bookingList = readBookingFile(bookingFile)

    #Data is collected from the booking form
    bookingName = request.form[('bookingName')]
    email = request.form[('email')]
    arrivalDate = request.form[('arrivalDate')]
    departureDate = request.form[('departureDate')]
    #The status is set to 0 by default, meaning the booking is unconfirmed
    status = 0

    #A new booking is created using the data from the form
    newBooking = [arrivalDate, departureDate, bookingName, email, status]
    bookingList.append(newBooking)

    #The new booking is written to bookings.csv using the writeFile function
    writeFile(bookingList, bookingFile)

    return render_template('home.html')


@app.route('/exitForm', methods=['GET'])
def exitForm():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)

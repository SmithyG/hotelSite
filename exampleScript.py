from flask import Flask, render_template
from flask import request
import csv

app = Flask(__name__)

@app.route('/')
def home(): 
    return render_template('home.html')

@app.route('/skills')
def skills():
    with open('static\\skills.csv','r') as inFile:
        reader = csv.reader(inFile)
        skillList = [row for row in reader]
    return render_template('skills.html', skillList = skillList)

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')
    
@app.route('/exit', methods=['GET'])
def exit():
    return render_template('home.html')

def readFile(aFile):
    with open(aFile,'r') as inFile:
        reader = csv.reader(inFile)
        skillList = [row for row in reader]
    return skillList

def writeFile(aList, aFile):
    with open(aFile,'w',) as outFile:
        writer = csv.writer(outFile)
        writer.writerows(aList)
    return

@app.route('/addSkill',methods=['POST'])
def addSkill():
    skillFile ='static\\skills.csv'
    skillList = readFile(skillFile)
    
    skillName = request.form[('skill')]
    rating = request.form[('rating')]
    
    newSkill = [skillName,rating]
    skillList.append(newSkill)
    
    writeFile(skillList,skillFile)
    return render_template('skills.html',skillList=skillList)
    
    
if __name__ == '__main__':
    app.run(debug = True)

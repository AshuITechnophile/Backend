# impoting the Flack class from flask module
from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

#let's see the content of the flask module
#print(dir(flask))
#let's create an object
app = Flask(__name__)



#connecting  the flask application (server) with SQLite Database
#let's create the url This  command tells the flask app to  connect with  a sqlite type database named task.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task.db'

#creting an object  of SQLalchemy class
#Telling the SqLalchemy class to connect with 
database = SQLAlchemy(app)

#writing python class which will  be used to insert data into table
class Task(database.Model):
    SNo = database.Column(database.Integer,primary_key= True)
    taskTitle = database.Column(database.String(100),nullable = False)
    taskDescription = database.Column(database.String(200),nullable = False)


@app.route('/', methods=["GET","POST"] )
def index():
  #let's check if the request is get or  post
  #if request is post--->
  
  if request.method == "POST":
    #fetch the values of the title and description
    task_title = request.form.get('Title')
    task_description = request.form.get('Description')
    print(tasktitle,taskDescription)

    #add it to the database
    task = Task(taskTitle = task_title )
  

  return render_template('index.html')

#Second route: for contact 
@app.route('/contact')
def contact():
   return render_template('contact.html')

#Third route: for About
@app.route('/about')
def about():
   
 return render_template('about.html')


app.run(debug = True, host = '0.0.0.0') 



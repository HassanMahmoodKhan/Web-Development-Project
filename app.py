import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

class  trip_data (db.Model):
    id = db.Column(db.Integer, primary_key= True)
    origin = db.Column(db.Text)
    destination = db.Column(db.Text)
    
    

    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination
        

    def __repr__(self):
        return (f"{self.origin}+{self.destination}")


db.create_all()


trip_1 = trip_data('Toronto','Montreal')
trip_2 = trip_data('Toronto','Ottawa')
trip_3 = trip_data('Toronto','Vancouver')
trip_4 = trip_data('Toronto','Mississauga')
trip_5 = trip_data('Montreal','Toronto')
trip_6 = trip_data('Montreal','Ottawa')
trip_7 = trip_data('Montreal','Vancouver')
trip_8 = trip_data('Montreal','Mississauga')
trip_9 = trip_data('Ottawa','Toronto')
trip_10 = trip_data('Ottawa','Montreal')
trip_11 = trip_data('Ottawa','Vancouver')
trip_12 = trip_data('Ottawa','Mississauga')
trip_13 = trip_data('Vancouver','Toronto')
trip_14 = trip_data('Vancouver','Montreal')
trip_15 = trip_data('Vancouver','Ottawa')
trip_16 = trip_data('Vancouver','Mississauga')
trip_17 = trip_data('Mississauga','Toronto')
trip_18 = trip_data('Mississauga','Montreal')
trip_19 = trip_data('Mississauga','Ottawa')
trip_20 = trip_data('Mississauga','Vancouver')


db.session.add_all([trip_1, trip_2, trip_3, trip_4, trip_5, trip_6, trip_7, trip_8, trip_9, trip_10, trip_11, trip_12, trip_13, trip_14,trip_15, trip_16, trip_17, trip_18, trip_19, trip_20])
                     
db.session.commit()   


################################################################################



from flask import Flask, render_template, request, url_for

app = Flask(__name__)
@app.route('/')
def homepage():
    return render_template('webpage1.html')

@app.route('/trip', methods=['GET', 'POST'])
def trip():
    origin= request.form.get('origin')
    destination= request.form.get('destination')
    date= request.form.get('date')
    passengers= request.form.get('passengers')
    select=[origin, destination, date, passengers]
    return(str(select))


@app.route('/About')
def About():
    return render_template('About.html')

db = SQLAlchemy(app)
migrate= Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True)
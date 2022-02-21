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
    date = db.Column(db.Text)
    
    

    def __init__(self, origin, destination, date):
        self.origin = origin
        self.destination = destination
        self.date = date
        
    def __repr__(self):
        return (f"Train from {self.origin} to {self.destination} is available on {self.date}")

################################################################################
################# Do not comment out below code ################################
################################################################################


# db.create_all()


# trip_1 = trip_data('Toronto','Montreal', 'Date')
# trip_2 = trip_data('Toronto','Ottawa', 'Date')
# trip_3 = trip_data('Toronto','Vancouver', 'Date')
# trip_4 = trip_data('Toronto','Mississauga', 'Date')
# trip_5 = trip_data('Montreal','Toronto', 'Date')
# trip_6 = trip_data('Montreal','Ottawa', 'Date')
# trip_7 = trip_data('Montreal','Vancouver', 'Date')
# trip_8 = trip_data('Montreal','Mississauga', 'Date')
# trip_9 = trip_data('Ottawa','Toronto', 'Date')
# trip_10 = trip_data('Ottawa','Montreal', 'Date')
# trip_11 = trip_data('Ottawa','Vancouver', 'Date')
# trip_12 = trip_data('Ottawa','Mississauga', 'Date')
# trip_13 = trip_data('Vancouver','Toronto', 'Date')
# trip_14 = trip_data('Vancouver','Montreal', 'Date')
# trip_15 = trip_data('Vancouver','Ottawa', 'Date')
# trip_16 = trip_data('Vancouver','Mississauga', 'Date')
# trip_17 = trip_data('Mississauga','Toronto', 'Date')
# trip_18 = trip_data('Mississauga','Montreal', 'Date')
# trip_19 = trip_data('Mississauga','Ottawa', 'Date')
# trip_20 = trip_data('Mississauga','Vancouver', 'Date')


# db.session.add_all([trip_1, trip_2, trip_3, trip_4, trip_5, trip_6, trip_7, trip_8, trip_9, trip_10, trip_11, trip_12, trip_13, trip_14,trip_15, trip_16, trip_17, trip_18, trip_19, trip_20])
                     
# db.session.commit()   

# print (trip_data.query.filter_by(origin='Toronto', destination='Montreal').all())
# # print (trip_data.query.all())



################################################################################



from flask import Flask, render_template, request, url_for

app = Flask(__name__)
@app.route('/')
def homepage():
    return render_template('webpage1.html')
# trp1 =(trip_data.query.all())

trp1 = trip_data.query.filter_by(origin='Toronto', destination='Montreal').all()
trp2 = trip_data.query.filter_by(origin='Toronto', destination='Ottawa').all()
trp3 = trip_data.query.filter_by(origin='Toronto', destination='Vancouver').all()
trp4 = trip_data.query.filter_by(origin='Toronto', destination='Mississauga').all()
trp5 = trip_data.query.filter_by(origin='Montreal', destination='Toronto').all()
trp6 = trip_data.query.filter_by(origin='Montreal', destination='Ottawa').all()
trp7 = trip_data.query.filter_by(origin='Montreal', destination='Vancouver').all()
trp8 = trip_data.query.filter_by(origin='Montreal', destination='Mississauga').all()
trp9 = trip_data.query.filter_by(origin='Ottawa', destination='Toronto').all()
trp10 = trip_data.query.filter_by(origin='Ottawa', destination='Montreal').all()
trp11= trip_data.query.filter_by(origin='Ottawa', destination='Vancouver').all()
trp12= trip_data.query.filter_by(origin='Ottawa', destination='Mississauga').all()
trp13= trip_data.query.filter_by(origin='Vancouver', destination='Toronto').all()
trp14= trip_data.query.filter_by(origin='Vancouver', destination='Montreal').all()
trp15= trip_data.query.filter_by(origin='Vancouver', destination='Ottawa').all()
trp16= trip_data.query.filter_by(origin='Vancouver', destination='Mississauga').all()
trp17= trip_data.query.filter_by(origin='Mississauga', destination='Toronto').all()
trp18= trip_data.query.filter_by(origin='Mississauga', destination='Montreal').all()
trp19= trip_data.query.filter_by(origin='Mississauga', destination='Vancouver').all()
trp20= trip_data.query.filter_by(origin='Mississauga', destination='Ottawa').all()


@app.route('/trip', methods=['GET', 'POST'])
def trip():
    origin= request.form.get('origin')
    destination= request.form.get('destination')
    date= request.form.get('date')
    passengers= request.form.get('passengers')
    select=[origin, destination, date, passengers]
    if date== date:
        return (str(date))
    if origin=='Toronto' and destination=='Montreal':
        return (str(trp1[0]))
    if origin=='Toronto' and destination=='Ottawa':
        return (str(trp2[0]))
    if origin=='Toronto' and destination=='Vancouver':
        return (str(trp3[0]))
    if origin=='Toronto' and destination=='Mississauga':
        return (str(trp4[0]))
    if origin=='Montreal' and destination=='Toronto':
        return (str(trp5[0]))
    if origin=='Montreal' and destination=='Ottawa':
        return (str(trp6[0]))
    if origin=='Montreal' and destination=='Vancouver':
        return (str(trp7[0]))
    if origin=='Montreal' and destination=='Mississauga':
        return (str(trp8[0]))
    if origin=='Ottawa' and destination=='Toronto':
        return (str(trp9[0]))
    if origin=='Ottawa' and destination=='Montreal':
        return (str(trp10[0]))
    if origin=='Ottawa' and destination=='Vancouver':
        return (str(trp11[0]))
    if origin=='Ottawa' and destination=='Mississauga':
        return (str(trp12[0]))
    if origin=='Vancouver' and destination=='Toronto':
        return (str(trp13[0]))
    if origin=='Vancouver' and destination=='Montreal':
        return (str(trp14[0]))
    if origin=='Vancouver' and destination=='Ottawa':
        return (str(trp15[0]))
    if origin=='Vancouver' and destination=='Mississauga':
        return (str(trp16[0]))
    if origin=='Mississauga' and destination=='Toronto':
        return (str(trp17[0]))
    if origin=='Mississauga' and destination=='Montreal':
        return (str(trp18[0]))
    if origin=='Mississauga' and destination=='Ottawa':
        return (str(trp19[0]))
    if origin=='Mississauga' and destination=='vancouver':
        return (str(trp20[0]))
    else:
        return ('Sorry! Invalid Input.')


    # return(str(select))

        
@app.route('/About')
def About():
    return render_template('About.html')

db = SQLAlchemy(app)
migrate= Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True)


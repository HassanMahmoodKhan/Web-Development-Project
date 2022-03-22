import os
import datetime
from datetime import date
from types import CoroutineType
from flask import Flask, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from rds import cur,conn
import requests
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
        return ()
        

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
# print (trip_data.query.all())



################################################################################



from flask import Flask, render_template, request
from flask import url_for

app = Flask(__name__)



@app.route('/')
def Home():
    return render_template('Home(new).html')


@app.route('/About')
def About():
    return render_template('About.html') 
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



global_ori = []
global_des = []
global_dat = []
global_pas = []

@app.route('/trip', methods=['GET', 'POST'])
def trip():
    origin= request.form.get('origin')
    destination= request.form.get('destination')
    date= request.form.get('date')
    passengers= request.form.get('passengers')
    global_ori.append(origin)
    global_des.append(destination)
    global_dat.append(date)
    global_pas.append(passengers)
            
    if origin == origin and destination== destination:
    
        qur1 = "SELECT * FROM DATABASEPROJ.train_data WHERE departure= %s AND arrival= %s"
        tup2 = (origin, destination)   
        cur.execute(qur1,tup2)
        details = cur.fetchall()  
        details1 = list(details[0])
        details2 = list(details[1])
        details3 = list(details[2])
        details4 = list(details[3])
        
        
        return render_template('Train_Schedule.html',  date=date, train_1 = details1[1:2][0],
                                                        origin_1 = details1[2:3][0],
                                                        destination_1 = details1[3:4][0],
                                                        departure_time_1 = details1[4:5][0],
                                                        arrival_time_1 = details1[5:6][0],
                                                        duration_1 = details1[6:7][0],
                                                        train_2 = details2[1:2][0],
                                                        departure_time_2 = details2[4:5][0],
                                                        arrival_time_2 = details2[5:6][0],
                                                        duration_2 = details2[6:7][0],
                                                        train_3 = details3[1:2][0],
                                                        departure_time_3 = details3[4:5][0],
                                                        arrival_time_3 = details3[5:6][0],
                                                        duration_3 = details3[6:7][0],
                                                        train_4 = details4[1:2][0],
                                                        departure_time_4 = details4[4:5][0],
                                                        arrival_time_4 = details4[5:6][0],
                                                        duration_4 = details4[6:7][0],
                                                        eco1 = details1[7:8][0], eco2 = details2[7:8][0],
                                                        eco3 = details3[7:8][0], eco4 = details4[7:8][0],
                                                        bus1 = details1[8:9][0], bus2 = details2[8:9][0],
                                                        bus3 = details3[8:9][0], bus4 = details4[8:9][0]) 

    
    else:
        return redirect(url_for('fare'))
  
gst_1 =[]
pst_1 =[]
total_1 = []
g_passenger = []  
fare_1 = []

@app.route('/fare', methods=['GET', 'POST'])
def fare():

    origin = global_ori.pop()
    destination = global_des.pop()
    date = global_dat.pop()
    passengers = global_pas.pop()
    g_passenger.append(passengers)
    option = request.form['option']
    
    if origin==origin and destination==destination and option==option:
        option1 = option[-1:]
        print(option1)
        query = "SELECT * FROM DATABASEPROJ.train_data WHERE departure= %s AND arrival= %s AND train= %s"
        tup1 = (origin, destination, option1) 
        cur.execute(query,tup1) 
        details = cur.fetchall()  
        details1 = list(details[0])
        fare = int(details1[7:8][0])* int(passengers)
        gst = int(0.05 * fare)
        pst = int(0.09 * fare)
        total = int((fare + gst + pst))
        gst_1.append(gst)
        pst_1.append(pst)
        total_1.append(total)
        fare_1.append(fare)
    
        return render_template('Fare_Details.html', origin_1=origin, destination_1=destination, date=date,
                                                passengers=passengers, option=option, departure_time_1= details1[4:5][0],
                                                arrival_time_1 = details1[5:6][0], duration_1= details1[6:7][0], train_1=option1, fare=fare,
                                                gst=gst, pst=pst, total=total )

        
       

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    
    return render_template('Contact_Info1.html')

g_fname=[]  
g_lname=[]
g_address1=[]
g_address2=[]
g_city=[]
g_zipcode=[]
g_province=[]
g_cnumber=[]
g_email=[]


@app.route('/guest', methods=['GET', 'POST'])
def guest():
    fname= request.form.get('fname')
    lname = request.form.get('lname')
    address1=request.form.get('address1')
    address2=request.form.get('address2')
    city= request.form.get('city')
    zipcode= request.form.get('zipcode')
    province= request.form.get('province')
    cnumber= request.form.get('cnumber')
    email= request.form.get('email')
    g_fname.append(fname)
    g_lname.append(lname)
    g_address1.append(address1)
    g_address2.append(address2)
    g_city.append(city)
    g_zipcode.append(zipcode)
    g_province.append(province)
    g_cnumber.append(cnumber)
    g_email.append(email)
    
    query = "INSERT INTO DATABASEPROJ.guest_user (fname,lname,address1,address2,city,zipcode,province,cnumber,email) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    tup1= (fname,lname,address1,address2,city,zipcode,province,cnumber,email) 
    print(tup1)
    cur.execute(query,tup1) 
    conn.commit()

    return render_template('Payment.html', passengers = g_passenger[0], gst=gst_1[0], pst=pst_1[0],total=total_1[0],
                                            fare= fare_1[0])

@app.route('/signup',  methods=['GET', 'POST'])
def signup():
    return render_template('reg.html')

@app.route('/signup1',  methods=['GET', 'POST'])
def signup1():
    fname = request.form.get('first_name')
    lname = request.form.get('last_name')
    password = request.form.get('password')
    email = request.form.get('email')
    area_code = request.form.get('area_code')
    phone = request.form.get('phone')
    country = request.form.get('country')
    print(fname,lname, password, email, area_code, phone, country)
    tup1 = (email)
    query = "SELECT * FROM DATABASEPROJ.registration_info WHERE email_id = %s"
    cur.execute(query,tup1)
    log_detail = list(cur.fetchall())
    email1 = log_detail[4:5]
    
    if email==email1 :
        return redirect(url_for('login'))

    else:
        query = "INSERT INTO DATABASEPROJ.registration_info (first_name,last_name,password,email_id,area_code,phone_number,country) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        tup1= (fname,lname,password,email,area_code,phone,country) 
        print(tup1)
        cur.execute(query,tup1) 
        conn.commit()

        return redirect(url_for('Home'))



@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/login_1', methods=['GET', 'POST'])
def login_1():
    email = request.form.get('email')
    password = request.form.get('password')
    
    query = "SELECT * FROM DATABASEPROJ.registration_info WHERE email_id = %s AND password= %s"
    tup1 = (email, password)
    cur.execute(query,tup1)
    log_detail = list(cur.fetchall())
    
    if log_detail == []:
        return redirect(url_for('signup'))
    
    if log_detail != []:
        log_detail_1 = log_detail[0]
        email1 = log_detail_1[4:5][0]
        password1 = log_detail_1[3:4][0]
        print(email1, password1, email, password, log_detail_1)
        if email==email1 and password==password1:    
            return render_template('Home(new).html')
        else:
            return redirect(url_for('signup'))
        

@app.route('/login2', methods=['GET', 'POST'])
def login2():
    email = request.form.get('email')
    password = request.form.get('password')
    
    query = "SELECT * FROM DATABASEPROJ.registration_info WHERE email_id = %s AND password= %s"
    tup1 = (email, password)
    cur.execute(query,tup1)
    log_detail = list(cur.fetchall())
    
    if log_detail == []:
        return redirect(url_for('signup'))
    
    if log_detail != []:
        log_detail_1 = log_detail[0]
        email1 = log_detail_1[4:5][0]
        password1 = log_detail_1[3:4][0]
        print(email1, password1, email, password, log_detail_1)
        if email==email1 and password==password1:
            return render_template('Payment.html', passengers = g_passenger[0], gst=gst_1[0], pst=pst_1[0],total=total_1[0],
                                                fare= fare_1[0])
        else:
            return redirect(url_for('signup'))
    

    

    

    

# @app.route('/payment', method = ['GET', 'POST'])
# def payment():
#     return render_template('Payment.html')




    # if origin== 'Origin' or destination== 'Destination':
    #     return ("<h1>Please select origin and destination!<h1>")
    # elif origin==destination:
    #     return ('<h1>Origin and destination can not be the same!<h1>')
    # elif origin=='Toronto' and destination=='Montreal' and D > D1:
    #     return (str(trp1[0]) + date + ".<br><br>Seats are available for " + passengers + " passenger.")
    # elif origin=='Toronto' and destination=='Ottawa' and D > D1:
    #     return (str(trp2[0]) + date + "." "<br><br>Seats are available for " + passengers + " passenger.")
    # elif origin=='Toronto' and destination=='Vancouver' and D > D1:
    #     return (str(trp3[0]) + date + "." "<br><br>Seats are available for " + passengers + " passenger.")
    # elif origin=='Toronto' and destination=='Mississauga' and D > D1:
    #     return (str(trp4[0]) + date + "." "<br><br>Seats are available for " + passengers + " passenger.")
    # elif origin=='Montreal' and destination=='Toronto' and D > D1:
    #     return (str(trp5[0]) + date + "." "<br><br>Seats are available for " + passengers + " passenger.")
    # elif origin=='Montreal' and destination=='Ottawa' and D > D1:
    #     return (str(trp6[0]) + date + "." "<br><br>Seats are available for " + passengers + " passenger.")
    # elif origin=='Montreal' and destination=='Vancouver' and D > D1:
    #     return (str(trp7[0]) + date + "." "<br><br>Seats are available for " + passengers + " passenger.")
    # elif origin=='Montreal' and destination=='Mississauga' and D > D1:
    #     return (str(trp8[0]) + date + "." "<br><br>Seats are available for " + passengers + " passenger.")
    # elif origin=='Ottawa' and destination=='Toronto' and D > D1:
    #     return (str(trp9[0]) + date + "." "<br><br>Seats are available for " + passengers + " passenger.")
    # elif origin=='Ottawa' and destination=='Montreal' and D > D1:
    #     return (str(trp10[0]) + date + "." "<br><br>Seats are available for " + passengers + " passenger.")
    # elif origin=='Ottawa' and destination=='Vancouver' and D > D1:
    #     return (str(trp11[0]) + date + "." "<br><br>Seats are available for " + passengers + " passenger.")
    # elif origin=='Ottawa' and destination=='Mississauga' and D > D1:
    #     return (str(trp12[0]) + date + "." "<br><br>Seats are available for " + passengers + " passenger.")
    # elif origin=='Vancouver' and destination=='Toronto' and D > D1:
    #     return (str(trp13[0]) + date + "." "<br><br>Seats are available for " + passengers + " passenger.")
    # elif origin=='Vancouver' and destination=='Montreal' and D > D1:
    #     return (str(trp14[0]) + date + "." "<br><br>Seats are available for " + passengers + " passenger.")
    # elif origin=='Vancouver' and destination=='Ottawa' and D > D1:
    #     return (str(trp15[0]) + date + "." "<br><br>Seats are available for " + passengers + " passenger.")
    # elif origin=='Vancouver' and destination=='Mississauga' and D > D1:
    #     return (str(trp16[0]) + date + "." "<br><br>Seats are available for " + passengers + " passenger.")
    # elif origin=='Mississauga' and destination=='Toronto' and D > D1:
    #     return (str(trp17[0]) + date + "." "<br><br>Seats are available for " + passengers + " passenger.")
    # elif origin=='Mississauga' and destination=='Montreal' and D > D1:
    #     return (str(trp18[0]) + date + "." "<br><br>Seats are available for " + passengers + " passenger.")
    # elif origin=='Mississauga' and destination=='Ottawa' and D > D1:
    #     return (str(trp19[0]) + date + "." "<br><br>Seats are available for " + passengers + " passenger.")
    # elif origin=='Mississauga' and destination=='vancouver' and D > D1 :
    #     return (str(trp20[0]) + date + "." "<br><br>Seats are available for " + passengers + " passenger.")
    # else:
    #     return ('<h1>Invalid date input!<h1>')


    



db = SQLAlchemy(app)
migrate= Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True)


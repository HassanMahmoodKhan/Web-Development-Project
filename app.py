import os
from flask import Flask, redirect, render_template, request, url_for
from datetime import datetime
from rds import cur,conn

basedir = os.path.abspath(os.path.dirname(__file__))

today = datetime.today().strftime('%Y-%m-%d')

app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('Home(new).html', today= today)


@app.route('/About')
def About():
    return render_template('about1.html') 

@app.route('/Contact_Us')
def contact_us():
    return render_template('contact.html')

@app.route('/Covid')
def covid():
    return render_template('index.html') 

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

    if origin != None:
        global_ori.insert(0, origin)
    if destination != None:
        global_des.insert(0, destination)
    if date != None:
        global_dat.insert(0, date)
    if passengers != None:
        global_pas.insert(0, passengers)

    print(global_ori, global_des,global_dat, global_pas)

    if global_ori[0]==global_des[0]:
        return redirect(url_for('Home'))

    if global_ori[0] == global_ori[0] and global_des[0] == global_des[0]:
    
        qur1 = "SELECT * FROM DATABASEPROJ.train_data WHERE departure= %s AND arrival= %s"
        tup2 = (global_ori[0], global_des[0])  
        print(tup2) 
        cur.execute(qur1,tup2)
        details = cur.fetchall()
        print(details)  
        details1 = list(details[0])
        details2 = list(details[1])
        details3 = list(details[2])
        details4 = list(details[3])
        return render_template('Train_Schedule.html',  date=global_dat[0], train_1 = details1[1:2][0],
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


        

gst_1 =[]
pst_1 =[]
total_1 = []
g_passenger = []  
fare_1 = []
option = []

@app.route('/fare', methods=['GET', 'POST'])
def fare():

    origin = global_ori[0]
    destination = global_des[0]
    date = global_dat[0]
    passengers = global_pas[0]
    g_passenger.insert(0, passengers)
    option_1 = request.form.get('option')
    if option_1 != None:
        option.insert(0, option_1)
    print(option)
    
    
    if origin==origin and destination==destination and option==option:
        option1 = option[0][-1:]
        print(option[0])
        query = "SELECT * FROM DATABASEPROJ.train_data WHERE departure= %s AND arrival= %s AND train= %s"
        tup1 = (origin, destination, option1) 
        cur.execute(query,tup1) 
        details = cur.fetchall()  
        details1 = list(details[-1:][0])
        print(details1)
        if option[0][0:3]=="Eco":
            fare = int(details1[7:8][0])* int(passengers)
        else:
            fare = int(details1[8:9][0])* int(passengers)

        gst = int(0.05 * fare)
        pst = int(0.09 * fare)
        total = int((fare + gst + pst))
        gst_1.insert(0, gst)
        pst_1.insert(0, pst)
        total_1.insert(0, total)
        fare_1.insert(0, fare)
    
        return render_template('Fare_Details.html', origin_1=origin, destination_1=destination, date=date,
                                                passengers=passengers, option=option[0], departure_time_1= details1[4:5][0],
                                                arrival_time_1 = details1[5:6][0], duration_1= details1[6:7][0], train_1=option1, fare=fare_1[0],
                                                gst=gst_1[0] , pst=pst_1[0], total=total_1[0] )

        
       

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
    g_fname.insert(0, fname)
    g_lname.insert(0, lname)
    g_address1.insert(0, address1)
    g_address2.insert(0, address2)
    g_city.insert(0, city)
    g_zipcode.insert(0, zipcode)
    g_province.insert(0, province)
    g_cnumber.insert(0, cnumber)
    g_email.insert(0, email)
    
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
    
    phone = request.form.get('phone')
    province = request.form.get('province_1')
    print(fname,lname, password, email,  phone, province)
    tup1 = (email)
    query = "SELECT * FROM DATABASEPROJ.registration_info WHERE email_id = %s"
    cur.execute(query,tup1)
    log_detail = list(cur.fetchall())
    email1 = log_detail[4:5]
    
    if email==email1 :
        return redirect(url_for('login'))

    else:
        query = "INSERT INTO DATABASEPROJ.registration_info (first_name,last_name,password,email_id,phone_number, province) VALUES (%s,%s,%s,%s,%s,%s)"
        tup1= (fname,lname,password,email, phone, province) 
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
    


if __name__ == '__main__':
    app.run(debug=True)


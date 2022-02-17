from app import db

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

# print(trip_20)
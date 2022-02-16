from app import db, trip

db.create_all()

trip_1 = trip('Toronto','Montreal')
trip_2 = trip('Toronto','Ottawa')
trip_3 = trip('Toronto','Vancouver')
trip_4 = trip('Toronto','Mississauga')
trip_5 = trip('Montreal','Toronto')
trip_6 = trip('Montreal','Ottawa')
trip_7 = trip('Montreal','Vancouver')
trip_8 = trip('Montreal','Mississauga')
trip_9 = trip('Ottawa','Toronto')
trip_10 = trip('Ottawa','Montreal')
trip_11 = trip('Ottawa','Vancouver')
trip_12 = trip('Ottawa','Mississauga')
trip_13 = trip('Vancouver','Toronto')
trip_14 = trip('Vancouver','Montreal')
trip_15 = trip('Vancouver','Ottawa')
trip_16 = trip('Vancouver','Mississauga')
trip_17 = trip('Mississauga','Toronto')
trip_18 = trip('Mississauga','Montreal')
trip_19 = trip('Mississauga','Ottawa')
trip_20 = trip('Mississauga','Vancouver')



db.session.add_all([trip_1, trip_2, trip_3, trip_4, trip_5, trip_6, trip_7,
                    trip_8, trip_9, trip_10, trip_11, trip_12, trip_13, trip_14, 
                    trip_15, trip_16, trip_17, trip_18, trip_19, trip_20])

db.session.commit()


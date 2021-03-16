import sqlite3

con=sqlite3.connect("bloodbank")
cur=con.cursor()

def request_blood(patient_name,age,bloodgroup,contact_number,address):
	values="insert into request_blood values(patient_name,age,bloodgroup,contact_number,address)values('{}','{}','{}','{}','{}')".format(patient_name,age,bloodgroup,contact_number,address)
	con.execute(values)
	con.commit()
	print("Your Order for bloodgroup",bloodgroup,"had been succesfully Placed")
def donar(donar_name,donar_boodgroup,contact_info):
	values="insert"

	print("Record had been added succesfully")
	

print("++++++++++++++++++++++++++++++++BLOODBANK MANAGEMENT SYSTEM++++++++++++++++++++++++++++++++")

auth=(input("Enter UserName:"))
passw=(input("Enter Password:"))
if(auth=="admin" and passw=="root"):
	print("To Request blood Enter 1:")
	print("To Donate blood Enter 2:")
	option=int(input("Enter Your Option:"))
	if(option==1):
		patient_name=(input("Enter Patient Name:"))
		age=(input("Enter Patient_age:"))
		bloodgroup=(input("Enter bloodgroup:"))
		contact_number=int(input("Enter patient contact number:"))
		address=(input("Enter patient Address:"))
		request_blood(patient_name,age,bloodgroup,contact_number,address)
	elif(option==2):
		print
		donar_name=(input("Enter Donar Name:"))
		donar_boodgroup=(input("Enter Donar Bloodgroup:"))
		contact_info=(input("Enter contact-Number:"))
		donar(donar_name,donar_boodgroup,contact_info)
elif(auth=="superadmin" and passw=="root"):
	print("To show Patient Records Enter 1:")
	print("To show donar records Enter 2:")
	opt2=int(input("Enter Your Option:"))
	if(opt2==1):
		rows=cur.fetchall()
		for row in rows:
			print(row)


else:
	print("++++++++++++++++++++++++Enter Valid UserName Or Password++++++++++++++++++++++++++++++++")




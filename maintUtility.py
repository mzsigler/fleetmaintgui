import sqlite3
import PySimpleGUI as sg

if __name__ == '__main__':
	conn = sqlite3.connect('maint.db')
	c = conn.cursor()

	c.execute('''CREATE TABLE cars (
		inv text,
		year integer,
		make text,
		model text,
		vin integer,
		cur_miles integer,
		fbrakes integer,
		rbrakes integer,
		oil integer
	)''')
	conn.commit()
	conn.close()

def car_adder():
	sg.theme("DarkBlue16")
	layout3 = [
		[sg.Text('*Inventory Number*'), sg.In(key='-INV-')],
		[sg.Text('*******Year*******'), sg.In(key='-YEAR-')],
		[sg.Text('*******Make*******'), sg.In(key='-MAKE-')],
		[sg.Text('*******Model******'), sg.In(key='-MODEL-')],
		[sg.Text('********VIN********'), sg.In(key='-VIN-')],
		[sg.Text('***Current Miles***'), sg.In(key='-CUR_MILES-')],
		[sg.Button('Save'), sg.Button('Quit')]
	]
	win3 = sg.Window('Car Adder', layout3)

	while True:
		events, values = win3.Read()
		win3.Refresh()
		if events in ('Save'):
			inv = (values['-INV-'])
			year = (values['-YEAR-'])
			make = (values['-MAKE-'])
			model = (values['-MODEL-'])
			vin = (values['-VIN-'])
			cur_miles = (values['-CUR_MILES-'])
			fbrakes = 0
			rbrakes = 0
			oil = 0
			conn = sqlite3.connect('maint.db')
			c = conn.cursor()

			c.execute(
				"INSERT INTO cars (inv, year, make, model, vin, cur_miles, fbrakes, rbrakes, oil) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
				(inv, year, make, model, vin, cur_miles, fbrakes, rbrakes, oil))

			print('****Database updated****')
			conn.commit()
			conn.close()
		if events in ('Quit', None):
			win3.close()
			break



def update_oil():
	sg.theme("DarkBlue16")
	layout5 = [
		[sg.Text('*Inventory Number*'), sg.In(key='-INV-')],
		[sg.Text('Last Oil Change Mileage'), sg.In(key='-OIL-')],
		[sg.Button('Save'), sg.Button('Quit')]
	]
	win5 = sg.Window('Update Latest Oil Change', layout5)

	while True:
		events, values = win5.Read()
		win5.Refresh()
		if events in ('Save'):
			inv = (values['-INV-'])
			oil = (values['-OIL-'])
			conn = sqlite3.connect('maint.db')
			c = conn.cursor()

			c.execute(""" UPDATE cars SET oil=? where inv=?""", (oil, inv))
			conn.commit()
			conn.close()
			print('****Database updated****')
		if events in ('Quit', None):
			win5.close()
			break

	
def update_current_miles():
	sg.theme("DarkBlue16")
	layout6 = [
		[sg.Text('*Inventory Number*'), sg.In(key='-INV-')],
		[sg.Text('New Mileage'), sg.In(key='-CUR_MILES-')],
		[sg.Button('Save'), sg.Button('Quit')]
	]
	win6 = sg.Window('Update Mileage', layout6)

	while True:
		events, values = win6.Read()
		win6.Refresh()
		if events in ('Save'):
			inv = (values['-INV-'])
			miles = (values['-CUR_MILES-'])
			conn = sqlite3.connect('maint.db')
			c = conn.cursor()

			c.execute(""" UPDATE cars SET cur_miles=? where inv=?""", (miles, inv))
			conn.commit()
			conn.close()
			print('****Database updated****')
		if events in ('Quit', None):
			win6.close()
			break
	
def update_frbrakes():
	sg.theme("DarkBlue16")
	layout7 = [
		[sg.Text('*Inventory Number*'), sg.In(key='-INV-')],
		[sg.Text('Last Front Brake Change Mileage'), sg.In(key='-FRBRAKES-')],
		[sg.Button('Save'), sg.Button('Quit')]
	]
	win7 = sg.Window('Update Front Brakes', layout7)

	while True:
		events, values = win7.Read()
		win7.Refresh()
		if events in ('Save'):
			inv = (values['-INV-'])
			fbrakes = (values['-FRBRAKES-'])
			conn = sqlite3.connect('maint.db')
			c = conn.cursor()

			c.execute(""" UPDATE cars SET fbrakes=? where inv=?""", (fbrakes, inv))
			conn.commit()
			conn.close()
			print('****Database updated****')
		if events in ('Quit', None):
			win7.close()
			break

def update_rrbrakes():
	sg.theme("DarkBlue16")
	layout8 = [
		[sg.Text('*Inventory Number*'), sg.In(key='-INV-')],
		[sg.Text('Last Rear Brake Change Mileage'), sg.In(key='-RRBRAKES-')],
		[sg.Button('Save'), sg.Button('Quit')]
	]
	win8 = sg.Window('Update Rear Brakes', layout8)

	while True:
		events, values = win8.Read()
		win8.Refresh()
		if events in ('Save'):
			inv = (values['-INV-'])
			rbrakes = (values['-RRBRAKES-'])
			conn = sqlite3.connect('maint.db')
			c = conn.cursor()

			c.execute(""" UPDATE cars SET rbrakes=? where inv=?""", (rbrakes, inv))
			conn.commit()
			conn.close()
			print('****Database updated****')
		if events in ('Quit', None):
			win8.close()
			break

	
def update_year():
	sg.theme("DarkBlue16")
	layout9 = [
		[sg.Text('*Inventory Number*'), sg.In(key='-INV-')],
		[sg.Text('New Model Year'), sg.In(key='-YEAR-')],
		[sg.Button('Save'), sg.Button('Quit')]
	]
	win9 = sg.Window('Update Year', layout9)

	while True:
		events, values = win9.Read()
		win9.Refresh()
		if events in ('Save'):
			inv = (values['-INV-'])
			year = (values['-YEAR-'])
			conn = sqlite3.connect('maint.db')
			c = conn.cursor()

			c.execute(""" UPDATE cars SET year=? where inv=?""", (year, inv))
			conn.commit()
			conn.close()
			print('****Database updated****')
		if events in ('Quit', None):
			win9.close()
			break
	
def update_make():
	sg.theme("DarkBlue16")
	layout10 = [
		[sg.Text('*Inventory Number*'), sg.In(key='-INV-')],
		[sg.Text('New Make'), sg.In(key='-MAKE-')],
		[sg.Button('Save'), sg.Button('Quit')]
	]
	win10 = sg.Window('Update Make', layout10)

	while True:
		events, values = win10.Read()
		win10.Refresh()
		if events in ('Save'):
			inv = (values['-INV-'])
			make = (values['-MAKE-'])
			conn = sqlite3.connect('maint.db')
			c = conn.cursor()

			c.execute(""" UPDATE cars SET make=? where inv=?""", (make, inv))
			conn.commit()
			conn.close()
			print('****Database updated****')
		if events in ('Quit', None):
			win10.close()
			break

def update_model():
	sg.theme("DarkBlue16")
	layout11 = [
		[sg.Text('*Inventory Number*'), sg.In(key='-INV-')],
		[sg.Text('New Model'), sg.In(key='-MODEL-')],
		[sg.Button('Save'), sg.Button('Quit')]
	]
	win11 = sg.Window('Update Model', layout11)

	while True:
		events, values = win11.Read()
		win11.Refresh()
		if events in ('Save'):
			inv = (values['-INV-'])
			model = (values['-MODEL-'])
			conn = sqlite3.connect('maint.db')
			c = conn.cursor()

			c.execute(""" UPDATE cars SET model=? where inv=?""", (model, inv))
			conn.commit()
			conn.close()
			print('****Database updated****')
		if events in ('Quit', None):
			win11.close()
			break

def update_vin():
	sg.theme("DarkBlue16")
	layout4 = [
		[sg.Text('Inventory Number'), sg.In(key='-INV-')],
		[sg.Text('New Vin'), sg.In(key='-VIN-')],
		[sg.Button('Save'), sg.Button('Quit')]
	]
	win4 = sg.Window('Update Vin', layout4)

	while True:
		events, values = win4.Read()
		win4.Refresh()
		if events in ('Save'):
			inv = (values['-INV-'])
			vin = (values['-VIN-'])
			conn = sqlite3.connect('maint.db')
			c = conn.cursor()

			c.execute(""" UPDATE cars SET vin=? where inv=?""", (vin, inv))
			conn.commit()
			conn.close()
			print('****Database updated****')
		if events in ('Quit', None):
			win4.close()
			break

	
def viewer():
	sg.theme("DarkBlue16")
	layout2 = [
		[sg.Text('*Inventory Number*'), sg.In(key='-INV-')],
		[sg.Button('View Info'), sg.Button('Exit')],
		[sg.Output(size=(50, 10))]
	]
	win2 = sg.Window('Car Viewer', layout2)

	while True:
		events, values = win2.Read()
		win2.Refresh()
		if events in ('View Info',):
			inv = (values['-INV-'])
			conn = sqlite3.connect('maint.db')
			c = conn.cursor()

			c.execute("""SELECT * FROM cars WHERE inv=?""", (inv,))
			records = c.fetchall()
			for row in records:
				print('Inventory number: ', row[0])
				print('Year: ', row[1])
				print('Make: ', row[2])
				print('Model: ', row[3])
				print('VIN: ', row[4])
				print('Current Miles: ', row[5])
				print('Last front brake change mileage: ', row[6])
				print('Last rear brake change mileage: ', row[7])
				print('Last oil change mileage: ', row[8])
		if events in ('Exit', None):
			win2.close()
			break



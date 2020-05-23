
from maintUtility import *
sg.theme('DarkBlue16')




layout = [[sg.Text('What would you like to do?', size=(50,2))],
		  [sg.Button('Add', size=(5, 7.5)), sg.Button('View', size=(5, 7.5)),
           sg.Button('Edit', size=(5, 7.5)), sg.Button('Done', size=(5, 7.5))],
          [sg.Combo(['Edit Vin', 'Edit Year', 'Edit Make', 'Edit Model',
            'Edit Oil', 'Edit Front Brakes', 'Edit Rear Brakes', 'Edit Current Miles'], key='combo', enable_events=True)],
		  [sg.Output(size=(80,10))]

		  ]



window = sg.Window('FleetMaint', layout, finalize=True)

window.Size = (640, 480)

while True:
	events, values = window.Read()
	window.Refresh()
	if events in ('Done', None):
		break
	if events in ('Add'):
		car_adder()
	if events in ('View'):
		viewer()
	if events == ('Edit'):
		if "Edit Vin" in values['combo']:
			update_vin()
		if 'Edit Year' in values['combo']:
			update_year()
		if 'Edit Make' in values['combo']:
			update_make()
		if 'Edit Current Miles' in values['combo']:
			update_current_miles()
		if 'Edit Front Brakes' in values['combo']:
			update_frbrakes()
		if 'Edit Rear Brakes' in values['combo']:
			update_rrbrakes()
		if 'Edit Model' in values['combo']:
			update_model()
		if 'Edit Oil' in values['combo']:
			update_oil()


window.close(); del window

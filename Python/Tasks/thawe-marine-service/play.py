import json
l = [{'type': 'Speed & Fuel consumption data', 'params': '["SOG (knots)", "SOW (knots)", "Total HFO consumption (mT)", "ME HFO Consumption (mT)", "GE HFO Consumption (mT)", "Boiler HFO consumption (mT)", "Total MGO consumption (mT)", "ME MGO Consumption (mT)", "GE MGO Consumption (mT)", "Boiler MGO consumption (mT)", "IGG MGO consumption (mT)", "ME SFOC (gm/kWhr)"]'}, {'type': 'Navigation parameters', 'params': '["Distance through Water (miles)", "Distance over Ground (miles)", "Vessel Heading", "Course over Ground", "Wind Speed (True)", "Wind Direction (True)", "Wave Height (Significant)", "Wave Direction (True)", "Current Speed", "Current Direction (True)", "Current Effect"]'}, {'type': 'ME parameters', 'params': '["ME shaft power (kW)", "ME RPM", "ME slip", "A/E 1 Power (kW)", "A/E 2 Power (kW)", "A/E 3 Power (kW)", "M/E RH", "A/E 1 RH", "A/E 2 RH", "A/E 3 RH", "Boiler 1 RH", "Boiler 2 RH"]'}, {'type': 'ROBs', 'params': '["HFO ROB (mT)", "MGO ROB (mT)", "LSFO ROB (mT)", "FW ROB (mT)", "CYL Oil ROB (liters)", "ME Sump LO ROB (litres)", "AE Sump LO ROB (litres)"]'}]
di={}

for i in l:
    di[i['type']] = json.loads(i["params"])


print(di)
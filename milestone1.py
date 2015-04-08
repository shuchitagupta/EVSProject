"""

EVS: Python Code

Group 4 { Apurba Mondal 	2013128,
         Chanchal Prajapati 2013030,
         Juhi Bhatnagar 	2013044 [Group Leader],
         Mohini Verma 		2013062,
         Prerna Singh 		2013149,
         Protichi Basak 	2013075,
         Ritvik Agarwal 	2013078,
         Saloni Gupta 		2013084,
         Shuchita Gupta 	2013101,
         Siddhant Sharma 	2013160,
         Simran Saxena 		2013104 }

"""

#MAP_QUALITY_INDICES = { 1 : "Good",
#                     2: "Moderate",
#                     3: "Unhealthy_Sensitive",
#                     4: "Unhealthy",
#                     5: "Very_Unhealthy",
#                     6: "Hazardous",
#                     7: "Hazardous"
#                    }


MAP_GASES_CONC = { "Ozone": [(0.000, 0.064), (0.065, 0.084), (0.085, 0.104), (0.105, 0.124), (0.125, 0.374), (-1, -1), (-1, -1)],
                  "ParticulateMatter2.5": [(0.0, 15.4), (15.5, 40.4), (40.5, 65.4), (65.5, 150.4), (150.5, 250.4), (250.5, 350.4), (350.5, 500.4)],
                  "ParticulateMatter10": [(0.0, 54.0), (55.0, 154.0), (155.0, 254.0), (255.0, 354.0), (355.0, 424.0), (425.0, 504.0), (505.0, 604.0)],
                  "CO": [(0.0, 4.4), (4.5, 9.4), (9.5, 12.4), (12.5, 15.4), (15.5, 30.4), (30.5, 40.4), (40.5, 50.4)],
                  "SO2": [(0.000, 0.034), (0.035, 0.144), (0.145, 0.224), (0.225, 0.304), (0.305, 0.604), (0.605, 0.804), (0.805, 1.004)],
                  "NO2": [(-1, -1), (-1, -1), (-1, -1), (-1, -1), (0.65, 1.24), (1.25, 1.64), (1.65, 2.04)]
    }
GAS_HIGHER_AQI = [50, 100, 150, 200, 300, 400, 500]
GAS_LOWER_AQI = [0, 51, 101, 151, 201, 301, 401]

def calculate_aqi(gas, conc):
    if gas not in MAP_GASES_CONC.keys():
        return -1		# this is a bad input
    bp_low = -1.0
    bp_high = -1.0
    i_low = -1.0
    i_high = -1.0
    temp_array = MAP_GASES_CONC[gas]
    index = -1
    for dummy_i in range(7):
        range_conc = temp_array[dummy_i]
        if conc > range_conc[0] and conc < range_conc[1]:
            index = dummy_i
            bp_low = range_conc[0]
            bp_high = range_conc[1]
            break
    i_low = GAS_LOWER_AQI[index]
    i_high = GAS_HIGHER_AQI[index]
    print index, bp_low, bp_high, i_low, i_high
    
    aqi = i_low + ((conc - bp_low) * (i_high - i_low) / (bp_high - bp_low))
    return aqi

print "**********\nTEST CASES\n**********\n"

print "Ozone, 0.077:"
print calculate_aqi("Ozone", 0.077)
print "---------------\n"
print "Ozone, 0.087:"
print calculate_aqi("Ozone", 0.087)
print "---------------\n"
print "Wrong name:"
print calculate_aqi("Ozon", 0.087)
print "---------------\n"
print "ParticulateMatter2.5, 54.4:"
print calculate_aqi("ParticulateMatter2.5", 54.4)
print "---------------\n"
print "CO, 8.4:"
print calculate_aqi("CO", 8.4)
print "---------------\n"


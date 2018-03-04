# -*- coding: cp1251 -*-
#enter the diameter of the shaft and verify the correctness of the input (number or not)
while 1:
    try:
        d = int(raw_input("Enter the shaft diameter value, mm: "))
        break
    except ValueError:
        print ("Need enter the number!")
#determine which key is used at a given diameter of the shaft
if 6 <= d < 8:
    shponka = {"b": 2, "h": 2, "t1": 1.2, "t2": 1.0}
elif 8 <= d < 10:
    shponka = {"b": 3, "h": 3, "t1": 1.8, "t2": 1.4}
elif 10 <= d < 12:
    shponka = {"b": 4, "h": 4, "t1": 2.5, "t2": 1.8}
elif 12 <= d < 17:
    shponka = {"b": 5, "h": 5, "t1": 3.0, "t2": 2.3}
elif 17 <= d < 22:
    shponka = {"b": 6, "h": 6, "t1": 3.5, "t2": 2.8}
elif 22 <= d < 30:
    shponka = {"b": 8, "h": 7, "t1": 4.0, "t2": 3.3}
elif 30 <= d < 38:
    shponka = {"b": 10, "h": 8, "t1": 5.0, "t2": 3.3}
elif 38 <= d < 44:
    shponka = {"b": 12, "h": 8, "t1": 5.0, "t2": 3.3}
elif 44 <= d < 50:
    shponka = {"b": 14, "h": 9, "t1": 5.5, "t2": 3.8}
elif 50 <= d < 58:
    shponka = {"b": 16, "h": 10, "t1": 6.0, "t2": 4.3}
elif 58 <= d < 65:
    shponka = {"b": 18, "h": 11, "t1": 7.0, "t2": 4.4}
elif 65 <= d < 75:
    shponka = {"b": 20, "h": 12, "t1": 7.5, "t2": 4.9}
elif 75 <= d < 85:
    shponka = {"b": 22, "h": 14, "t1": 9.0, "t2": 5.4}
elif 85 <= d < 95:
    shponka = {"b": 25, "h": 14, "t1": 9.0, "t2": 5.4}
elif 95 <= d < 110:
    shponka = {"b": 28, "h": 16, "t1": 10.0, "t2": 6.4}
elif 110 <= d < 130:
    shponka = {"b": 32, "h": 18, "t1": 11.0, "t2": 7.4}
else:
    print("The shaft diameter is outside the standard dimensions for the keyed connection")
    raw_input("Press any key to exit.")
    exit()
print ("Width of key = " + str(shponka["b"]) + " mm, key height = " + str(shponka["h"]) + " mm, the depth of the groove on the shaft = " + str(shponka["t1"]) + " mm, the depth of the groove in the sleeve = " + str(shponka["t2"]) + " mm")
while 1:
    try:
        material = raw_input("Specify the type of hub material: steel (1) or cast iron (2). ")
        break
    except ValueError:
        print ("Choose one of the proposed material options by entering the desired number.")
if material == "1":
    dopysk_napr = 130 
elif material == "2":
    dopysk_napr = 80 
else:
    print("Invalid material type specified!")
    raw_input("Press any key to exit")
    exit()
#enter the value of the moment acting on the connection and verify the correctness of the input
while 1:
    try:
        moment = float(raw_input("Enter the value of the torque acting on the connection in Nm: "))
        break
    except ValueError:
        print ("It is necessary to enter a numerical value of the moment acting on the connection!")
#enter the value of the key length and verify the correctness of the input
while 1:
    try:
        l = float(raw_input("Enter the length of the key in mm: "))
        break
    except ValueError:
        print ("You must enter a number!")
l_work = l - shponka["b"]
napr = (2 * 1000 * moment) / (d * l_work * (shponka["h"] - shponka["t1"]))
if napr <= dopysk_napr:
    print("Stresses in the keyed joint make up " + str(napr) + " N / mm ^ 2. Allowable stresses are " + str(dopysk_napr) + " N / mm ^ 2.")
    raw_input("Press any key to exit")
    exit()
else:
    print("This key is not suitable for these parameters! Voltages exceed the hubs permitted for this material!")
    #calculate the required working length of the key
    l_work_rek = (2 * 1000 * moment) / ((dopysk_napr - 20) * d * (shponka["h"] - shponka["t1"]))
    #calculate the required length of the key, taking into account the rounding
    l_rek = l_work_rek + shponka["b"]
    #tension when using recommended length keys
    napr_rek = (2 * 1000 * moment) / (d * l_work_rek * (shponka["h"] - shponka["t1"]))
    print("It is recommended to increase the key to " + str(l_rek) + " mm. In this case, the stresses are " + str(napr_rek) + " N / mm ^ 2.")
    raw_input("Press any key to exit")
    exit()

def main():
    #input parameters and get gear ratio, top speed and acceleration
    
    hp = 6.5
    ERPM = 3600
    Etorque = hp * 5252 / ERPM
    print(f"Engine Torque: {Etorque:.2f} ftlbs @ {ERPM} RPM")
    idle = 1800             # +-150 rpm
    #Etorque = 8.1           # ftlbs @ 2500 RPM
    Wheeldiameter = 1.25    # ft = 15 inches
    wheel_circumference = Wheeldiameter * 3.14159       
    g = .85 # gear efficency 
    m = 145 #kg 

    gearto(ERPM, Etorque, Wheeldiameter, wheel_circumference, g, m)

    ERPM = 2500
    Etorque =8.1              # ftlbs @ 2500 RPM
    Wheeldiameter = 1.25    # ft = 15 inches
    wheel_circumference = Wheeldiameter * 3.14159       
    g = .85 # gear efficency 
    m = 145 #kg 
    
    gearto(ERPM, Etorque, Wheeldiameter, wheel_circumference, g, m)
    
def gearto(ERPM, Etorque, Wheeldiameter, wheel_circumference, g, m):
    i = 0.1
    while i < 1:
        gear_ratio = i
        RPM = ERPM / gear_ratio
        torque = Etorque * gear_ratio
        force = (torque * g)/(Wheeldiameter/2)               # force in lbf
        newtons = force * 4.44822                            # force in newtons
        top_speed = (RPM * wheel_circumference * 60) / 5280
        acceleration = (newtons / m)*3.28084                 # acceleration in ft/s^2
        horsepower = (torque * RPM) / 5252
        timetotop = (top_speed * 5280 / 3600) / acceleration
        print(f"Gear Ratio: {gear_ratio:.2f}, Top Speed: {top_speed:.2f} mph, Acceleration: {acceleration:.2f} ft/s^2, Horsepower: {horsepower:.2f}")
        i += 0.1

    i = 1
    while i < 10:
        gear_ratio = i
        RPM = ERPM / gear_ratio
        torque = Etorque * gear_ratio
        top_speed = (RPM * wheel_circumference * 60) / 5280
        force = (torque * g)/(Wheeldiameter/2)               # force in lbf
        newtons = force * 4.44822                            # force in newtons
        acceleration = (newtons / m)*3.28084                 # acceleration in ft/s^2

        #acceleration = (torque * 5252) / (Wheeldiameter * 12 * 32.174)
        horsepower = (torque * RPM) / 5252
        timetotop = (top_speed * 5280 / 3600) / acceleration
        print(f"Gear Ratio: {gear_ratio:.2f}, Top Speed: {top_speed:.2f} mph, Acceleration: {acceleration:.2f} ft/s^2, Horsepower: {horsepower:.2f}, Time to Top Speed: {timetotop:.2f} s")
        i += 0.5
main()    
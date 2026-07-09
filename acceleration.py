def main():
    ERPM = 3600
    #idle = 1800             # +-150 rpm
    Etorque = 8           # ftlbs @ 2500 RPM
    Wheeldiameter = 1.25    # ft = 15 inches
    wheel_circumference = Wheeldiameter * 3.14159       
    
    gearratio = 5.5
    g = .85 # gear efficiency 
    grav = 32.2 #
    m = 300 #lbs 

    RPM = ERPM / gearratio
    frictionconst = .03
    friction = -frictionconst * m

    force = (Etorque * gearratio * g)/(Wheeldiameter/2)               # force in lbf at wheel

    top_speed = (RPM * wheel_circumference )/60 # top speed in ft/sec
    print(f"Top Speed: {top_speed:.2f} ft/sec")  
    v0 = 0
    a = ((force + friction)/m)*32.174
    #i = 0
    t = 0
    v = 0
    dt = 0
    print("Topspeed in meters:", top_speed/3.28)
    netforce = force + friction
    while v < top_speed:                    # convert top speed to m/s
        v_mps = v * 0.3048
        #v = (v0 + a*dt) 
        #v = v * 3.28

        forcedrag = -(.5* .8 * 1.225 * (v_mps**2)* 1)/4.448          # convert to lbf after calculating in newtons
        netforce = force + forcedrag + friction          #lbf
        a = ((netforce)/m)*32.174                        #ft/s^2  
               # 
        v0 = v_mps
        print(f"Time: {t:.1f} s, Velocity: {v:.2f} ft/s, Acceleration: {a:.2f} ft/s^2, NetForce: {netforce:.2f} lbf, Drag: {forcedrag:.2f} lbf") 
        #i += 1
        v = v + a*dt
        dt=.1
        t += dt
        if v >= top_speed or netforce <= 0:
            break

    # to stop in 3 secs, net force required, a = -14.3ft/s^2
    print(v)
    t = 4
    netforce = -((v/t)*m)/grav
    dt = 0
    while v > 0:
        v_mps = v * 0.3048
        forcedrag = -(.5* .8 * 1.225 * (v_mps**2)* 1)/4.448   
        forcebrake = -netforce + forcedrag + friction
        a = ((netforce)/m)*32.174
        print(f"Time: {t:.1f} s, Velocity: {v:.2f} ft/s, Acceleration: {a:.2f} ft/s^2, NetForce: {netforce:.2f} lbf, Drag: {forcedrag:.2f} lbf", f"BrakeForce: {forcebrake:.2f} lbf") 
        v = v + a*dt
        dt=.1
        t -= dt
        netforce = -((v/t)*m)/grav
        if v < 0 or netforce >= 0:
            break
    print(f"Time: {t:.1f} s, Velocity: {v:.2f} ft/s, Acceleration: {a:.2f} ft/s^2, NetForce: {netforce:.2f} lbf, Drag: {forcedrag:.2f} lbf", f"BrakeForce: {forcebrake:.2f} lbf")

    FOSBrake = 1.5
    brakereq = FOSBrake * forcebrake
    print(f"Required Brake Force = {brakereq:.2f} with Factor of Safety: {FOSBrake:.2f}")










main()
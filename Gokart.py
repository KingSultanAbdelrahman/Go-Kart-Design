from math import pi, acos, degrees, atan, sqrt, tan, radians
def main():
    print("Gokart.py")
    
    # Calculating front axle link angle 
    # Constant values for the front axle A, B: do not change.
    

    m = 300             # lbs
    mew = 0.8            # static coefficient of friction
    g = 32.174          # ft/s^2
    h = 15/12              # vertical com

    w = 40              # distance between front kingpins/top pivots 
    winft = 40/12
    s = 37              # Steering rack/ Tierod Length
    y = 3               # distance from front axle to steering rack in nuetral straight tires
    l = 70              # length of back wheel to front wheel


    x = w - s
    strwheel = x/2                             # x distance in nuetral wheel position from kingpin to tie rod
    r = sqrt(strwheel**2 + y**2)               # Steering arm link length (distance from kingpin to tie rod)
          
    #print(f"r: {r:.1f}", end = " ")

    thetacenter = acos( strwheel / r)             # Left linkage angle for a straight wheel
    phicenter = acos( strwheel / r)                # Right linkage angle for a straight wheel
    


    i = 0.0             # increments through the distance between the kingpins (w-s) 
                        # to calculate the angles of the steering linkages and wheels

    max_i = r - strwheel     #
    while i < max_i :                       # calculates the angles of the steering linkages and wheels for a right turn
        leftx = strwheel - i                # left kingpin to tie rod distance
        rightx = strwheel + i               # right kingpin to tie rod distance
        
        leftlinkangle = acos (leftx / r)        # left linkage angle for a right turn
        rightlinkangle = acos (rightx / r)       # right linkage angle for a right turn
        
        print(f"Rack shift i: {i:.2f} ")
        print(f"Left Link Angle: {degrees(leftlinkangle):.1f} ", end = " ")
        print(f"Right Link Angle: {degrees(rightlinkangle):.1f} ", end = " ")
        
        wheelleft = degrees(leftlinkangle - thetacenter)
        wheelright = degrees(phicenter-rightlinkangle)
        print(f"Wheel Left: {wheelleft:.1f} ", end = " ")
        print(f"Wheel Right: {wheelright:.1f} ")

        if wheelleft > 0 and wheelright > 0 and wheelleft < 30 and wheelright < 30:  # only calculate if the wheels are within a reasonable range
            # For a right turn:
            # right wheel = inside wheel
            # left wheel = outside wheel
            Rfromin = (l / tan(radians(abs(wheelright)))) + w/2    # Inner turning radius of the gokart in inches
            Rfromout = (l / tan(radians(abs(wheelleft)))) - w/2      # Outer turning radius of the gokart in inches
            RCOM = ((Rfromin + Rfromout) / 2)/12
            print(f"Centerline Turn Radius from inner: {Rfromin/12:.1f} ft", end = " ")   #  convert to feet
            print(f"Centerline Turn Radius from outer: {Rfromout/12:.1f} ft", end = " ")   # convert to feet 

            #rtol = abs(Rin/l)
            #print(f"Rin/l: {rtol:.1f} ")
            ackermantheory = w/l
            ackermanact = (1/tan(radians(abs(wheelleft)))) - (1/tan(radians(abs(wheelright))))
            percenterror = ((ackermanact - ackermantheory) / ackermantheory) * 100
            print(f"Ackerman Theory: {ackermantheory:.4f} ", end = " ")
            print(f"Ackerman Actual: {ackermanact:.4f} ", end = " ")
            print(f"Percent Error: {percenterror:.2f}%")  
            
            maxslidespeed = sqrt(mew*g*RCOM)
            maxtipspeed = sqrt((g*winft*RCOM)/(2*h))
            FOS = 1.25
            allowablespeed = maxslidespeed/FOS
            
            print(f"Allowable speed with FOS = {FOS:.2f}: {allowablespeed:.1f} ft/s = {allowablespeed/1.46667:.1f} mph")
            print(f"maxslidespeed: {maxslidespeed:.1f} ft/s = {maxslidespeed/1.46667:.1f} mph")
            print(f"maxtipspeed: {maxtipspeed:.1f} ft/s = {maxtipspeed/1.46667:.1f} mph")
            #maxslidespeed = sqrt(mew*g*RCOM)
            #maxtipspeed = sqrt((g*w*RCOM)/(2*h))
            

            #for v in range(0, 100, 1): # mph
           #     v = v * 1.46667 # convert to ft/s
            #    slide = (v**2)/(g*RCOM)
           #     tip = (m*h*v**2)/(g*RCOM)
           #     print(f"Speed: {v/1.46667:.1f} mph, Slide: {slide:.2f} ft")

                #if slide >= mew:
                 #   print(f"slide detected at v: {v/1.46667:.1f} mph!")
                  #  print("Turn radius COM:", RCOM)
                   # print(f"Wheel Left: {wheelleft:.1f} ", end = " ")
                    #print(f"Wheel Right: {wheelright:.1f} ")
                    #break
                #if tip >= mresist:
                 #   print(f"tip detected at v: {v/1.46667:.1f} mph!") 
                  #  print(f"Wheel Left: {wheelleft:.1f} ", end = " ")
                   # print(f"Wheel Right: {wheelright:.1f} ")
                    #break

            if abs(percenterror) > 10:
                print("Significant Ackerman error detected!")
                print(f"percenterror: {percenterror:.1f}")
             
        i += 0.25
    
    # at max angle of wheel, what is turn radius of the gokart?
    ssf = (w/12)/(2*h) # static stability factor
    print(f"Static Stability Factor: {ssf:.2f}")
    
    


main()
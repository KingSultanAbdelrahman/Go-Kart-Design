from math import pi, acos, degrees, atan, sqrt, tan, radians
def main():
    print("Gokart.py")
    
    # Calculating front axle link angle 
    # Constant values for the front axle A, B: do not change.
 
    w = 10              # distance between front kingpins/top pivots 
    s = 8              # Steering rack/ Tierod Length
    #y = 3               # distance from front axle to steering rack in nuetral straight tires
    l = 70              # length of back wheel to front wheel

    x = w - s
    strwheel = x/2                             # x distance in nuetral wheel position from kingpin to tie rod
    r = x+sqrt(5**2)               # Steering arm link length (distance from kingpin to tie rod)
          
    print(f"r: {r:.1f}", end = " ")

    thetacenter = acos( strwheel / r)               # Left linkage angle for a straight wheel
    phicenter = 180- degrees(acos( strwheel / r))   # Right linkage angle for a straight wheel

    i = 0.0             # increments through the distance between the kingpins (w-s) 
                        # to calculate the angles of the steering linkages and wheels

    
    while i <= x :
        print("x:", i, end = " ")
        theta = acos (i / r)
        #print("delta x: ", i, end = " ")
        #print("theta: ", degrees(theta), end = " ")
        
        phi = acos ( (x-i) / r )
        #print("phi:", degrees(phi))
        
        phiunmirr = 180-degrees(phi)

        #print("phiunmirr:", phiunmirr, end = " ")
        wheelleft = degrees(theta - thetacenter)
        wheelright = phiunmirr - phicenter
        print(f"wheelleft:{wheelleft:.1f} ", end = " ")
        print(f"wheelright:{wheelright:.1f}")
        i += 0.25   

    # at max angle of wheel, what is turn radius of the gokart?


    Rout = (l / tan(radians(abs(wheelright)))) + w/2
    Rin = (l / tan(radians(abs(wheelleft)))) - w/2
   
    print(f"Rin: {Rin:.1f} ", end = " ")
    print(f"Rout: {Rout:.1f}", end = " ")

    rtol = abs(Rin/l)
    print(f"Rin/l: {rtol:.1f} ")
    ackermantheory = w/l
    print("cot out: ", 1/tan(radians(abs(wheelright))), end = " ")
    print("cot in: ", 1/tan(radians(abs(wheelleft))), end = " ")
    print("wheel right: ", wheelright, end = " ")
    print("wheel left: ", wheelleft)

    ackermanact = (1/tan(radians(abs(wheelright)))) - (1/tan(radians(abs(wheelleft))))
    percenterror = ((ackermantheory - ackermanact) / ackermanact) * 100
    print(f"ackermantheory: {ackermantheory:.4f} ", end = " ")
    print(f"ackermanact: {ackermanact:.4f} ", end = " ")
    print(f"percenterror: {percenterror:.2f}%")
    
    A = 0 # never moves
    B = w # never moves
    C = A
    D = s
    


main()
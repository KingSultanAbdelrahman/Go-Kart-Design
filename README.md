# Go-Kart-Design

## Project Goal 
A ground-up go-kart design project focused on steering geometry, drivetrain sizing, braking torque, rollover limits, and turning performance using Python, CAD, and engineering analysis.

## Engineering Requirements 
1. Kart shall accelerate from 0 to 30 mph in 10–12 seconds with a 160–200 lb driver.
Solved by back engineering required engine force on wheel and python code acceleration at 5.5 gear ratio   
3. Kart shall stop from 30 mph to 0 in ≤ 3 seconds on dry pavement.
4. Kart shall complete 5 repeated 30-to-0 mph stops without brake fade or mechanical failure.
5. Front steering geometry shall be within ±10–15% of ideal Ackermann angles across the normal steering range.
6. Low-speed 10 mph turning radius shall be ≤ 12.5 ft.
7. Kart shall not tip during steady-state turning at design cornering speed, with stability factor ≥ 1.3–1.5.
8. Chassis shall meet FOS ≥ 2 against yield for vertical bump, braking, and lateral cornering load cases.
9. Braking torque at the wheel shall be ≥ 2× engine idle drive torque at the wheel.
10. Throttle shall automatically return to idle within 1 second after release.
11. Kart shall include driver-accessible and external kill switches.
12. Chain and sprockets shall be guarded from driver contact.
13. Chain alignment error shall be ≤ 1–2 mm, with adjustable chain tension.
14. Driven sprocket shall be swappable in ≤ 15 minutes using common tools.
15. Kart shall complete a 30-minute endurance test with no critical failures.
16. Measured acceleration, top speed, and braking performance shall match predictions within ±15–20%.
17. Final deliverables shall include CAD assembly, drawings, BOM, calculations, test plan, test data, and design review report.
## Engineering Design Decisions 

### Steering 
#### 1. Steering Geometry
#### 2. Wheelbase Track Width
#### 3 Tierod-placement
#### 4 Spindle and Kingpin Design
#### 5 Frame Mounting Points

### Stability and Rollover
- Center of mass height estimate
- Track width effect on tipping
- Tipping moment vs resisting moment
- Maximum safe cornering speed

For a vehicle to make a turn, a frictional force is exerted by the tires to move the vehicle in the direction the wheel points. This frictional force must at a minimum equal or exceed the opposing centrifugal "force" to make the turn without sliding or skidding of the tire.  

$$
Ff = μ m g
$$

$$
Fc = \frac{mv^2}{r}
$$
$$
μ m g >= \frac{m v^2}{ r}
$$

where: 
- \( F_c \) = required centripetal force
- \( m \) = vehicle mass
- \( v \) = vehicle speed
- \( r \) = turn radius

The maximum velocity a gokart can go prior to sliding is thus:

$$
v = \sqrt{μ g r}
$$

For a vehicle to not roll over or tip while making a turn, net torque must equal zero. 

$$
m g T/2 >= Fc h
$$

The maximum velocity a gokart can go prior to tipping is: 

$$
v = \sqrt{\frac{g T r}{2 h}}
$$

### Drivetrain
- Engine torque and RPM assumptions

The net force required on the gokart to reach 30mph or 44ft/s in 12 secs, is:   

$$
F_{net} = a_{net} m = \frac{vm}{t} = \frac{44 * m}{12} = 34.31lbf
$$

$$
F_{net} = F_{wheel} - F_{rolling} - F_{drag}
$$

where: 
- \( F_{wheel} \) = required forward force felt by the wheel

$$
F_{drag} = \frac {C_{d} ρ A v^2}{2} 
$$

where: 
- \( C_{d} \) = drag coefficent
- \(ρ \) = density of air
- \(A \) = surface area of gokart front
- \(v \) = velocity

Assumping ρ = 0.0765 lb/ft³, C_{d} = .8, A = 1 m^2 = 10.76 ft^2. as v increases, F_{d} grows and resists acceleration of the gokart.  At max speed v= 30mph, 44ft/s 

$$
F_{drag} = 20lbf  
$$

Assuming rolling friction coffeicent = 0.03 and W = 300lbs

$$
F_{rolling} = 0.03 * 300 = 9lbf
$$

$$
F_{wheel} = F{net} + Ffrolling = 43.3lbf 
$$

The force felt by the wheel is: 

F_{wheel} = \frac{T{engine} * G * η}{r}

where: 
- \( T_{engine} \) = Engine Torque
- \( G ) = Gear Ratio
- \( η ) = Gear Ratio Efficency
- \( r ) = Driven Wheel Radius  

The maximum torque of a Predator 212 engine is 8.1 ftlbs 
  
- Gear ratio selection
- Wheel torque calculation
- Estimated top speed under load

### Braking System
- Required braking torque
- Wheel lockup condition
- Tire-road friction limit
- Brake force distribution considerations
### Chassis Geometry 
#### Center of Mass, Sliding and Tipping Prevention 

### Frame and Chassis
- Wheelbase and track width selection
- Mounting points
- Structural packaging
- CAD model development

## 5. CAD and Analysis
Include screenshots, drawings, dimensions, and calculations.

## 6. Build Process
Show what changed from CAD to real life.

## 7. Testing
Compare theoretical vs actual results.

## 8. Lessons Learned
What failed, what improved, and what you would redesign.

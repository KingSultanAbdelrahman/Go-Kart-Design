# Go-Kart-Design

## Project Goal 
A ground-up go-kart design project focused on steering geometry, drivetrain sizing, braking torque, rollover limits, and turning performance using Python, CAD, and engineering analysis.

## Engineering Requirements 
1. Kart shall accelerate from 0 to 30 mph in 10–12 seconds with a 160–200 lb driver.
2. Kart shall stop from 30 mph to 0 in ≤ 3 seconds on dry pavement.
3. Kart shall complete 5 repeated 30-to-0 mph stops without brake fade or mechanical failure.
4. Front steering geometry shall be within ±10–15% of ideal Ackermann angles across the normal steering range.
5. Low-speed 10 mph turning radius shall be ≤ 12.5 ft.
6. Kart shall not tip during steady-state turning at design cornering speed, with stability factor ≥ 1.3–1.5.
7. Chassis shall meet FOS ≥ 2 against yield for vertical bump, braking, and lateral cornering load cases.
8. Braking torque at the wheel shall be ≥ 2× engine idle drive torque at the wheel.
9. Throttle shall automatically return to idle within 1 second after release.
10. Kart shall include driver-accessible and external kill switches.
11. Chain and sprockets shall be guarded from driver contact.
12. Chain alignment error shall be ≤ 1–2 mm, with adjustable chain tension.
13. Driven sprocket shall be swappable in ≤ 15 minutes using common tools.
14. Kart shall complete a 30-minute endurance test with no critical failures.
15. Measured acceleration, top speed, and braking performance shall match predictions within ±15–20%.
16. Final deliverables shall include CAD assembly, drawings, BOM, calculations, test plan, test data, and design review report.
## Engineering Design Decisions 

### Steering 
#### 1. Steering Geometry
#### 2. Wheelbase Track Width
#### 3 Tierod-placement
#### 4 Spindle and Kingpin Design
#### 5 Frame Mounting Points

### Chassis Geometry 
#### Center of Mass, Sliding and Tipping Prevention 
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

The maximum velocity a gokart can go prior to sliding is thus:

$$
v = \sqrt{μ g r}
$$
For a vehicle to not roll over or tip while turning, net torque must equal zero. 

$$
m g T/2 = Fc h
$$

### Brakes 
#### Controlled & Effective Stop 

## 5. CAD and Analysis
Include screenshots, drawings, dimensions, and calculations.

## 6. Build Process
Show what changed from CAD to real life.

## 7. Testing
Compare theoretical vs actual results.

## 8. Lessons Learned
What failed, what improved, and what you would redesign.

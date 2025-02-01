def pcalc(density,depth):
    p=density*g*depth
    return p

density=int(input("Enter density here:"))
depth=int(input("Enter depth in Metres here:"))
pressure=pcalc(density,depth)
print(f"The pressure calculated is: {pressure} Pa")

def ecalc(m):
    E=m*c**2
    return E
mass=float(input("Enter mass in kg here:"))
er=ecalc(mass)
print(f"The energy released is {er} J")

def kcalc(mass,velocity):
    K=(1/2)* mass*velocity**2
    return K
mass=float(input("Enter mass of object in kg here:"))
velocity=float(input("Enter velocity of object in m/s here:"))
Ke=kcalc(mass,velocity)
print(f"The kinetic energy output is {Ke} J")

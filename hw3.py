import math
try:
    angle_deg = float(input("Enter the angle in degrees: "))
    angle_rad = math.radians(angle_deg)
    sin_val = math.sin(angle_rad)
    cos_val = math.cos(angle_rad)
    tan_val = math.tan(angle_rad)

    print("sin(", angle_deg, ") =", sin_val)
    print("cos(", angle_deg, ") =", cos_val)
    print("tan(", angle_deg, ") =", tan_val)

except ValueError:
    print("Error: Please enter a valid number for the angle.")
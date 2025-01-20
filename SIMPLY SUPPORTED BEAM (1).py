import math

Job_No = int(input('Job no. :  '))
Job_title = input('Job title: ')
Subject = input('Subject: ')
Client = input('Client: ')
Made_by = input('Made by: ')
Checked_by = input('Checked by: ')
Date = input('Date: ')

print('1. ACTIONS AND SUPPORT TYPE')
g1 = int(input('1.1 Permanent Actions(g1, kN/m): '))
q1 = int(input('1.2 Variable Actions(q1, kN/m): '))
Support = input('Support type: ')
print('--------------------------------------------------------------------------------------------------')

print('2. PARTIAL FACTORS FOR ACTIONS')
γg1 = float(input('γg1= '))
γq1 = float(input('γq1= '))
print('--------------------------------------------------------------------------------------------------')

print('3. LOAD COMBINATION FOR ULS')
W = γg1 * g1 + γq1 * q1  # Calculate Load Combination for ULS
print(f'Load combinations for ULS= {W:.2f} kN/m')
print('--------------------------------------------------------------------------------------------------')

print('4. DESIGN BENDING MOMENT AND SHEAR FORCES')
L = float(input('Span of beam= '))

print('Maximum bending moment occurs at mid span, maximum shear force occurs at supports')
M = (W * L**2) / 8  # Design bending moment
Vs = (W * L) / 2  # Design shear force
print(f'Design bending moment = {M:.2f} kN-m')
print(f'Design shear force at supports = {Vs:.2f} kN')
print('--------------------------------------------------------------------------------------------------')

print('5. CROSS SECTION PROPERTIES')
beam_section = input('Beam section: ')
h = float(input('Depth(mm)= '))
b = float(input('Width(mm)= '))
tw = float(input('Web thickness(mm)= '))
tf = float(input('Flange thickness(mm)= '))
r = float(input('Root radius(mm)= '))
d = float(input('Depth between flange fillets(mm)= '))
iy = float(input('Second moment of area, y-y axis(cm^4)= '))
Wply = float(input('Plastic modulus, y-y axis(cm^3)= '))
A = float(input('Area(cm^2)= '))
E = float(input('Modulus of elasticity(n/mm^2)= '))
fy = float(input('Yield strength(n/mm^2)= '))

ε = math.sqrt(235 / fy)
print(f'ε = {ε:.2f}')

print('--------------------------------------------------------------------------------------------------')
print('6. CROSS SECTIONAL RESISTANCE')
print('6.1 SHEAR BUCKLING CHECK- VERIFIED ACCORDING TO SECTION 5 OF BSEN 1993-1-5')

hw = h - (2 * tf)
η = 1.0
if hw / tw > (72 * ε) / η:
    print('Shear buckling resistance for webs should be verified since (hw/tw) > (72*ε)/η')
else:
    print('Shear buckling resistance of the web does not need to be verified since (hw/tw) < (72*ε)/η')

print('.................................................')

# Shear Resistance Check
print('6.2 SHEAR RESISTANCE CHECK')
Av = (A - 2 * b * tf) + (tf * (tw + 2 * r))
Ax = η * hw * tw
Vr = min(Av, Ax) * (fy / math.sqrt(3))
print(f'Vr = {Vr:.2f} kN')

if Vs / Vr < 1:
    print('Shear resistance of the section is adequate since (Vs/Vr) < 1')
else:
    print('Shear resistance of the section is inadequate since (Vs/Vr) > 1')
print(Vs / Vr)

print('.................................................')

# Bending Resistance Check
print('6.3 BENDING RESISTANCE CHECK')
M_crd = (Wply * fy) / 1e6  # Design bending resistance
print(f'M_crd = {M_crd:.2f} kNm')

if M > M_crd:
    print('Since M > M_crd, bending moment resistance is inadequate')
else:
    print('Since M < M_crd, bending moment resistance is adequate')

print('--------------------------------------------------------------------------------------------------')

# Vertical Deflection Check
print('7. VERTICAL DEFLECTION CHECK AT SERVICEABILITY LIMIT STATE')
W_T = g1 + q1  # Total load
print(f'W_L, Total Load = g1 + q1 = {W_T:.2f} kN/m')

deflection = (5 * W_T * L**4) / (384 * E * iy)
print(f'Vertical Deflection = δ = {deflection:.2f} mm')

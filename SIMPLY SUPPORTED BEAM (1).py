Job_No=int(input('Job no. :  '))
Job_title=input('Job title: '  )
Subject=input('Subject: ')
Client=input('Client: ')
Made_by=input('Made by: ')
Checked_by=input('Checked by: ')
Date=input('Date: ')


print('1. ACTIONS AND SUPPORT TYPE')
g1=int(input('1.1 Permanent Actions(g1, kN/m): '))
q1=int(input('1.2 Variable Actions(q1, kN/m): '))
Support=input('Support type: ')
print('--------------------------------------------------------------------------------------------------')

print('2. PARTIAL FACTORS FOR ACTIONS')
γg1=float(input('γg1= '))
γq1=float(input('γq1= '))
print('--------------------------------------------------------------------------------------------------')

print('3. LOAD COMBINATION FOR ULS')
W=print('Load combinations for ULS= ', float(float(γg1)*g1+float(γq1)*q1))
W=float(float(γg1)*g1+float(γq1)*q1)
print('--------------------------------------------------------------------------------------------------')

print('4. DESIGN BENDING MOMENT AND SHEAR FORCES')
L=float(input('Span of beam= '))

print('Maximum bending moment occurs at mid span, maximum shear force occurs at supports')
#W=None
#if W==None:
     #W=65.25
M=print('Design bending moment=(W*(L*L)/8)=  ', (W*(L*L)/8), 'kn-m')

print('Maximum design shear force at supports,')
Vs=print('Design shear force at supports=(W*L)/2)=  ', ((W*L)/2), 'kn')
Vs=((W*L)/2)
print('--------------------------------------------------------------------------------------------------')

print('5. CROSS SECTION PROPERTIES')
beam_section=input('Beam section: ')
h=input('Depth(mm)= ')
b=input('Width(mm)= ')
tw=input('Web thickness(mm)= ')
tf=input('Flange thickness(mm)= ')
r=input('Root radius(mm)= ')
d=input('Depth between flange fillets(mm)= ')
iy=input('Second moment of area, y-y axis(cm^4)= ')
Wply=input('Plastic modulus, y-y axis(cm^3)= ')
A=input('Area(cm^2)= ')
E=input('Modulus of elasticity(n/mm^2)= ')
fy=input('Yield strength(n/mm^2)= ')
import math
ε=math.sqrt(235/int(fy))
print('ε= ', ε)

print('--------------------------------------------------------------------------------------------------')
print('6. CROSS SECTIONAL RESISTANCE')
print('6.1 SHEAR BUCKLING CHECK- VERIFIED ACCORDING TO SECTION 5 OF BSEN 1993-1-5')

hw=(float(h))-((2*float(tf)))
η=1.0

if (float(hw)/float(tw))>(72*ε)/(η):
     print('Shear buckling resistance for webs should be verified since (hw/tw)>(72*ε)/η')
else:
     print('Shear buckling resistance of the web does not need to be verified since (hw/tw)<(72*ε)/η')
     
print('.................................................')

print('6.2 SHEAR RESISTANCE CHECK')
print('Vr is the design plastic shear resistance')
print('Vr=[Av(fy/√3)]/γM0')
print('Av or Ax is shear area with the load applied parallel to the web')


Av=(float(A)-(2*float(b))*float(tf))+(float(tf)*(float(tw)+(2*float(r))))
Ax=(float(η)*float(hw)*float(tw))
print('Av= ',Av)
print('Ax= ',Ax)
Vr=float(Av)*(float(fy)/math.sqrt(3))

if Av>Ax:
     Vr=float(Av)*(float(fy)/math.sqrt(3))
else:
     Vr=float(Ax)*(float(fy)/math.sqrt(3))
     
print('Vr=(Av)*(fy)/sqrt(3) ',Vr, 'kN')

if ((Vs)/(Vr)) <float(1):
     print('Shear resistance of the section is adequate since (Vs/Vr)<1')
else:
     print('Shear resistance of the section is inadequate since (Vs/Vr)>1')
print(Vs/Vr)

print('.................................................')

print('6.3 BENDING RESISTANCE CHECK')
print('M_crd is the design resistance for bending for class 1& 2 sections')
print('Bending resistance of the section is adequate if M/M_crd<1')
print('At the point of maximum bending moment, at mid span, if (Vr/2)>Vs, bending resistance is not reduced by shear force')
print('Vr/2=',float(Vr/float(2)))
x=Vr/2
if x>Vs:
     print('Since (Vr/2)>Vs,bending resistance is not reduced by shear force')
else:
     print('Since (Vr/2)<Vs,bending resistance is reduced by shear force')

print('M_crd = (Wply*fy)')
M_crd=int(Wply)*int(fy)/(1e6)
print('Design bending resistance, M_crd = (Wply*fy)/10^6=',int(Wply)*int(fy)/(1e6), 'kNm')
M=(W*(L*L)/8)
if float(M)>M_crd:
     print('Since M>M_crd,bending moment resistance is inadequate')
else:
     print('Since M<M_crd,bending moment resistance is adequate')

print('--------------------------------------------------------------------------------------------------')
print('7. VERTICAL DEFLECTION CHECK AT SERVICEABILITY LIMIT STATE')
print('For a conservative design, total load has been considered for deflection and vibration check')
W_T=((print('W_L,Total Load=g1+q1=  ', (g1+q1), 'kn-m')))
print('Vertical Deflection = δ')
A=print(('(int(5)*str(W_T)*int(L**4))',(int(5)*(g1+q1))*int(L*L*L*L)))
B=print('(int(384)*float(E)*float(iy))',(int(384)*float(E)*float(iy)))
print('Vertical Deflection = δ',(A/B))











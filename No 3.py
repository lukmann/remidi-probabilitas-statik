print("Nama = lukmanul hakim")
print("Nim = A11.2016.09732")
print("Kelas = A11.54301")

n=9
a1=78;a2=69;a3=77;a4=88;a5=67;a6=80;a7=74;a8=94;a9=102
s1=2.75;s2=2.15;s3=4.41;s4=5.52;s5=3.21;s6=4.32;s7=2.31;s8=4.30;s9=3.71
d1=57.5;d2=52.8;d3=61.3;d4=67.0;d5=53.5;d6=62.7;d7=56.2;d8=68.5;d9=69.2
f1=a1*s1;f2=a2*s2;f3=a3*s3;f4=a4*s4;f5=a5*s5;f6=a6*s6;f7=a7*s7;f8=a8*s8;f9=a9*s9
g1=a1*a1;g2=a2*a2;g3=a3*a3;g4=a4*a4;g5=a5*a5;g6=a6*a6;g7=a7*a7;g8=a8*a8;g9=a9*a9
h1=s1*s1;h2=s2*s2;h3=s3*s3;h4=s4*s4;h5=s5*s5;h6=s6*s6;h7=s7*s7;h8=s8*s8;h9=s9*s9
j1=d1*d1;j2=d2*d2;j3=d3*d3;j4=d4*d4;j5=d5*d5;j6=d6*d6;j7=d7*d7;j8=d8*d8;j9=d9*d9
k1=a1*d1;k2=a2*d2;k3=a3*d3;k4=a4*d4;k5=a5*d5;k6=a6*d6;k7=a7*d7;k8=a8*d8;k9=a9*d9
l1=s1*d1;l2=s2*d2;l3=s3*d3;l4=s4*d4;l5=s5*d5;l6=s6*d6;l7=s7*d7;l8=s8*d8;l9=s9*d9

x1=a1+a2+a3+a4+a5+a6+a7+a8+a9
x2=s1+s2+s3+s4+s5+s6+s7+s8+s9
y=d1+d2+d3+d4+d5+d6+d7+d8+d9
x1x2=f1+f2+f3+f4+f5+f6+f7+f8+f9
x1y=k1+k2+k3+k4+k5+k6+k7+k8+k9
x2y=l1+l2+l3+l4+l5+l6+l7+l8+l9
x12=g1+g2+g3+g4+g5+g6+g7+g8+g9
x22=h1+h2+h3+h4+h5+h6+h7+h8+h9
y2=j1+j2+j3+j4+j5+j6+j7+j8+j9

print("x1 =",a1,a2,a3,a4,a5,a6,a7,a8,a9,"total =",x1)
print("x2 =",s1,s2,s3,s4,s5,s6,s7,s8,s9,"total =",x2)
print("y =",d1,d2,d3,d4,d5,d6,d7,d8,d9,"total =",y)
print("x1x2 =",f1,f2,f3,f4,f5,f6,f7,f8,f9,"total =",x1x2)
print("x1y =",k1,k2,k3,k4,k5,k6,k7,k8,k9,"total =",x1y)
print("x2y =",l1,l2,l3,l4,l5,l6,l7,l8,l9,"total =",x2y)
print("x1^2 =",g1,g2,g3,g4,g5,g6,g7,g8,g9,"total =",x12)
print("x2^2 =",h1,h2,h3,h4,h5,h6,h7,h8,h9,"total =",x22)
print("y^2 =",j1,j2,j3,j4,j5,j6,j7,j8,j9,"total =",y2)
print(  )
b1=(((n*x1x2)-(x1*x2))/((n*x12)-(x1*x1)))
b2=(((n*x1y)-(x1*y))/((n*x12)-(x1*x1)))
b3=(((n*x2y)-(x2*y))/((n*x22)-(x2*x2)))
print("Rumus : b=(((n*x1y)-(x1*y))/((n*x12)-(x1*x1)))")
w1=((x2/n)+((b1*x1)/n))
w2=((y/n)+((b2*x1)/n))
w3=((y/n)+((b3*x2)/n))
print("Rumus : w=((y/n)+((b*x1)/n))")
print(  )
print("Hasilnya : Y =",w1,"+",w2,"+",w3)





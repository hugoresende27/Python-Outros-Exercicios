from math import hypot,sqrt


ca=float(input("Cateto Adjacente --> "))
co=float(input("Cateto Oposto -->"))

hip = sqrt( ( pow(ca,2)+ pow(co,2)  )  )

print ("A hipotenusa mede {:.2f}".format(hip))

hip2 = hypot(co,ca)
print ("outra maneira é {:.2f}".format(hip2))
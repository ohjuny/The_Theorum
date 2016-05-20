#"The Thoerum" from "An Abundance of Katherines"

#http://effyeahnerdfighters.com/post/683364805/colins-equation-from-an-abundance-of-katherines
#https://www.wolframalpha.com/input/?i=plot

#Names
per1 = raw_input("Name of person 1: ")
per2 = raw_input("Name of person 2: ")

print("\n\n")

#Age
age1 = input("%s's age: " %(per1))
age2 = input("%s's age: " %(per2))
A = (age1 + age2) / 2 - 5

print("\n\n")

#Popularity Differential
print("On a scale of 1 to 1000...")
pop1 = input("How popular is %s? " %(per1))
pop2 = input("How popular is %s? " %(per2))
C = (pop1 - pop2) / 75

print("\n\n")

#Attractiveness Differential
print("On a scale of 0 to 5...")
att1 = input("How attractive is %s? " %(per1))
att2 = input("How attractive is %s? " %(per2))
H = att1 - att2

print("\n\n")

#Dumper/Dumpee Differential
print("On a scale from 0 to 1, where\n0 is an extreme dumpee and\n1 is an extreme dumper...")
dum1 = input("%s is : " %(per1))
dum2 = input("%s is : " %(per2))
D = dum1 - dum2

print("\n\n")

#Introvert/Extrovert Differential
print('''On a scale from 0 to 5, where\n
        0 is an extreme introvert and\n
        5 is an extreme extrovert...''')
vert1 = input("%s is : " %(per1))
vert2 = input("%s is : " %(per2))
P = vert1 - vert2

print("\n")

#Calculating the Function

# (p1) - D^7 * x^8
p1p1 = -D**7
part1 = ("%dx^8 " %(p1p1))

# (p2) + D^2 * x^3
p2p1 = D**2
part2 = ("+ %dx^3 " %(p2p1))

# (p3) - x^2 / A^3
p3p1 = A**3
part3 = ("- x^2 / %d " %(p3p1))

# (p4) - C * x^2
part4 = ("- %d * x^2 " %(C))

# (p5) - Px
part5 = ("- %d * x " %(P))

# (p6) + 1 / A
p6p1 = 1 / A
part6 = ("+ %d " %(A))

# (p7) + 13P
p7p1 = 13 * P
part7 = ("+ %d " %(P))

#Things get a bit complicated here

pi = 3.1415

# (p8) + sin(2x) / 2
part8 = ("+ sin(2x) / 2 ")

# (p9) * (1 + (-1)^(H + 1)  *  (x + 11pi / 2)^H  /  |x + 11pi / 2|^H)
p9p1 = 1 + (-1)**(H + 1)
pi11 = 11 * pi
part9 = ("* (%d * (x + %d / 2)^(%d) / |x + %d / 2|^(%d))" %(p9p1, pi11, H, pi11, H))

function = ("%s%s%s%s%s%s%s%s%s" %(part1, part2, part3, part4, part5, part6, part7, part8, part9))

print("Input the following function into WolframAlhpa's graph plotter:\n%s" %(function))
print("\n")
print("Here's the WolframAlpha link: https://www.wolframalpha.com/input/?i=plot")
print("\n")
print("If the graph looks like a frown, %s will be the dumper" %(per1))
print("If the graph looks like a smile, %s will be the dumper" %(per2))
print("\n")
print("Have fun :D")
import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
d = b**2-4*a*c
root1 = (-b-(d**0.5))/2*a
root2 = (-b+(d**0.5))/2*a

if d<0:
    print("This function has not real roots.")
elif d==0:
    print("This function has two equal roots and the roots are {}".format(root1))
else:
    print("This functions roots are {0} and {1}".format(root1,root2))
n = int(input())
dni = input()
dnil = dni.split(" ")
dot = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14"]
if dnil[-1] == "0":
    print("UP")
elif dnil[-1] == "15":
    print("DOWN")
elif n == 1 and  dnil[-1] in dot:
    print("UNKNOWN")
elif int(dnil[-1]) > int(dnil[-2]):
    print("UP")
elif int(dnil[-1]) < int(dnil[-2]):
    print("DOWN")
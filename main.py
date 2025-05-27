try:
    from turtle import *
    from math import *
except Exception as e:
    print("Dieser Fehler trat auf: " + str(e))
    exit(e)
speed(0)
while True:
    while True:
        try:
            n=int(input("Wie viele Ecken? "))
            break
        except:
            print("Fehlerhafte Eingabe. Bitte versuche es erneut.")
    forward(800/n/2)
    circle((800/n) / (2 * sin(pi / n)))
    back(800/n/2)
    for i in range(n):
        forward(800/n)
        left(180-(180*(n-2))/n)
    e = input("Zum beenden beliebige Taste drücken.\nZum fortfahren J eingeben. ")
    if e.lower() != "j":
        exit(e)
    reset()

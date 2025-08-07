import random

rnum = random.randint(0, 2)
s = "kő"
run = True

if rnum == 0:
    s = "kő"
if rnum == 1:
    s = "papír"
if rnum == 2:
    s = "olló"

while run:

    c = input("kő/papír/olló:  ")

    if c not in ["kő", "papír", "olló"]:
        print("nincs értelmezve")

    if c == "kő" and s == "kő":
        print("döntetlen")
    if c == "kő" and s == "papír":
        print("vesztettél")
    if c == "kő" and s == "olló":
        print("nyertél")

    if c == "papír" and s == "papír":
        print("döntetlen")
    if c == "papír" and s == "kő":
        print("nyertél")
    if c == "papír" and s == "olló":
        print("vesztettél")

    if c == "olló" and s == "olló":
        print("döntetlen")
    if c =="olló" and s == "kő":
        print("vesztettél")
    if c == "olló" and s == "papír":
        print("nyertél")
    
    e = input("Szeretnél még egyet? (I/N)   ")

    if e == "N":
        run = False
    if e == "I":
        run = True
    if e not in ["N", "I"]:
        print("hibás érték")
        run = False


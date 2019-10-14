
print("Quina edad tens?")
edad = input()

if (int(edad) >= 18):
    print("Ets major de edad!")
    print("!!!!!")
else:
    print("No ets major de edad!")


# Si estic en edad treballador (no me puc jubilar i puc treballar)
print("Quina edad tens?")
edad = input()
edadI = int(edad)

if (edadI >= 16 and edadI <=67):
    print("Has de treballar!")
else:
    if (edadI > 67):
        if (edadI > 99):
            print("Aprofita......")
        else:
            print("T'has de jubilar!")

    else:
        print("Ets un mocós!")


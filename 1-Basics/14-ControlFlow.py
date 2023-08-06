# --------------------
# --  Control Flow  --
# -- If, Elif, Else --
# -- Make Decisions --
# --------------------
uName = "Loai"
cName = "Algo"
cPrice = 200
uCountry = input("enter ur country name : ")

if uCountry == "Algerie" or uCountry == "KSA":

    print(f"Hello \"{uName}\" Because ur from {uCountry}")
    print(f"The price is {cPrice - 80}")


else:

    print(f"Hello \"{uName}\" Because ur from {uCountry}")
    print(f"The price is {cPrice - 30}")

# -------------------
# -- Loop => While --
# -------------------
# while condition_is_true
#   Code Will Run Until Condition Become False
# -----------------------

a = 0

while a < 10:
    print(a)
    a += 1

else:
    print("Loop Is Done")  # True become false

myF = ["Ghanou", "Hami", "Yasser"]

a = 0

while a < len(myF):
    print(f"#{str(a).zfill(2)} {myF[a]}")
    a += 1

# -------------------------------------
maximumWebsite = 5
fList = []

while maximumWebsite > 0:
    web = input("Please Enter Ur Favorite Website Without https://")
    fList.append(f"https://{web.strip().lower()}")
    maximumWebsite -= 1
    print(f"Website Added , '{maximumWebsite}' Place Left's")

else:
    print("BookMarke is full , U Cant Add More")

if len(fList) > 0:
    print("The List Is Not Empty")
    fList.sort()

index = 0

while index < len(fList):
    print(fList[index])
    index += 1

# -------------------------------------
tries = 4

mainPassword = "A@B-loaiRebouh"
inputPassword = input("Type Ur Password")

while inputPassword != mainPassword:
    tries -= 1
    print(f"U Have Enter The Wrong Password , {tries} Remaining")
    inputPassword = input("Type Ur Password")
    if tries == 0:
        break
else:
    print("GoodJob u Have Enter The Correct Password")

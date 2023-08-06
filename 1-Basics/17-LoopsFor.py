# -----------------
# -- Loop => For --
# -----------------
# for item in iterable_object :
#   Do Something With Item
# -----------------------------
# item Is A Vairable You Create and Call Whenever You Want
# item refer to the current position and will run and visit all items to the end
# iterable_object => Sequence [ list, tuples, set, dict, string of charcaters, etc ... ]
# ---------------------------------------------------------------


myNum = [1, 2, 3, 4, 5]

for number in myNum:
    if number % 2 == 0:
        print(f"The Number ' {number} ' is Peer")
    else:
        print(f"The Number ' {number} ' is Odd")
else:
    print("The Loop Is Finished")

Name = "Loai"

for letter in Name:
    print(f"[{letter.upper()}]")

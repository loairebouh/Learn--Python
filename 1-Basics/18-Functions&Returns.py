# -------------------------
# -- Function And Return --
# -------------------------
# [1] A Function is A Reusable Block Of Code Do A Task
# [2] A Function Run When You Call It
# [3] A Function Accept Element To Deal With Called [Parameters]
# [4] A Function Can Do The Task Without Returning Data
# [5] A Function Can Return Data After Job is Finished
# [6] A Function Create To Prevent DRY
# [7] A Function Accept Elements When You Call It Called [Arguments]
# [8] There's A Built-In Functions and User Defined Functions
# [9] A Function Is For All Team and All Apps
# ----------------------------------------


a, b, c = "Loai", "Ghanou", "Hami"


def say_hello(name):
    return print(f"Hello {name}")


print(say_hello(a))


def mult(a, b):
    s = a+b
    return s


print(mult(3, 5))

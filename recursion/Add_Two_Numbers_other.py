f = open("user.out", "w")
trash = {91: None, 93: None, 44: None, 10: None}
while True:
    try:
        f.writelines(("[", ",".join(
            str(int(next(lines).translate(trash)[::-1]) + int(next(lines).translate(trash)[::-1])))[::-1], "]\n"))
    except StopIteration:
        exit()

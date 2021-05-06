import mtmf

vyr = input("выражение\n").replace(" ","")

# vyr = "(4-3)*(12+(2-1))"
while vyr.count(")"):
    for y in range(len(vyr)):
        if vyr[y] == ")":
            for x in range(y, -1, -1):
                if vyr[x] == "(":
                    pr = []
                    for g in range(x + 1, y):
                        pr.append(vyr[g])
                    pr = "".join(pr)
                    reshenie = mtmf.vn(pr)
                    vyr = vyr.replace(vyr[x:y + 1], str(reshenie))
                    break
            break
        else:
            continue
itog = mtmf.vn(vyr)
print("Результат", itog)

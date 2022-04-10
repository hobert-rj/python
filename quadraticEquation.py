def simpleRoots(a: float, b: float, c: float):
    """Calculates simple roots of a quadratic equation"""
    r = []
    delta = b**2-4*a*c
    if delta > 0:
        r.extend([(-b+delta**(1/2))/2*a, (-b-delta**(1/2))/2*a])
    elif delta == 0:
        r.append(-b/2*a)
    return r


def inputFormated(multiplicand: list[str], seprator: str, example: str, model: str):
    val = input(
        f"example: {example}\nType equation as {model} ... ").lower().replace(' ', '')
    hold = ""
    index = 0
    result = [0] * len(multiplicand)
    lenght = len(val)
    for i in range(0, lenght):
        hold += val[i]
        v_in_s = val[i] in seprator
        if v_in_s or i == lenght-1:
            m = multiplicand[index].lower()
            if v_in_s:
                hold = hold.replace(val[i], '')
            if m in hold:
                hold = hold.replace(m, '')
                result[index] = float(hold)
                index += 1
            else:
                print("Invalid input!")
            hold = ""
    return result


equation = inputFormated(multiplicand=[
                         "X[2]", "X", ""], seprator="+-", example="5X[2] + 4X + 6", model="aX[2] + bX + c")
print(f"result: {simpleRoots(equation[0], equation[1], equation[2])}")

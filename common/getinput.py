def getInput(day):
    with open("input/day" + day, "r") as fopen:
        inputValues = fopen.readlines()
    return inputValues
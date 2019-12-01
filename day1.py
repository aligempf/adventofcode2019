def getInput():
    with open("input/day1", "r") as fopen:
        inputValues = fopen.readlines()
    inputValues = list(map(lambda val: int(val.strip()), inputValues))
    return inputValues

def getTestValues():
    return [12, 14, 1969, 100756]

def getTestResults():
    return [2, 2, 654, 33583]

def getTestResultsPartTwo():
    return [2, 2, 966, 50346]

def getFuelRequired(mass):
    return int(mass / 3) - 2

def getRecursiveFuel(mass):
    fuelRequired = getFuelRequired(mass)
    return fuelRequired + getRecursiveFuel(fuelRequired) if fuelRequired > 0 else 0

def part1():
    assert(list(map(getFuelRequired, getTestValues())) == getTestResults())
    print(sum(map(getFuelRequired, getInput())))

def part2():
    assert(list(map(getRecursiveFuel, getTestValues())) == getTestResultsPartTwo())
    print(sum(map(getRecursiveFuel, getInput())))

part1()
part2()
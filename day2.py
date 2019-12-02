import common.getInput

def getInput():
    return list(map(int, common.getInput.getInput('2')[0].split(',')))

def getTestInputs():
    return [[1,0,0,0,99], [2,3,0,3,99], [2,4,4,5,99,0], [1,1,1,4,99,5,6,0,99]]

def getTestResults():
    return [[2,0,0,0,99], [2,3,0,6,99], [2,4,4,5,99,9801], [30,1,1,4,2,5,6,0,99]]

class Instruction:
    def __init__(self, instruction, noun = 0, verb = 0, address = 0):
        self.instruction = instruction
        self.noun = noun
        self.verb = verb
        self.address = address

    def run(self, pointer, program):
        if self.instruction == 99:
            return -4
        elif self.instruction == 1:
            program[self.address] = program[self.noun] + program[self.verb]
        elif self.instruction == 2:
            program[self.address] = program[self.noun] * program[self.verb]
        else:
            print("ERROR!!")
        return pointer + 4

class Program:
    def __init__(self, program):
        self.program = program
        self.pointer = 0

    def get(self, index, default=None):
        try:
            return self.program[index]
        except IndexError:
            return default

    def run_instruction(self, instruction_pointer):
        instruction_address = instruction_pointer * 4
        instruction = Instruction(
            self.program[instruction_address],
            self.get(instruction_address + 1, 0),
            self.get(instruction_address + 2, 0),
            self.get(instruction_address + 3, 0),
        )
        return int(instruction.run(instruction_address, self.program) / 4)

def runOpCodes(opCodes):
    prog = Program(opCodes)
    pointer = 0
    while pointer >= 0:
        pointer = prog.run_instruction(pointer)
    return prog.program

def runTests():
    assert(list(map(runOpCodes, getTestInputs())) == getTestResults())

def part1():
    runTests()
    program = getInput()
    program[1] = 12
    program[2] = 2
    print(runOpCodes(program)[0])

def part2():
    result = 0
    noun = 0
    verb = 0
    target = 19690720
    while True:
        while noun < 100:
            inputValues = getInput()
            inputValues[1] = noun
            inputValues[2] = verb
            result = runOpCodes(inputValues)[0]
            if result == target:
                break
            noun += 1
        if result == target:
            break
        noun = 0
        verb += 1
    print(100*noun + verb)

part1()
part2()

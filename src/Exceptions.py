class InvalidRoomSize(Exception):
    def __init__(self, message):
        super(InvalidRoomSize, self).__init__('Room size ' + message + ' is invalid!')


class InvalidInitialCoords(Exception):
    def __init__(self, message):
        super(InvalidInitialCoords, self).__init__('Initial coord ' + message + ' is invalid!')
        

class InvalidPatch(Exception):
    def __init__(self, message):
        super(InvalidPatch, self).__init__('Patch ' + message + ' is invalid!')


class InvalidInstruction(Exception):
    def __init__(self, message):
        super(InvalidInstruction, self).__init__('Instruction ' + message + ' is invalid!')
        



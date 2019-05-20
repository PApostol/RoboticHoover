class InvalidRoomSize(Exception):
    def __init__(self, message):
        super(InvalidRoomSize, self).__init__(message + ' is invalid!')


class InvalidInitialCoords(Exception):
    def __init__(self, message):
        super(InvalidInitialCoords, self).__init__(message + ' is invalid!')
        

class InvalidPatch(Exception):
    def __init__(self, message):
        super(InvalidPatch, self).__init__(message + ' is invalid!')


class InvalidInstruction(Exception):
    def __init__(self, message):
        super(InvalidInstruction, self).__init__(message + ' is not recognised!')
        



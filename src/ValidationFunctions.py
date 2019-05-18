from src.Exceptions import InvalidRoomSize, InvalidInitialCoords, InvalidPatch, InvalidInstruction

def validateRoomSize(roomSize):

    x = roomSize[0]
    y = roomSize[1]

    if (not isinstance(x, int)) or (not isinstance(y, int)) or (x<0) or (y<0):
            raise InvalidRoomSize(str(roomSize))


def validateInitialCoords(coords, roomSize):
    x = coords[0]
    y = coords[1]

    roomx = roomSize[0]
    roomy = roomSize[1]

    if (not isinstance(x, int)) or (not isinstance(y, int)) or (x<0) or (y<0) or (x>roomx) or (y>roomy):
            raise InvalidInitialCoords(str(coords))


def validatePatches(patches, roomSize):
    roomx = roomSize[0]
    roomy = roomSize[1]
    
    for patch in patches:
        x = patch[0]
        y = patch[1]

        if (not isinstance(x, int)) or (not isinstance(y, int)) or (x<0) or (y<0) or (x>roomx) or (y>roomy):
            raise InvalidPatch(str(patch))


def validateInstructions(instructions):
    
    myset = {'N','S','E','W'}

    for letter in instructions:
        if letter not in myset:
            raise InvalidInstruction(letter)
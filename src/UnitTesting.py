from Hoover import Hoover
from WriteFunctions import writeToStorage, writeToDatabase
from ValidationFunctions import validateRoomSize, validateInitialCoords, validatePatches, validateInstructions
from Exceptions import InvalidRoomSize, InvalidInitialCoords, InvalidPatch, InvalidInstruction
import unittest

def execute(roomSize, coords, patches, instructions):
    try:
        validateRoomSize(roomSize)
        validateInitialCoords(coords, roomSize)
        validatePatches(patches, roomSize)
        validateInstructions(instructions)

        myhoover = Hoover(coords[0], coords[1])
        myhoover.setRoomSize(roomSize)

        for step in instructions:
            location = myhoover.getLocation()

            if location in patches:
                patches.remove(location)
                myhoover.incrementPatchCount()

            myhoover.executeInstruction(step)
        
    except Exception as err:
        raise err

    else:
        return str(myhoover.getOutput())


class VariousTests(unittest.TestCase):

    def test_default(self):
        roomSize = [5, 5]
        coords = [1, 2]
        patches = [[1, 0], [2, 2], [2, 3]]
        instructions = 'NNESEESWNWW'
        self.assertEqual(execute(roomSize, coords, patches, instructions), "{'coords': [1, 3], 'patches': 1}")

  
    def test_InvalidRoomSize(self):
        roomSize = [5, -1]
        coords = [1, 2]
        patches = [[1, 0], [2, 2], [2, 3]]
        instructions = 'NNESEESWNWW'

        with self.assertRaises(Exception) as context:
            execute(roomSize, coords, patches, instructions)

        self.assertTrue('Room size [5, -1] is invalid!' in str(context.exception))


    def test_InvalidInitialCoords(self):
        roomSize = [5, 5]
        coords = [1, 6]
        patches = [[1, 0], [2, 2], [2, 3]]
        instructions = 'NNESEESWNWW'
        
        with self.assertRaises(Exception) as context:
            execute(roomSize, coords, patches, instructions)

        self.assertTrue('Initial coord [1, 6] is invalid!' in str(context.exception))


    def test_InvalidPatch(self):
        roomSize = [5, 5]
        coords = [1, 2]
        patches = [[1, 0], [2, 2], [-2, 3]]
        instructions = 'NNESEESWNWW'

        with self.assertRaises(Exception) as context:
            execute(roomSize, coords, patches, instructions)

        self.assertTrue('Patch [-2, 3] is invalid!' in str(context.exception))


    def test_InvalidRoomSize_3D(self):
        roomSize = [5, 5, 2]
        coords = [1, 2]
        patches = [[1, 0], [2, 2], [2, 3]]
        instructions = 'NNESEESWNWW'

        with self.assertRaises(Exception) as context:
            execute(roomSize, coords, patches, instructions)

        self.assertTrue('Room size [5, 5, 2] is invalid!' in str(context.exception))


    def test_InvalidInitialCoords_3D(self):
        roomSize = [5, 5]
        coords = [1, 2 ,2]
        patches = [[1, 0], [2, 2], [2, 3]]
        instructions = 'NNESEESWNWW'
        
        with self.assertRaises(Exception) as context:
            execute(roomSize, coords, patches, instructions)

        self.assertTrue('Initial coord [1, 2, 2] is invalid!' in str(context.exception))


    def test_InvalidPatch_3D(self):
        roomSize = [5, 5]
        coords = [1, 2]
        patches = [[1, 0], [2, 2, 1], [2, 3]]
        instructions = 'NNESEESWNWW'

        with self.assertRaises(Exception) as context:
            execute(roomSize, coords, patches, instructions)

        self.assertTrue('Patch [2, 2, 1] is invalid!' in str(context.exception))


    def test_InvalidInstruction(self):
        roomSize = [5, 5]
        coords = [1, 2]
        patches = [[1, 0], [2, 2], [2, 3]]
        instructions = 'NNESEESWNWA'

        with self.assertRaises(Exception) as context:
            execute(roomSize, coords, patches, instructions)

        self.assertTrue('Instruction A is invalid!' in str(context.exception))


    def test_hoover_1by1_room(self):
        roomSize = [1, 1]
        coords = [1, 2]
        patches = [[1, 0], [2, 2], [2, 3]]
        instructions = 'NNESEESWNWA'

        with self.assertRaises(Exception) as context:
            execute(roomSize, coords, patches, instructions)

        self.assertTrue('Initial coord [1, 2] is invalid!' in str(context.exception))


    def test_boundaries_top_right(self):
        roomSize = [5, 5]
        coords = [1, 2]
        patches = [[1, 0], [2, 2], [2, 3]]
        instructions = 'NNNNNNNNNNNNNNNNNEEEEEEEEEEEEEEEEEEEE'
        self.assertEqual(execute(roomSize, coords, patches, instructions), "{'coords': [5, 5], 'patches': 0}")
    

    def test_boundaries_bottom_left(self):
        roomSize = [5, 5]
        coords = [1, 2]
        patches = [[1, 0], [2, 2], [2, 3]]
        instructions = 'SSSSSSSSSSSSSSSWWWWWWWWWWWWWWWWWWWWWW'
        self.assertEqual(execute(roomSize, coords, patches, instructions), "{'coords': [0, 0], 'patches': 1}")
    

    def test_repeat_over_patch(self):
        roomSize = [1, 3]
        coords = [1, 1]
        patches = [[1, 2]]
        instructions = 'NNSSNNSSNNSSNNSSNNSSNNSS'
        self.assertEqual(execute(roomSize, coords, patches, instructions), "{'coords': [1, 1], 'patches': 1}")


if __name__ == '__main__':
    unittest.main()
from flask import Flask, request, abort
from datetime import datetime
from src.Hoover import Hoover
from src.WriteFunctions import writeToStorage, writeToDatabase
from src.ValidationFunctions import validateRoomSize, validateInitialCoords, validatePatches, validateInstructions

import ast, json

app = Flask(__name__)

@app.route('/api/test/')
def test():
    return 'If you see this, the back end is up and running.'


@app.route('/api/execute/', methods=['POST'])
def execute():
    try:
        temp_dict = request.form.to_dict() # assumes POST request
        json_str = list(temp_dict.keys())[0]
        myjson = ast.literal_eval(json_str)

        roomSize = myjson['roomSize']
        validateRoomSize(roomSize)

        coords = myjson['coords']
        validateInitialCoords(coords, roomSize)

        patches = myjson['patches'] # list of list of int
        validatePatches(patches, roomSize)

        instructions = myjson['instructions']
        validateInstructions(instructions)
   
        myhoover = Hoover(coords[0], coords[1])
        myhoover.setRoomSize(roomSize)

        for step in instructions:
            location = myhoover.getLocation()

            if location in patches:
                patches.remove(location) #  i.e. cleaned 
                myhoover.incrementPatchCount()

            myhoover.executeInstruction(step)
        
    except Exception as err:
        abort(400, str(err))

    else:
        output = myhoover.getOutput()
        app_json = json.dumps(output)

        writeToStorage(json_str, output)
        writeToDatabase(json_str, output)

        return app_json

 
if __name__ == '__main__':
    app.run(debug=True)
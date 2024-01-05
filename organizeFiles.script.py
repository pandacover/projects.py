import os
import shutil
from pathlib import Path

# path to target folder
targetPath = 'D:/Downloads/'
targetFolder = Path(targetPath)

try:
    if not targetFolder.exists():
        raise Exception('Target folder does not exists!')

    filePathListInTargetFolder = list(targetFolder.glob('*'))

    for filePath in filePathListInTargetFolder:
        # get the file extension
        fileExtension = filePath.suffix[1:]
    
        if fileExtension:
            # change your destination here
            destination = targetPath + fileExtension

            # make a directory with the extension name if doesn't exists
            if not Path(destination).exists() or not Path(destination).is_dir():
                os.makedirs(destination, exist_ok=True)

            # move the file to the target folder
            shutil.move(str(filePath), destination)

except Exception as error:
    print('Something went wrong: ' + repr(error))
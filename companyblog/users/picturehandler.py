import os
from PIL import Image

from flask import current_app,url_for

def addProfilePic(picUpload, username):
    filename = picUpload.filename
    extType = filename.split('.')[-1]
    storageFileName = str(username)+'.'+extType
    filePath = os.path.join(current_app.root_path, 'static\profile_pics' , storageFileName)

    outputSize = (200,200)
    pic = Image.open(picUpload)
    pic.thumbnail(outputSize)
    pic.save(filePath)

    return storageFileName

import datetime
import uuid

def generateDateFileName(fileType, prefix="test"):
    return prefix+ "-{date:%Y%m%d_%H%M%S}".format( date=datetime.datetime.now() ) + "." + fileType

def generateUniqueFileName(fileType, prefix="default"):
    return prefix+ "_" +str(uuid.uuid4()) + fileType
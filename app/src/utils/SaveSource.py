import datetime
import os
from config.settings import OUTPUT_FILE_PATH
from json import loads
from dicttoxml import dicttoxml

def save_source_to_file(source, *args, **kwargs):
    if not "filename" in kwargs or not kwargs["filename"]:
        filename = 'test-{date:%Y-%m-%d_%H:%M:%S}.html'.format( date=datetime.datetime.now() )
    else:
        filename = kwargs["filename"]
    path = os.path.join(OUTPUT_FILE_PATH, filename)
    try:
        with open(path, 'w') as f:
            f.write(source)
    except Exception as e:
        print("ERROR: " + str(e))
    else:
        print("Save file at "+path)


def save_json_to_xml(source, *args, **kwargs):
    if not "filename" in kwargs or not kwargs["filename"]:
        filename = 'test-{date:%Y-%m-%d_%H:%M:%S}.xml'.format( date=datetime.datetime.now() )
    else:
        filename = kwargs["filename"]
    path = os.path.join(OUTPUT_FILE_PATH, filename)
    try:
        xml = dicttoxml(loads(source), attr_type=False)
        with open(path, 'wb') as f:
            f.write(xml)
    except Exception as e:
        print("ERROR: " + str(e))
    else:
        print("Save file at "+path)
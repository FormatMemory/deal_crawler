import datetime
import os
from config.settings import OUTPUT_FILE_PATH
import json
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
        print("ERROR at save_source_to_file: " + str(e))
    else:
        print("Save file at "+path)


def save_json_to_xml(source, *args, **kwargs):
    if not "filename" in kwargs or not kwargs["filename"]:
        filename = 'test-{date:%Y-%m-%d_%H:%M:%S}.xml'.format( date=datetime.datetime.now() )
    else:
        filename = kwargs["filename"]
    path = os.path.join(OUTPUT_FILE_PATH, filename)
    try:
        xml = dicttoxml(json.loads(source), attr_type=False)
        with open(path, 'wb') as f:
            f.write(xml)
    except Exception as e:
        print("ERROR at save_json_to_xml : " + str(e))
    else:
        print("Save file at "+path)


def save_json_to_csv(source, *args, **kwargs):
    print(type(source))
    return 
    if not "filename" in kwargs or not kwargs["filename"]:
        filename = 'test-{date:%Y-%m-%d_%H:%M:%S}.csv'.format( date=datetime.datetime.now() )
    else:
        filename = kwargs["filename"]
    path = os.path.join(OUTPUT_FILE_PATH, filename)
    try:
        # data = [json.loads(i) for i in source if i]
        data = source
        with open(path, 'wb') as f:
            f.writerow(data[0].keys())
            for row in data:
                f.writerow(row.values())
    except Exception as e:
        print("ERROR at save_json_to_csv: " + str(e))
    else:
        print("Save file at "+path)
import os
from config.settings import OUTPUT_FILE_PATH
import json
from dicttoxml import dicttoxml
import csv
from src.utils.NameGenerators import generateDateFileName


def save_source_to_file(source, *args, **kwargs):
    if not "filename" in kwargs or not kwargs["filename"]:
        filename = generateDateFileName("html")
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
        filename = generateDateFileName("xml")
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


def save_dict_to_csv(source, *args, **kwargs):
    if type(source) != dict:
        raise Exception("ERROR at save_dict_to_csv: Expect input source in dict type but received "+ type(source))
    if "filename" in kwargs and  kwargs["filename"]:
        filename = kwargs["filename"]
    else:
        filename = generateDateFileName("csv")
    path = os.path.join(OUTPUT_FILE_PATH, filename)
    try:
        with open(path, 'w') as f:  # Just use 'w' mode in 3.x
            w = csv.DictWriter(f, source.keys())
            w.writeheader()
            w.writerow(source)
    except Exception as e:
        print("ERROR at save_json_to_csv: " + str(e))
    else:
        print("Save file at "+path)

def save_list_dict_to_csv(source, *args, **kwargs):
    if type(source) != list:
        raise Exception("ERROR at save_dict_to_csv: Expect input source in list type but received "+ type(source))
    if len(source) == 0:
        raise Exception("ERROR at save_dict_to_csv: empty source input")

    if "filename" in kwargs and  kwargs["filename"]:
        filename = kwargs["filename"]
    else:
        filename = filename = generateDateFileName("csv")
    path = os.path.join(OUTPUT_FILE_PATH, filename)
    try:
        with open(path, 'w') as f:  # Just use 'w' mode in 3.x
            w = csv.DictWriter(f, source[0].keys())
            w.writeheader()
            for r in source:
                w.writerow(r)
    except Exception as e:
        print("ERROR at save_list_dict_to_csv: " + str(e))
    else:
        print("Total rows:" + str(len(source)))
        print("Save file at "+path)
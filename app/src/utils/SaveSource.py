import datetime
import os
from config.settings import OUTPUT_FILE_PATH

def save_source_to_file(source, *args, **kwargs):
    if not "filename" in kwargs or not kwargs["filename"]:
        filename = 'test-{date:%Y-%m-%d_%H:%M:%S}.html'.format( date=datetime.datetime.now() )
    else:
        filename = kwargs["filename"]
    path = os.path.join(OUTPUT_FILE_PATH, filename)
    html = source
    try:
        with open(path, 'w') as f:
            f.write(html)
    except Exception as e:
        print("ERROR: " + str(e))
    else:
        print("Save file at "+path)
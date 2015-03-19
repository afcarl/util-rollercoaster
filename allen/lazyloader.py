import json

def json_loadbyline(fpath):

    with open(fpath, 'rb') as f:
        for line in f:
            yield json.loads(line)

def json_savebyline(save_obj, fpath):

    with open(fpath, 'wb') as f:
        for line in save_obj:
            json.dump(line, f)
            f.write('\n')

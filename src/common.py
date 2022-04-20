import json

######################################
# 2022-04-12 - Steven Chiu
# Convert list obj to json obj
######################################
def convert_list_to_json(listObj):
    json_object = json.dumps(listObj);
    return json_object;

######################################
# 2022-04-12 - Steven Chiu
# Get value from json obj by key
######################################
def get_value_by_key_fromJson(jsonObj, key):
    _jsonObj = json.loads(jsonObj);
    
    if key == "all":
        return json.dumps(_jsonObj);
    else:
        get_value_by_key = _jsonObj[key];
        return json.dumps(get_value_by_key);
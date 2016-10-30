import json
import datetime

def get_json_item(ori_data, keys):
    result = ''
    data = ori_data.copy()
    for key in keys:
        if data.get(key) is None:
            return ''
        else:
            result = data.get(key)
            data = result
    return result

def timestamp_to_ymd(timestamp):
    dt = datetime.datetime.fromtimestamp(timestamp)
    return dt.strftime('%Y%m%d')

def timestamp_to_date(timestamp):
    dt = datetime.datetime.fromtimestamp(timestamp)
    return dt.strftime('%Y%m%d-%H:%M:%S')

def extract_ymd(result_json):
    timestamp = get_json_item(result_json[u'timestamp'])
    return timestamp_to_ymd(timestamp)


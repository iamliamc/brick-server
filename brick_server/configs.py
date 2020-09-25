import json
import os

try:
    configs = json.load(open(os.environ['BRICK_CONFIGFILE']))
except KeyError:
    configs = json.load(open("./configs/configs.json"))
    configs['auth']['jwt'] = {}

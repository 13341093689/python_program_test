import os

from utils.add_prropties import add_pro_id
from utils.write_and_read_json import read_json,write_json
def main(path):
  info = read_json(path)
  id= add_pro_id()
  info['id'] = id
  write_json(path,info)


if __name__ == "__main__":
  path="/home/zzm/python-program/data/json_data/demo.json"
  main(path)
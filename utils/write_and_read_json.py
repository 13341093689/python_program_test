import json


def write_json(path,info):
  print('写入json')
  with open(path,'w') as f:
    # f.write(json.dumps(info))
    json.dump(info,f,indent=4,sort_keys=True,ensure_ascii=False)


def read_json(path):
  print('读取json')
  try:
    with open(path) as f:
      data = json.load(f)
      return data
  except Exception as ex:
    print('发生错误',ex)

if __name__=='__main__':
  file_path = '/home/zzm/python-program/data/json_data/demo.json'
  json_content = read_json(file_path)
  print(json_content)

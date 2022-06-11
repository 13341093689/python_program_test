import uuid

def add_pro_id():
  id = str(uuid.uuid4())
  id = id.replace('-','')
  return id


if __name__=="__mian__":
  add_pro_id()

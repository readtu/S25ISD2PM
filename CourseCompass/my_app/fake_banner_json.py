import json
from my_app.models import ModelData

json_string = '{"key":"value"}'
data = json.loads(json_string)
json_instance = ModelData(json_data=data)
json_instance.save()

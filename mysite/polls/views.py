from django.http import HttpResponse

from .models import Employee

from pymongo import MongoClient


def get_db_handle(db_name, host, port, username, password):
    client = MongoClient(host=host,
                         port=int(port),
                         username=username,
                         password=password
                         )
    db_handle = client['db_name']
    return db_handle, client


my_client = MongoClient('localhost', 27017)
# First define the database name
dbname = my_client['sample_medicines']

# Now get/create collection name (remember that you will see the database in your mongodb cluster only after you
# create a collection)
collection_name = dbname["medicinedetails"]

# let's create two documents
medicine_1 = {
    "medicine_id": "RR000123456",
    "common_name": "Paracetamol",
    "scientific_name": "",
    "available": "Y",
    "category": "fever"
}
medicine_2 = {
    "medicine_id": "RR000342522",
    "common_name": "Metformin",
    "scientific_name": "",
    "available": "Y",
    "category": "type 2 diabetes"
}

collection_name.insert_many([medicine_1, medicine_2])

med_details = collection_name.find({})

for r in med_details:
    print(r["common_name"])
    print(type(r))


# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello and welcome to my first <u>Django App</u> project!</h1>")


def get_json_data(request):
    employees = med_details
    import json
    from django.core import serializers
    json_data = serializers.serialize('json', employees)
    json_data = json.loads(json_data)
    from django.http import HttpResponse, JsonResponse
    return JsonResponse(json_data, safe=False)

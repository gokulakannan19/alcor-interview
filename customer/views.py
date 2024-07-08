import json
import requests
import xmltodict
from django.http import HttpResponse

# Create your views here.
def extract_user_info(request):

    url = "https://filesampleshub.com/download/code/xml/sample2.xml"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        xml_data = response.content
        
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving data from URL: {e}")
        return

    data_dict = xmltodict.parse(xml_data)
    json_data = json.dumps(data_dict)
    
    return HttpResponse(json_data)
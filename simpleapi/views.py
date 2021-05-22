from typing_extensions import final
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
import random
import string
import uuid
from tests.models import KeyValue
from . serializers import UIIDSerializer


uidd = uuid.uuid1()


@api_view(['GET'])
def generate(request):

    ## Dictionary to pass the uuid value to the data serializer class
    uidd_data = {
        "uiid": uidd.hex
    }

    ## Use the Serializer to send serialized data to the database
    serializer = UIIDSerializer(data=uidd_data)
    if serializer.is_valid():
        serializer.save()

    
    ## Process the Output of the New Data and the Previous Data
    showData = KeyValue.objects.filter().order_by('-id')
    final_data = {}
    ## Loop Through every Data in the Database and add it to a dictionary
    for i in showData:
        final_data[f'{i.date_time}'] = i.uiid
    
    ## Return the result.
    return Response(data=final_data, status=status.HTTP_200_OK)
    
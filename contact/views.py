from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ContactInfo
from .serializers import ContactInfoSerializer

@api_view (['GET'])
def contact_message(request):
    contactinfo = ContactInfo.objects.all()
    serializer = ContactInfoSerializer(contactinfo, many=True)
    return Response (serializer.data)
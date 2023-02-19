from rest_framework.serializers  import ModelSerializer
from .models import ContactInfo

class ContactInfoSerializer (ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = '__all__' #['name', 'email', 'message']
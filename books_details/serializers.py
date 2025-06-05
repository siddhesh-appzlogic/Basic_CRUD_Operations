from rest_framework import serializers
from .models import books_details

class Bookserilizers(serializers.ModelSerializer):
    class Meta:
        model = books_details
        fields = '__all__'
from rest_framework import serializers
from .models import Books

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'

    def to_representation(self, instance):
        data = super(BookSerializer, self).to_representation(instance)
        # manipulate data here 
        return data

from rest_framework import serializers
from articales.models import Articals

class ArticalSerializer(serializers.ModelSerializer):
    class Meta():
        model = Articals
        fields = ('id','title','content')
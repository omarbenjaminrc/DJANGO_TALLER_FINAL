from rest_framework import serializers
from django_seminario_app.models import Inscripcion

class InscripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscripcion
        fields = '__all__'
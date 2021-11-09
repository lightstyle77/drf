from rest_framework.serializers import ModelSerializer

from notes.models import Project, Note


class ProjectModelSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'


class NoteModelSerializer(ModelSerializer):

    class Meta:
        model = Note
        fields = '__all__'

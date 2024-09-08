from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Note
from .serializer import NoteSerializer

@api_view(['GET'])
def get_notes(request):
    notes = Note.objects.all()
    serialized_data = NoteSerializer(notes, many=True).data
    return Response(serialized_data)        
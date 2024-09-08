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


@api_view(['POST'])
def create_note(request):
    data = request.data
    serializer = NoteSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
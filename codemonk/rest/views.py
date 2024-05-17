from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .models import Paragraph, Word, CustomUser
from .serializers import CustomUserSerializer, ParagraphSerializer, WordToParagraphMappingSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status

# API view to list and create CustomUser objects
class CustomUserListCreateAPIView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

# API view to retrieve, update, and delete a CustomUser object by ID
class CustomUserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

# API view to save paragraphs of text and their word mappings
@csrf_exempt
@permission_classes([IsAuthenticated])
@api_view(['POST'])
def save_paragraph(request):
    paragraphs = request.data.get('paragraphs', [])
    saved_paragraphs = []

    for para in paragraphs:
        # Save the paragraph object
        paragraph = Paragraph(text=para)
        paragraph.save()
        saved_paragraphs.append(paragraph)

        # Split the paragraph into words and save word mappings
        words = para.split()
        for word in words:
            mapping = WordToParagraphMapping(word=word, paragraph=paragraph)
            mapping.save()

    return Response({'saved_paragraphs': ParagraphSerializer(saved_paragraphs, many=True).data}, status=status.HTTP_201_CREATED)

# API view to search for paragraphs containing a specific word
@api_view(['GET'])
def search_paragraph(request):
    word = request.query_params.get('word')
    if not word:
        return Response({'error': 'No word parameter provided'}, status=status.HTTP_400_BAD_REQUEST)
    
    # Retrieve paragraphs containing the specified word
    mappings = WordToParagraphMapping.objects.filter(word=word)
    paragraphs = [mapping.paragraph for mapping in mappings]

    return Response({'paragraphs': ParagraphSerializer(paragraphs, many=True).data})

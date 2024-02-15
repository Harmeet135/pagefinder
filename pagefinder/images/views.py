from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from PyPDF2 import PdfReader
import re

from .models import Image
from .serializers import ImageSerializer

class ImageView(APIView):  

    def post(self, request, *args, **kwargs):
        search_string = request.data.get('search_string')  

        pdf_file = request.POST.get('file_path', "C:\\Users\\acer\\OneDrive\\Desktop\\chatbot\\pdfreader\\test.py\\rdpd.pdf")
        

        if not pdf_file:
            return Response({'error': 'PDF file is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            reader = PdfReader(pdf_file)
            num_pages = len(reader.pages)
            results = []

            for i in range(num_pages):
                print(i)
                page = reader.pages[i]
                text = page.extract_text()
                if re.search(search_string, text, re.IGNORECASE):
                    results.append(i)

            response_data = {
                'message': 'Search complete.',
                'search_string': search_string,
                'results': results,
                'total_pages': num_pages,
                'matches_found': len(results)
            }
            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


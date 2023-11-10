from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import EnvironmentSerializer
from .models import Environment

# Create your views here.

def hello(request: HttpRequest):
    return HttpResponse('OK, deu certo!')

class PingView(APIView):

    def get(self, request):
        return Response({'nome': 'Rogério'}, status=200)
    
    def post(self, request):
        nome = request.data.get('nome') or 'Não Informada'
        return Response({'nome': nome}, status=201)
    
class EnvironmentsListView(APIView):
    def get(self, request):
        ambientes = Environment.objects.all()
        serializer = EnvironmentSerializer(ambientes, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = EnvironmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.instance.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)
        
class EnvironmentDatailUpdateView(APIView):
    def get(self, request, pk):
        try:
            environment = Environment.objects.get(id=pk)
            serializer = EnvironmentSerializer(environment)
            return Response(serializer.data)
        except:
            return Response(status=404)
        
    def put(self, request, pk):
        try:
            environment = Environment.objects.get(id=pk)
            serializer = EnvironmentSerializer(environment, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=400)
        except:
            return Response({"detail": "Não localizado!"}, status=404)
    
    def delete(self, request, pk):
        try:
            environment = Environment.objects.get(id=pk)
            environment.delete()
            return Response(status=204)
        except:
            return Response({"detail": "Não localizado!"}, status=404)
        
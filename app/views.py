from django.shortcuts import render

# Create your views here.
from app.models import *
from app.serializers import *
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

class productcls(ViewSet):
    def list(self,request):
        po=product.objects.all()
        pjd=productmodelserializer(po,many=True)
        return Response(pjd.data)
    

    def retrieve(self,request,pk):
        po=product.objects.get(pid=pk)
        pjd=productmodelserializer(po)
        return Response(pjd.data)
    

    def update(self,request,pk):
        pjd=request.data
        po=product.objects.get(pid=pk)
        pd=productmodelserializer(po,data=pjd)
        if pd.is_valid():
            pd.save()
            return Response({"message":"update successfully"})
        
        else:
            return Response({"failed":"not updated"})
    
    def partial_update(self,request,pk):
        pjd=request.data
        po=product.objects.get(pid=pk)
        pd=productmodelserializer(po,data=pjd,partial=True)
        if pd.is_valid():
            pd.save()
            return Response({"message":"update successfully"})
        
        else:
            return Response({"failed":"not updated"})
        

    def create(self,request):
        pjd=request.data
        pd=productmodelserializer(data=pjd)
        if pd.is_valid():
            pd.save()
            return Response({'message':'Product is Created'})
        else:
            return Response({'Failed':'Product is not created'})
  
        
    def destroy(self,request,pk):
        po=product.objects.get(pid=pk)
        po.delete()
        return Response({'message':'Product is Deleted'})


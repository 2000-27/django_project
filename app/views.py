from django.shortcuts import render
from .serializers import CustomerDetailsSerlizer
from .models import CustomerDetail
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["POST"])
def create_customer(request):
    try:
        data = request.data
        print(data)
        serializer = CustomerDetailsSerlizer(data=data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response({"success": True, "message": "done successfully"})
        return Response({"sucess": False, "message": serializer.errors})
    except Exception as e:
        return Response({"your error is ": str(e)})


@api_view(["GET"])
def view_customer(request):
    todo_objs = CustomerDetail.objects.all()
    serializer = CustomerDetailsSerlizer(todo_objs, many=True)
    return Response(
        {"success": True, "message": "data is fetch", "data": serializer.data}
    )

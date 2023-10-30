from .serializers import CustomerDetailsSerlizer
from .models import CustomerDetail
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.views import status


class CustomerAPI(APIView):
    def get(self, request, customer_id=None):
        id = customer_id
        if id is not None:
            try:
                customer = CustomerDetail.objects.get(id=id)
                serializer = CustomerDetailsSerlizer(customer)
                return Response(
                    {
                        "success": True,
                        "message": "data is fetch",
                        "data": serializer.data,
                    },
                    status=status.HTTP_200_OK,
                )
            except Exception as e:
                return Response(
                    {
                        "success": False,
                        "message": "no data is found",
                        "error": str(e),
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

        customer = CustomerDetail.objects.all()
        serializer = CustomerDetailsSerlizer(customer, many=True)
        return Response(
            {"success": True, "message": "data is fetch", "data": serializer.data},
            status=status.HTTP_200_OK,
        )

    def post(self, request, format=None):
        try:
            data = request.data
            serializer = CustomerDetailsSerlizer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"success": True, "message": "done successfully"},
                    status=status.HTTP_200_OK,
                )
            return Response(
                {"sucess": False, "message": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Exception as e:
            return Response({"your error is ": str(e)})

    def put(self, request, customer_id=None):
        try:
            id = customer_id
            if id is not None:
                customer = CustomerDetail.objects.get(id=id)
                serializer = CustomerDetailsSerlizer(customer, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(
                        {
                            "sucess": True,
                            "message": "uptdated ",
                        },
                        status=status.HTTP_200_OK,
                    )

                return Response(
                    {
                        "sucess": False,
                        "message": serializer.errors,
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except Exception as e:
            print(str(e))
            return Response(
                {
                    "sucess": False,
                    "message": "pls enter a valid id",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

from .serializers import CustomerDetailsSerlizer
from .models import CustomerDetail
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.views import status
from django_project.pagination import page


class CustomerAPI(APIView):
    def get(self, request, id=None):
        if id:
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
            except Exception:
                return Response(
                    {
                        "success": False,
                        "message": "Invalid id",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

        customer = CustomerDetail.objects.all()
        serializer = CustomerDetailsSerlizer(customer, many=True)
        data = page(serializer.data, self.request)
        return Response(
            data,
            status=status.HTTP_200_OK,
        )

    def post(self, request):
        try:
            serializer = CustomerDetailsSerlizer(data=request.data)
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
            return Response(
                {"sucess": False, "message": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def put(self, request, customer_id=None):
        try:
            if customer_id:
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
        except Exception:
            return Response(
                {
                    "sucess": False,
                    "message": "Invalid ID",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    def patch(self, request, id=None):
        try:
            if id:
                customer = CustomerDetail.objects.get(id=id)
                serializer = CustomerDetailsSerlizer(
                    customer, data=request.data, partial=True
                )
                if serializer.is_valid():
                    serializer.save()
                    return Response(
                        {
                            "sucess": True,
                            "message": "updated successfully",
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

        except Exception:
            return Response(
                {
                    "sucess": False,
                    "message": "invalid id",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    def delete(self, request, id=None):
        if id:
            try:
                customer = CustomerDetail.objects.get(id=id)
                customer.delete()
                return Response(
                    {
                        "sucess": True,
                        "message": "deleted",
                    },
                    status=status.HTTP_200_OK,
                )
            except Exception:
                return Response(
                    {
                        "sucess": False,
                        "message": "Invalid id",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import EmailDelivery as EmailDeliveryModel


class EmailDelivery(APIView):
    def get(self, request):
        """
        이전에 알림예약을 했는지 확인
        :param request:
        :return: boolean
        """
        user = request.user
        book_id = request.GET['book_id']
        if EmailDeliveryModel.objects.filter(user=user, book_id=book_id, send_email=False).exists():
            return Response(status=status.HTTP_200_OK, data={"data": True})
        return Response(status=status.HTTP_204_NO_CONTENT, data={"data": False})

    def post(self, request):
        """
        알림 예약 등록
        {"book_title":"한입에 쏙 파이썬", "book_id":1127719808}
        :param request:
        :return:
        """
        user = request.user
        book_title = request.data['book_title']
        book_id = request.data['book_id']
        EmailDeliveryModel.objects.create(user=user, book_title=book_title,
                                          book_id=book_id)
        return Response(status=status.HTTP_201_CREATED, data={"data": True})

    def delete(self, request):
        """
        알림 예약 삭제
        :param request:
        :return:
        """
        user = request.user
        book_id = request.GET['book_id']
        user_delivery = EmailDeliveryModel.objects.filter(user=user, book_id=book_id)
        if user_delivery.exists():
            user_delivery.delete()
            return Response(status=status.HTTP_204_NO_CONTENT, data={"data": True, "message": "해당 예약을 취소합니다."})
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"data": False, "message": "해당하는 예약이 없습니다."})

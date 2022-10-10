from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from app_goods.models import Item
from app_goods.serializers import ItemSerializer
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.pagination import PageNumberPagination


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 2

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 2

class ItemList(ListModelMixin, CreateModelMixin, GenericAPIView):
    """Представление для получения списка товаров и создания самого товара."""
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = Item.objects.all()
        item_name = self.request.query_params.get('name')
        if item_name:
            queryset = queryset.filter(name=item_name)
        return queryset

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)
# def items_list(request):
#     if request.method == 'GET':
#         item_for_sale = [
#             Item(
#                 name='Кофеварка',
#                 description='Варит отличный кофе',
#                 weight=100
#             ),
#             Item(
#                 name='Беспроводные наушники',
#                 description='Отличный звук',
#                 weight=150
#             )
#         ]
#         return JsonResponse(ItemSerializer(item_for_sale, many=True), safe=False)

class ItemDetail(UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericAPIView):
    """Представление для получения детальной информации о товаре,
    а также для его редактирования и удаления"""
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
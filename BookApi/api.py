from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from .models import BookModel

class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = '__all__'

    def validate(self, data):
        price = data['price']
        if price < 0:
            raise serializers.ValidationError('Price cannot be negative')
        return data

# @api_view(['GET'])
# def bookListApi(request):
#     books = BookModel.objects.all()
    
#     serializer = BookModelSerializer(books, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def bookDetailApi(request, id):
#     try:
#         book = BookModel.objects.get(id=id)

#         serializer = BookModelSerializer(book)
#         return Response(serializer.data)
#     except:
#         return serializers.ValidationError('Book not found')

# @api_view(['POST'])
# def bookCreateApi(request):
#     data = request.data

#     serializer = BookModelSerializer(data = data)

#     if serializer.is_valid():
#         serializer.save()
#         return Response({
#             'message': 'Book successfully created'})
    
#     return Response(serializer.errors)

# @api_view(['PUT'])
# def bookUpdateApi(request, id):
#     data = request.data

#     book = BookModel.objects.get(id=id)

#     serializer = BookModelSerializer(instance = book, data = data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({
#             'message': 'Book updated successfully!'
#         })

#     return Response(
#         {
#             'message': 'Book not updated'
#         }
#     )

# @api_view(['DELETE'])
# def bookDeleteApi(request, id):
#     book = BookModel.objects.get(id=id)

#     book.delete()

#     return Response(
#         {
#             'message': 'Book successfully deleted.'
#         }
#     )

from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination,CursorPagination

# #For multiple viewset, create custom pagination using PageNumberPagination
# class CustomPagination1(PageNumberPagination):
#     page_size = 3

# class CustomPagination2(PageNumberPagination):
#     page_size = 2

# class CustomPagination3(PageNumberPagination):
#     page_size = 6

# #For LimitOffsetPagination
# class CustomPagination(LimitOffsetPagination):
#     limit_query_param = 'limit'
#     offset_query_param = 'offset'

#For CursorPagination
class CustomPagination(CursorPagination):
    page_size = 4
    ordering = 'price'

class BookViewSet(ModelViewSet):
    queryset = BookModel.objects.all()
    serializer_class = BookModelSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

    def list(self, request):
        user = request.user
        books = BookModel.objects.filter(author = user)
        page = self.paginate_queryset(books)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)
    
    def create(self, request):
        data = request.data

        serializer = self.get_serializer(data = data)

        if serializer.is_valid():
            serializer.save()

        return Response({
            'message':'Book created successfully'
        })
    
    def update(self, request, pk):
        
        book = BookModel.objects.get(id=pk)

        if book.author == request.user:
            data = request.data

            serializer = self.get_serializer(instance = book, data = data)

            if serializer.is_valid():
                serializer.save()

            return Response({
                'message':'Book updated successfully!'
            })
        
        return Response({
            'message':'You are not the author of this book'
        })
        
    def destroy(self, request, pk):
        user = request.user
        if not user.is_authenticated:
            return Response({
                'message':'User is not logged in!'
            })
        
        book = BookModel.objects.get(id=pk)

        if book.author == user:
            book.delete()

            return Response({
                'message':'Book deleted successfully!'
            })
        
        return Response({
            'message': 'You are not authorized to delete this book!'
        })
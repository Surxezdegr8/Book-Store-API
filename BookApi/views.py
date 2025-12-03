from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import serializers
from .models import BookModel

#using serializer for the handling validation
class SerializerModel(serializers.ModelSerializer):
    class Meta:
        models = BookModel
        fields = '__all__'

    def validate(self, data):
        price = data['price']
        if price < 0:
            raise serializers.ValidationError('Price cannot be negative')
        return data


#GET Request
@api_view(['GET'])
def listBooks(request):
    #Fetch all the data from the database
    books = BookModel.objects.all()
    #Convert the data to JSON format
    books = [
        {
            'name' : book.name,
            'author' : book.author
        } for book in books
    ]
    #Send response
    return Response(books)

#POST Request
@api_view(['POST'])
def createBooks(request):
    
    '''
    #fetch the data to be posted as request
    data = request.data
    #assign the corresponding values to the variables of the data request
    name = data["name"] #had to access the key of the dictionary because the request from postman is a dictionary
    author = data["author"] #accessing the author key in the dictionary
    #save into the database
    BookModel(name = name, author = author).save() #without the .save() the values would not be saved into the database though the code would return successful if there are no pending issues, it won't save to the database, hence, when listed you won't see the newly added data.
    '''

    data = request.data

    serializers = SerializerModel(data=data)

    if serializers.is_valid():
        serializers.save()
        #send response
        return Response({
            'message': 'Book created successfully'})
    return Response(serializers.errors)

@api_view(['PUT'])
def updateBooks(request, id):
    #fetch the request data which is gotten from postman
    data = request.data

    #get the specific book by it id from the database
    book = BookModel.objects.get(id=id)
    
    #do the update of the specific data with id
    book.name = data['name'] #this is where the name of the book in the database is now assigned to the name in the dictionary of the postman
    book.author = data['author'] #this is where the name of the author in the database is replaced by whatever name is inputed in the dictionary on postman.

    book.save()

    return Response(
        {
            'message': 'Book updated successfully'
        }
    )
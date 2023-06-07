from rest_framework import viewsets
from .models import Books
from .serializers import BookSerializer
from rest_framework import request, response, filters, generics
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, ListCreateAPIView
from django.db import connections
from rest_framework.response import Response
from djangotest.helper import *

class FindBook(generics.ListAPIView):
    search_fields = ['title','author','publication_date']
    filter_backends = (filters.SearchFilter,)
    queryset = Books.objects.all()
    serializer_class = BookSerializer

class BorrowBook(APIView):

    def dictfetchall(self, cursor):
        columns = [col[0].lower() for col in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]
    
    def post(self, request, format=None):
        id                  = request.data.get('id')
        username            = request.data.get('username')
        title               = request.data.get('title')
        author              = request.data.get('author')
        publication_date    = request.data.get('publication_date')

        id_count = id.split("\n")

        id_tot = len(id_count)

        if id_tot > 3:
            output = {'info': 'Maximum of 3 books' , 'code':55, 'data':None}
            return Response(output)
        

        with transaction.atomic():
            try:
                for x in id_count:

                    dataInsert                                      = {}
                    dataInsert['id_books']                          = x  
                    dataInsert['username']                          = username 
                    dataInsert['title']                             = title
                    dataInsert['author']                            = author 
                    dataInsert['publication_date']                  = publication_date
                    dataInsert['status_borrow']                     = '1'
                    dataInsert['id_status_books_id']                = '0'

                    saveData = saveGlobal('borrow_book', dataInsert)

                    if saveData['code'] != 0:
                        transaction.set_rollback(True)
                        return Response(saveData)
                    
            except Exception as e:
                transaction.set_rollback(True)
                return  Response({'info':str(e), 'code':20, 'data':None})

        
        return Response({'info':'Successfully submitting a book loan, please wait for the next status' , 'code':0, 'data':None})
    
class ConfirmBook(APIView):
    
    def post(self, request, format=None):

        id          = request.data.get('id')
        username    = request.data.get('username')
        id_count    = id.split("\n")
        type        = request.data.get('type')

        if type == 'borrow':

            with transaction.atomic():
                try:
                    for x in id_count:

                        dataupdate                  = {}
                        dataupdate['status_borrow'] = '2'

                        updateData = updateGlobal('borrow_book', dataupdate, "id_books = '%s' and status_borrow ='0'"%(id))

                        if updateData['code'] != 0:
                            transaction.set_rollback(True)
                            return Response(updateData)
                        
                except Exception as e:
                    transaction.set_rollback(True)
                    return  Response({'info':str(e), 'code':20, 'data':None})

            
            return Response({'info':'Sukses Melakukan Confirmasi Pengajuan Buku' , 'code':0, 'data':None})
        
        if type == 'return':
            with transaction.atomic():
                try:
                    for x in id_count:

                        dataupdate                              = {}
                        dataupdate['status_return']             = '2'

                        updateData = updateGlobal('borrow_book', dataupdate, "id_books = '%s' "%(id))

                        if updateData['code'] != 0:
                            transaction.set_rollback(True)
                            return Response(updateData)
                        
                except Exception as e:
                    transaction.set_rollback(True)
                    return  Response({'info':str(e), 'code':20, 'data':None})
        
            return Response({'info':'Sukses Melakukan Return Buku' , 'code':0, 'data':None})
        
        return Response({'info':'Type Not Matched' , 'code':0, 'data':None})

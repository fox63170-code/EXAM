from rest_framework.viewsets import ModelViewSet
from .models import Book
from .serializers import BookSerializer

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        is_read_param = self.request.query_params.get('is_read')
        
        if is_read_param is not None:
         
            is_read_bool = is_read_param.lower() == 'true'
            queryset = queryset.filter(is_read=is_read_bool)

        return queryset
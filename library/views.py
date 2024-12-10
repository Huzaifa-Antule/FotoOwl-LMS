from django.shortcuts import render
from django.http import HttpResponse
import csv
# Create your views here.
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Book, BorrowRequest
from .serializers import (
    UserSerializer,
    BookSerializer,
    BorrowRequestSerializer,
    BorrowHistorySerializer,
)
from django.contrib.auth.models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BorrowRequestViewSet(viewsets.ModelViewSet):
    queryset = BorrowRequest.objects.all()
    serializer_class = BorrowRequestSerializer

    def create(self, request, *args, **kwargs):
        """Handle borrow request creation with overlap checks."""
        user = request.user
        book_id = request.data.get('book')
        start_date = request.data.get('start_date')
        end_date = request.data.get('end_date')

        # Check for overlapping borrow dates
        if BorrowRequest.objects.filter(
            book_id=book_id,
            start_date__lte=end_date,
            end_date__gte=start_date,
            status='approved',
        ).exists():
            return Response(
                {"error": "Book is already borrowed during this period."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        request.data['user'] = user.id
        return super().create(request, *args, **kwargs)

    @action(detail=False, methods=['get'])
    def history(self, request):
        """View personal borrow history."""
        user = request.user
        history = BorrowRequest.objects.filter(user=user).order_by('-start_date')
        serializer = BorrowHistorySerializer(history, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'], url_path='download-history')
    def download_borrow_history(self, request):
        borrow_history = BorrowRequest.objects.filter(user=request.user)
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="borrow_history_{request.user.username}.csv"'

        writer = csv.writer(response)
        writer.writerow(['Book Title', 'Start Date', 'End Date', 'Status'])

        for borrow in borrow_history:
            writer.writerow([borrow.book.title, borrow.start_date, borrow.end_date, borrow.status])

        return response


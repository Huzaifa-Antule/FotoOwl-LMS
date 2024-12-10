from rest_framework.routers import DefaultRouter
from .views import UserViewSet, BookViewSet, BorrowRequestViewSet

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('books', BookViewSet)
router.register('borrow-requests', BorrowRequestViewSet)
urlpatterns = router.urls

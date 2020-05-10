from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet

router = DefaultRouter()
router.register(r'', ArticleViewSet, basename='articles')
urlpatterns = router.urls

# from django.urls import path
# from .views import ArticalListView, ArticalDetailView,ArticalCreateView
# urlpatterns = [
#     path('',ArticalListView.as_view()),
#     path('create/',ArticalCreateView.as_view()),
#     path('<pk>/',ArticalDetailView.as_view()),
# ]

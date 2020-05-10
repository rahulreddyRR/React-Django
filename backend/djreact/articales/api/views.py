from rest_framework import viewsets
from .serializer import ArticalSerializer
from articales.models import Articals



class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticalSerializer
    queryset = Articals.objects.all()

# from rest_framework.generics import  ListAPIView,RetrieveAPIView,CreateAPIView
# from articales.models import Articals
# from .serializer import ArticalSerializer

# class ArticalListView(ListAPIView):
#     queryset = Articals.objects.all()
#     serializer_class = ArticalSerializer

# class ArticalDetailView(RetrieveAPIView):
#     queryset = Articals.objects.all()
#     serializer_class = ArticalSerializer


# class ArticalCreateView(CreateAPIView):
#     queryset = Articals.objects.all()
#     serializer_class = ArticalSerializer
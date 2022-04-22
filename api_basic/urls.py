from django.conf.urls import include
from django.urls import path

from .views import ArticleDetails, ArticleViewSet, GenericAPIView, article_list, article_detail, ArticleAPIView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    # path('article/', article_list),
    path('article/', ArticleAPIView.as_view()),
    # path('article/', GenericAPIView.as_view()),
    # path('article/<int:pk>/', article_detail)
    path('article/<int:pk>/', ArticleDetails.as_view())
]

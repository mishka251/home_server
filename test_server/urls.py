from django.urls import include, path
from rest_framework import routers
from books import views
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'books', views.BooksList)
router.register(r'authors', views.AuthorView)
router.register(r'genres', views.GenresView)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('', views.index),
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('download/', views.download),
    path('api/v1/upload/', views.load_book),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import include, path
from rest_framework import routers
from books import views
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'api/v1/users', views.UserViewSet)
router.register(r'api/v1/groups', views.GroupViewSet)
router.register(r'api/v1/books', views.BooksList)
router.register(r'api/v1/authors', views.AuthorView)
router.register(r'api/v1/genres', views.GenresView)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('', views.index),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('download/', views.download),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import path, include
from books import views
from rest_framework import routers


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
    path('download/', views.download),
    path('api/v1/upload/', views.load_book),
    path('api/v1/', include(router.urls)),
    path('authors/<int:author_id>', views.author),
    path('books/<int:book_id>', views.book),
]
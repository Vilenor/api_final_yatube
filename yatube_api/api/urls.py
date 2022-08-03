from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'api'

router = DefaultRouter()
router.register('posts', views.PostViewSet)
router.register('groups', views.GroupViewSet)
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    views.CommentViewSet,
    basename='comments',
)
router.register('follow', views.FollowViewSet, basename='follow',)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]

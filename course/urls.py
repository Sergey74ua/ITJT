from django.urls import path
from . import views

urlpatterns = [
    path('', views.course, name='course'),
    path('create', views.courseCreate, name='courseCreate'),
    path('<int:pk>', views.CourseDetail.as_view(), name='courseDetail'),
    path('<int:pk>/update', views.CourseUpdate.as_view(), name='courseUpdate'),
    path('<int:pk>/delete', views.CourseDelete.as_view(), name='courseDelete')
]
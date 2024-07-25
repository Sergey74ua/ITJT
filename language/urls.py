from django.urls import path
from . import views

urlpatterns = [
    path('', views.language, name='language'),
    path('create', views.langCreate, name='langCreate'),
    path('<int:pk>', views.LangDetail.as_view(), name='langDetail'),
    path('<int:pk>/update', views.LangUpdate.as_view(), name='langUpdate'),
    path('<int:pk>/delete', views.LangDelete.as_view(), name='langDelete')
]
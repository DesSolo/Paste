from django.urls import path
from . import views

urlpatterns = [
        path('', views.CreateCodePasteView.as_view(), name='index'),
        path('paste/<pk>', views.PasteDetails.as_view(), name='detail'),
        path('raw/<pk>', views.Raw.as_view(), name='raw'),
        path('dl/<pk>', views.Download.as_view(), name='download'),
]

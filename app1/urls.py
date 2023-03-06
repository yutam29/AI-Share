from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lending', views.lending, name='lending'),
    path('request', views.req, name='request'),
    path('detail/<int:item_id>', views.detail, name='detail'),
    path('item_upload', views.item_upload, name='item_upload'),
    path('deliver/<int:item_id>', views.deliver_register, name='deliver'),
    path('state/<int:list_id>', views.change_state, name='change_state'),
]
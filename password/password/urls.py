from . import views
from django.urls import path

urlpatterns = [
    path('table/', views.table, name='table-url'),
    path('table/change/', views.change_table, name='change-table-url'),
    path('table/delete/', views.delete_table, name='delete-table-url'),
    path('table/decode/', views.decode_password, name='decode-password-url'),
]

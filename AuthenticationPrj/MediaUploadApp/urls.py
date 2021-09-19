from django.urls import path
from . import views


urlpatterns=[
    path('upload/',views.uploadView),
    path('books/',views.book_list,name='books'),
    path('bookupload/',views.upload_book,name='bookupload')

]

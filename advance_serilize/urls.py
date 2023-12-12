from django.urls import path,include
from advance_serilize.views import CreateFist,GetAllPublisher
urlpatterns_v1=[
    path('create-first',CreateFist.as_view(),name='create_first'),
    path('get-all-publisher',GetAllPublisher.as_view(),name='get_all_publisher')

]


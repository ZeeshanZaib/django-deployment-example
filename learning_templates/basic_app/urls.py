from django.conf.urls import url
from basic_app import views


# urlpatterns = [
#     url(r'^$',views.,name='index'),
#     url(r'^relative/',views.relative,name='relative'),
#     url(r'^other/',views.other,name='other'),
# ]


app_name='basic_app'



urlpatterns = [
    # url(r'^$',views.,name='index'),
    url(r'^relative/',views.relative,name='relative'),
    url(r'^other/',views.other,name='other'),
]
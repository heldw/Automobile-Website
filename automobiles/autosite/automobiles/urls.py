from django.conf.urls import url
 
from automobiles import views
 
app_name = 'automobiles'
 
urlpatterns = [
 
    # /automobiles/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # /motorcycles/
    url(r'^car/motorcycles/$', views.IndexView2.as_view(), name='index2'),
    # /carownerownscars/
    url(r'^car/personownscars/$', views.IndexView3.as_view(), name='index3'),
     # /carowners/
    url(r'^car/person/$', views.IndexView4.as_view(), name='index4'),
    # /carownerownscars/
    url(r'^car/personownsmotorcycles/$', views.IndexView5.as_view(), name='index5'),
    # /carownerownscars/
   # url(r'^car/index6/$', views.IndexView6.as_view(), name='index6'),
 
    # cars/car/entry
    url(r'^car/entry/$',views.CarEntry.as_view(),name='car-entry'),
    url(r'^car/motorcycles/entry/$',views.MotorcycleEntry.as_view(),name='motorcycle-entry'),
    url(r'^car/personownscars/entry/$',views.PersonOwnsCarEntry.as_view(),name='personownscar-entry'),
    url(r'^car/person/entry/$',views.PersonEntry.as_view(),name='person-entry'),
    url(r'^car/personownsmotorcycle/entry/$',views.PersonOwnsMotorcycleEntry.as_view(),name='personownsmotorcycle-entry'),
 
    # cars/car/2
    url(r'^car/(?P<pk>[0-9]+)/$', views.CarUpdate.as_view(), name='car-update'),
    url(r'^car/motorcycles/(?P<pk>[0-9]+)/$', views.MotorcycleUpdate.as_view(), name='motorcycle-update'),
    url(r'^car/personownscars/(?P<pk>[0-9]+)/$', views.PersonOwnsCarUpdate.as_view(), name='personownscar-update'),
    url(r'^car/person/(?P<pk>[0-9]+)/$', views.PersonUpdate.as_view(), name='person-update'),
    url(r'^car/personownsmotorcycles/(?P<pk>[0-9]+)/$', views.PersonOwnsMotorcycleUpdate.as_view(), name='personownsmotorcycle-update'),
 
    # cars/car/(?P<pk>[0-9]+)/delete
    #url(r'^car/(?P<pk>[0-9]+)/delete$', views.CarDelete.as_view(), name='car-delete'),
 
]

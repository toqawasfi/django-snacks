from django.contrib import admin
from django.urls import path
from.views import HomePageView,AboutPageView


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', HomePageView.as_view(),name='home'),#Home page endpoint
    path('about', AboutPageView.as_view(),name='about')#About page endpoint

]



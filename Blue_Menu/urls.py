"""Blue_Menu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from menu.views import CardDetailView, CardListView, FinalView
from menu.api.views import CardListApiView
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^docs/', include_docs_urls(title='My API service')),

    url(r'^cards/$', CardListView.as_view(), name='cards'),
    url(r'^card/(?P<pk>(\d)+)/$', CardDetailView.as_view(), name='card'),
    url(r'^final/$', FinalView.as_view(), name='final'),

    url(r'^cardsAPI/$', CardListApiView.as_view(), name='cards-api'),


]

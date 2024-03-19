"""
URL configuration for mental_healthnetwork project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from resources.views  import*
from django.conf.urls.static import static
from django.conf import settings

from EmergencySupport.views import*
from events.views import upcoming_events, seminars, workshops




urlpatterns = [
    path('admin/', admin.site.urls),
    path('resources-page/', resources, name='resources'),
    path('emergency-support/',EmergencySupport,name='emergencysupport'),
    path('upcoming-events/', upcoming_events, name='upcoming_events'),
    path('seminars/', seminars, name='seminars'),
    path('workshops/', workshops, name='workshops')
  
]

## for managing the media 
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)





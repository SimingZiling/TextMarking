"""SE_Team_demo1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from index.views import *
from SE_Team_demo1 import settings
from django.conf.urls.static import static
from project.text import import_text

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/project/', include('project.urls')),
                  path('user/', include('register.urls')),
                  path('index/', showIndex),
                  path('main/', showMain),
                  path('mgraph/', showGraph),
                  path('invite/', showInvite),
                  path('export/', showExport),
                  path('import', import_text)
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

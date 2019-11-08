"""controle_estoque URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
import adminactions.actions as actions

actions.add_to_site(admin.site)

admin.site.site_header = "Controle de Estoque"
admin.site.site_title = "Controle de Estoque"
admin.site.index_title = "Controle de Estoque"

urlpatterns = [
    path('adminactions/', include('adminactions.urls')),
    path('', admin.site.urls),
]

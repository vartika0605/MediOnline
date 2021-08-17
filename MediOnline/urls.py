"""nearbyshops URL Configuration

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
from django.urls import path,include
from donation import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('findDonors/', views.findDonors.as_view(), name = 'findDonors'),
    path('needPlasma/',views.needPlasma,name= 'needPlasma'),
    path('findNeeders/', views.findNeeders.as_view(),name='findNeeders'),
    path('donatePlasma/',views.donatePlasma,name= 'donatePlasma'),
    path('' , include('accounts.urls')),
    path('doctor/' , include('doctorconsult.urls')),
    path('needdelete/<int:post_id>', views.NeedDeleteView.as_view(), name='needdelete'),
    path('donatedelete/<int:post_id>', views.DonateDeleteView.as_view(), name='donatedelete'),
    path("select2/", include("django_select2.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

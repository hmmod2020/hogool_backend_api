"""hogool_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path
from api_hogool import views as vs
from rest_framework.authtoken import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('singUp/', vs.create_new_user,name='signUp'),
    path('api-token-auth/', views.obtain_auth_token),
    path('usertype/', vs.getUserType),
    path('profileComplete/', vs.completeProfile),
    path('addNewAdmin/', vs.addNew),
    path('news/<int:id>/', vs.getNews),
    path('addLand/', vs.createLand),
    path('addCrop/', vs.addCrop),
    path('Crops/', vs.showAllCrop),
    path('land/<int:id>/', vs.showLand),
    path('myLand/', vs.showUserLand),
    path('change_new_state/<int:id>/', vs.changeNewState),
    path('change_land_state/<int:id>/', vs.changeLandState),
    path('activateUser/<int:id>/', vs.activateUser)




]

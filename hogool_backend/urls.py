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
    path('api-token-auth/', views.obtain_auth_token),
    path('singUp/', vs.create_new_user, name='signUp'),
    path('usertype/', vs.getUserType),
    path('profileComplete/', vs.completeProfile),
    path('addNewAdmin/', vs.addNew),
    path('addLand/', vs.createLand),
    path('addCrop/', vs.addCrop),
    path('addCropFarmer/', vs.farmerAddCrop),
    path('showCropFarmer/<int:id>/', vs.farmerGetCrop),
    path('Crops/', vs.showAllCrop),
    path('change_new_state/<int:id>/', vs.changeNewState),
    path('change_land_state/<int:id>/', vs.changeLandState),
    path('activateUser/<int:id>/', vs.activateUser),
    path('show_farmer/<int:id>/', vs.showFarmer),
    path('show_farmer/<int:id>/',vs.showInvestor),
    path('land/<int:id>/', vs.showLand),
    path('land_filtter/', vs.showLandFiltter),
    path('myLand/', vs.showUserLand),
    path('news/<int:id>/', vs.getNews),
    path('create_invesment_offer/', vs.createNewOffer),
    path('invesment_offers/<int:id>/', vs.showOffer),
    path('investor_offers/', vs.showMyOffer),
    path('investor_offers_admin/', vs.showAllOffer),
    path('change_offer_state/<int:id>/', vs.changeOfferState),
    path('order_rent/<int:id>/', vs.createOredrRent),
    path('my_rent/<int:id>/', vs.showMyOrderRentO),
    path('my_order_rent/<int:id>/', vs.showMyOrderRentRequestU),
    path('notifi_rent/<int:id>/', vs.changeStateOrderRent),
    path('order_rent_filter/', vs.showMyOrderRentUF),
    path('my_rent_filter/', vs.showMyOrderRentOF),
    path('create_order_job_by_farmer/', vs.createOrderJobF),
    path('create_order_job_by_investor/', vs.createOrderJobI),
    path('show_order_Job_farmer_order/', vs.showOrderJobFO),
    path('show_order_Job_farmer_order_filter/', vs.showOrderJobFOFilter),
    path('show_order_Job_farmer_notfication/', vs.showOrderJobFN),
    path('show_order_Job_farmer_notfication_filter/', vs.showOrderJobFNFilter),
    path('show_order_Job_investor_order/', vs.showOrderJobIO),
    path('show_order_Job_investor_order_filter/', vs.showOrderJobIOFilter),
    path('show_order_Job_investor_notfication/', vs.showOrderJobIN),
    path('show_order_Job_investor_notfication_filter/', vs.showOrderJobINFilter),
    path('select_job/<int:id>/', vs.showOrderJob),
    path('change_job_state/', vs.changeJobState),
]

"""
URL configuration for Grace_Times_And_Eletronics project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from Grace import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('home/',views.home),
    path('about/',views.about),
    path('contact/',views.contact),
    path('products/',views.product),
    path('reservation/',views.reservation),
    path('testimonial/',views.testimonial),
    path('ourstory/',views.ourstory),
    path('ourvision/',views.ourvision),
    path('adminmenu/',views.adminmenu),
    path('addcategory/',views.addcategory),
    path('actioncategory/',views.actioncategory),
    path('updateviewcategory/',views.updateviewcategory),
    path('updatecategory/<str:a>',views.updatecategory),
    path('updateactioncategory/<str:a>',views.updateactioncategory),
    path('deletecategory/',views.deletecategory),
    path('actiondeletecategory/<str:a>',views.actiondeletecategory),
    path('addshope/',views.addshope),
    path('actionshope/',views.actionshope),
    path('updateviewshope/',views.updateviewshope),
    path('updateshope/<str:a>',views.updateshope),
    path('updateactionshope/<str:a>',views.updateactionshope),
    path('deleteshope/',views.deleteshope),
    path('deleteactionshope/<str:a>',views.deleteactionshope),
    path('shopemenu/',views.shopemenu),
    path('addproduct/',views.addproduct),
    path('actionproduct/',views.actionproduct),
    path('updateviewproduct/',views.updateviewproduct),
    path('updateproduct/<str:a>',views.updateproduct),
    path('updateactionproduct/<str:a>',views.updateactionproduct),
    path('deleteproduct/',views.deleteproduct),
    path('deleteactionproduct/<str:a>',views.deleteactionproduct),
    path('viewproduct/<str:id>',views.viewproduct),
    path('coustomermenubar/',views.coustomermenu),
    path('coustomerviewcategory/',views.coustomerviewcategory),
    path('coustomerviewproduct/<str:id>',views.coustomerviewproduct),
    path('coustomerregistration/',views.coustomerregistration),
    path('actioncoustomerregistration/',views.actioncoustomerregistration),
    path('coustomerlogin/',views.coustomerlogin),
    path('adminhome/',views.adminhome),
    path('shopehome/',views.shopehome),
    path('coustomerhome/',views.coustomerhome),
    path('loginaction/',views.loginaction),
    path('productdetails/<str:id>',views.productdetails),
    path('orderdetails/<str:id>',views.orderdetails),
    path('order/',views.order),
    path('shopeorder/',views.shopeorder),
    path('shopevieworder/<str:id>',views.shopevieworder),
    path('coustomerpostreview/<str:id>',views.coustomerpostreview),
    path('coustomerviewreview/<str:id>',views.coustomerviewreview),
    path('actionreview/',views.actionreview),
    path('acceptorder/<str:id>',views.acceptorder),
    path('rejectorder/<str:id>',views.rejectorder),
    path('shopereview/',views.shopereview),
    path('shopeviewreview/<str:id>',views.shopeviewreview),
    path('coustomervieworder/',views.coustomervieworder),
    path('coustomerviewonthewayorder/',views.coustomerviewonthewayorder),
    path('coustomerrejectvieworder/',views.coustomerrejectvieworder),
    path('coustomerdelivredvieworder/',views.coustomerdelivredvieworder),
    path('coustomerviewpendingorder/',views.coustomerviewpendingorder),
    path('coustomerviewacceptedorders/',views.coustomerviewacceptedorders),
    path('coustomerviewreviewdelete/',views.coustomerviewreviewdelete),
    path('deletecoustomerreview/<str:id>',views.deletecoustomerreview),
    path('agenthome/',views.agenthome),
    path('deliveryagentmenubar/',views.deliveryagentmenubar),
    path('adddeliveryagent/',views.adddeliveryagent),
    path('actionaddagent/',views.actionaddagent),
    path('devileryagentviewdelete/',views.devileryagentviewdelete),
    path('deleteactiondeliveryagent/<str:a>',views.deleteactiondeliveryagent),
    path('updateviewdeliveryagent/',views.updateviewdeliveryagent),
    path('updatedeliveryagent/<str:a>',views.updatedeliveryagent),
    path('updateactiondeliveryagent/<str:a>',views.updateactiondeliveryagent),
    path('deliveryagentvieworder/',views.deliveryagentvieworder),
    path('deliveryagentacceptorder/<str:id>',views.deliveryagentacceptorder),
    path('deliveryagentdelivered/',views.deliveryagentdelivered),
    path('actiondeliveryagentdelivered/<str:id>',views.actiondeliveryagentdelivered),
    path('viewreview/<str:id>',views.viewreview),
    path('adminviewproduct/',views.adminviewproduct),
    path('adminviewreview/<str:id>',views.adminviewreview),
    path('adminviewreport/',views.adminviewreport),
    path('adminactionviewreport/<str:id>',views.adminactionviewreport),
    path('forgetpassword/',views.forgetpassword),
    path('forgetpasswordchange/<str:id>',views.forgetpasswordchange),
    path('forgetpasswordaction/',views.forgetpasswordaction),
    path('adminlogout/',views.adminlogout),
    path('shopelogout/',views.shopelogout),
    path('coustomerlogout/',views.coustomerlogout),
    path('deliveryagentlogout/',views.deliveryagentlogout),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



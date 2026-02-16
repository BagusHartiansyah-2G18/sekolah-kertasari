from django.urls import path,include
# from app.views.Vpage import dashboard,data,pengusaha,denda,wilaya,monitoring
from app.views.views import home, about, programs, faq, contact, login

# from app.views.Vapi.VAsimtax import simtax_login,simtax_get_transaksi,TransaksiPajakViewSet


# from rest_framework.routers import DefaultRouter
# router = DefaultRouter()
# router.register(r'transaksipajak', TransaksiPajakViewSet)



urlpatterns = [
    # path('dashboard', dashboard, name='dashboard'),
    path('', home, name='home'),
    path('about', about, name='about'),
    path('programs', programs, name='programs'),
    path('faq', faq, name='faq'),
    path('contact', contact, name='contact'),
    path('login', contact, name='login'),
    # path('pengusaha', pengusaha, name='pengusaha'),
    # path('data', data, name='data'),
    # path('denda', denda, name='denda'),
    # path('wilaya', wilaya, name='wilaya'),
    # path('monitoring', monitoring, name='monitoring'),
    
    
    
    # path("proxy/simtax/login/", simtax_login),
    # path("proxy/simtax/data/", simtax_get_transaksi),
    # path('api/', include(router.urls)),
]

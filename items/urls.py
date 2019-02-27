from . import views
from django.conf.urls import url,include

urlpatterns = [
    url(r'^signup/$', views.UserSignupView, name="signup"),
    url(r'^login/$', views.UserLoginView.as_view(), name="login"),
    url(r'^logout/$', views.logout, name="logout"),
    url(r'^$', views.indexview, name="index"),
    #url(r'^detail/(?P<idd>[0-9]+)/$',views.ProductView().as_view(),name='detail'),
    #url(r'^detail/$',views.ProductView,name='detail'),
    url(r'^detail/(?P<idd>[0-9]+)/$',views.productview1,name='detail1'),
    #url(r'^detail/(?P<idd>[0-9]+)/$',views.ProductView().as_view(),name='detail')
    #url(r'^blog/$',views.blogview,name='blog'),
    #url(r'^blog/single-blog$',views.singleblog,name='singleblog'),
    url(r'^cart/$',views.newcart,name='newcart'),
    url(r'^cart1/(?P<cartid>[0-9]+)/$',views.cart1,name='cart1'),


    url(r'^cart/(?P<idd>[0-9]+)/$',views.add_to_cart,name='add_to_cart'),

    url(r'^contact/$',views.contact,name='contact'),
    url(r'^shop/(?P<idd>[0-9]+)/$',views.shop,name='shop'),
    url(r'^blog/$',views.blogview,name='blog'),
    url(r'^regular/$',views.regular,name='regular'),
    url(r'^ppal-return/$',views.ppal_return,name='return'),
    url(r'^ppal-cancel/$',views.ppal_cancel,name='cancel'),
    url(r'^qwerty/$',include('paypal.standard.ipn.urls')),

]

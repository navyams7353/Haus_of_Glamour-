from django.urls import path
from.import views
urlpatterns = [
    path('userindex',views.userindex,name='userindex'),
    path('category_card',views.category_card,name='category_card'),
    path('cat_viewmore/<int:id>/',views.cat_viewmore,name='cat_viewmore'),
    path('service_card/<str:category>/',views.service_card,name='service_card'),
    path('service_viewmore/<int:id>/',views.service_viewmore,name='service_viewmore'),
    path('about',views.about,name='about'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('log',views.log,name='log'),
    path('userlogout',views.userlogout,name='userlogout'),
    path('reg',views.reg,name='reg'),
    path('booking/<int:id>/',views.booking,name='booking'),
    path('book/',views.book,name='book'),
    path('branches',views.branches,name='branches'),
    path('success_page',views.success_page,name='success_page'),
    path('branch_card',views.branch_card,name='branch_card'),
    path('contact',views.contact,name='contact'),
    path('contactus',views.contactus,name='contactus'),
    ]
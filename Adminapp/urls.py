from django.urls import path
from.import views
urlpatterns = [
    path('',views.index,name='index'),
    path('category',views.category,name='category'),
    path('form',views.form,name='form'),
    path('cat_table',views.cat_table,name='cat_table'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('service',views.service,name='service'),
    path('edit_services/<int:id>/',views.edit_services,name='edit_services'),
    path('update_service/<int:id>/',views.update_service,name='update_service'),
    path('delete_service/<int:id>/',views.delete_service,name='delete_service'),
    path('service_table',views.service_table,name='service_table'),
    path('products',views.products,name='products'),
    path('booking_table',views.booking_table,name='booking_table'),
    path('reg_table',views.reg_table,name='reg_table'),
    path('branch',views.branch,name='branch'),
    path('Bran',views.Bran,name='Bran'),
    path('branch_table',views.branch_table,name='branch_table'),
    path('delete_branch/<int:id>/',views.delete_branch,name='delete_branch'),
    path('delete_appoinment/<int:id>/',views.delete_appoinment,name='delete_appoinment'),
    path('approve/<int:id>/',views.approve,name='approve'),
    path('contact_table',views.contact_table,name='contact_table')
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('vinyls/', views.vinyls_index, name='index'),
    path('vinyls/<int:vinyl_id>/', views.vinyls_detail, name='detail'),
    path('vinyls/create/', views.VinylCreate.as_view(), name='vinyls_create'),
    # CBVs that work with individual model instances expect to find a named parameter of 'pk'
    path('vinyls/<int:pk>/update/', views.VinylUpdate.as_view(), name='vinyls_update'),
    path('vinyls/<int:pk>/delete/', views.VinylDelete.as_view(), name='vinyls_delete'),
    path('vinyls/<int:vinyl_id>/add_purchase/', views.add_purchase, name='add_purchase'),
    # person URLs
    path('buyers/', views.BuyerList.as_view(), name='buyers_index'),
    path('buyers/<int:pk>', views.BuyerDetail.as_view(), name='buyers_detail'),
    path('buyers/create', views.BuyerCreate.as_view(), name='buyers_create'),
    path('buyers/<int:pk>/update/', views.BuyerUpdate.as_view(), name='buyers_update'),
    path('buyers/<int:pk>/delete/', views.BuyerDelete.as_view(), name='buyers_delete'),
    # M:M relationship between Buyer and Vinyl
    path('vinyls/<int:vinyl_id>/assoc_buyer/<int:buyer_id>/', views.assoc_buyer, name='assoc_buyer'),
]
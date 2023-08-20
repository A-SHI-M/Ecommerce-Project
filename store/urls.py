from django.urls import path
from store import views

app_name = 'store'
urlpatterns = [
    path('', views.HomeListView.as_view(), name='index'),
    path('product/<slug>/', views.ProductDetailView.as_view(), name = 'product-details'),
    path('reviewform/<int:pk>', views.ReviewForm, name = 'reviewform'),
    path('reviewsub/<int:pk>', views.ReviewSub, name = 'reviewsub'),
]
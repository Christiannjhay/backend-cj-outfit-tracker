from django.urls import path
from .views import OutfitDetailView, OutfitListCreateView, UserListCreateView, UserRetrieveUpdateDestroyView, UserLoginView, UserLogoutView, csrf_token_view


urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user-detail'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
     path('outfits/', OutfitListCreateView.as_view(), name='outfit-list-create'),
    path('outfits/<int:pk>/', OutfitDetailView.as_view(), name='outfit-detail'),
     path('csrf-token/', csrf_token_view, name='csrf-token'),
]

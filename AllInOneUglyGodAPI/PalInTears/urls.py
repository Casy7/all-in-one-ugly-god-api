from django.urls import path
from .views import LocationDetailView, CharacterDetailView, ArmyDetailView

urlpatterns = [
    path('locations/', LocationDetailView.as_view(), name='locations-list'),
    path('locations/<int:pk>/', LocationDetailView.as_view(), name='locations-detail'),
    
    path('characters/', CharacterDetailView.as_view(), name='characters-list'),
    path('characters/<int:pk>/', CharacterDetailView.as_view(), name='characters-detail'),
    
    path('armies/', ArmyDetailView.as_view(), name='armies-list'),
    path('armies/<int:pk>/', ArmyDetailView.as_view(), name='armies-detail'),
]
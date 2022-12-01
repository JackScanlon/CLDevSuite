from django.urls import path, include
from .views import PhenotypeHomeView, CreatePhenotypeView

app_name = 'phenotypes'

urlpatterns = [
    path('', PhenotypeHomeView.as_view(), name='phenotypes'),
    path('create-phenotype', CreatePhenotypeView.as_view(), name='create_phenotype'),
]
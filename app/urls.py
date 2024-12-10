from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pdf-editor/', views.pdf_editor, name='pdf_editor'),
    path('merge/', views.merge, name='merge'),
    path('split/', views.split, name='split'),
    path('remove-password/', views.remove_password, name='remove_password'),
    path('rotate/', views.rotate, name='rotate'),
    path('survey/', views.survey, name='survey'),
    path('billing-planning/', views.billing_planning, name='billing_planning'),
    path('qa-qc/', views.qa_qc, name='qa_qc'),  # Ensure this is correctly defined
]
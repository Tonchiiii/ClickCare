from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='main-home'),
    path('checkup/', views.checkup, name='main-checkup'),
    path('pain_scale/', views.pain_scale, name='main-pain_scale'),
    path('neck_questionnaire/', views.neck_questionnaire, name='main-neck_questionnaire'),
    path('shoulder_questionnaire/', views.shoulder_questionnaire, name='main-shoulder_questionnaire'),
    path('results/', views.results, name='main-results'),
    path('back_results/', views.back_results, name='main-back_results'),
    path('elbow_questionnaire/', views.elbow_questionnaire, name='main-elbow_questionnaire'),
    path('back_questionnaire/', views.back_questionnaire, name='main-back_questionnaire'),
    path('wrist_questionnaire/', views.wrist_questionnaire, name='main-wrist_questionnaire'),
    path('hnf_questionnaire/', views.hnf_questionnaire, name='main-hnf_questionnaire'),
    
]

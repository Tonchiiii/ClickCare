from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='main-home'),
    path('home/', views.home, name='main-home'),
    path('index/', views.index, name='main-index'),
    path('MSDs/', views.MSDs, name='main-MSDs'),
    path('elbow/', views.elbow, name='main-elbow'),
    path('checkup/', views.checkup, name='main-checkup'),
    path('neck_questionnaire/', views.neck_questionnaire, name='main-neck_questionnaire'),
    path('shoulder_questionnaire/', views.shoulder_questionnaire, name='main-shoulder_questionnaire'),
    path('back_results/', views.back_results, name='main-back_results'),
    path('elbow_questionnaire/', views.elbow_questionnaire, name='main-elbow_questionnaire'),
    path('elbow_results/', views.elbow_results, name='main-elbow_results'),
    path('back_questionnaire/', views.back_questionnaire, name='main-back_questionnaire'),
    path('hipthigh_questionnaire/', views.hipthigh_questionnaire, name='main-hipthigh_questionnaire'),
    path('hipthigh_results/', views.hipthigh_results, name='main-hipthigh_results'),
    path('kneelowerleg_results/', views.kneelowerleg_results, name='main-kneelowerleg_results'),
    path('wristhand_questionnaire/', views.wristhand_questionnaire, name='main-wristhand_questionnaire'),
    path('wristhand_results/', views.wristhand_results, name='main-wristhand_results'),
]

from django.urls import path
from . import views

urlpatterns = [

    path('',views.home,name='home'),
    path('basic/',views.basic,name='basic'),
    path('basic/<int:resume_id>',views.basic,name='basic'),
    path('education/<int:resume_id>',views.education,name='education'),
    path('experiances/<int:resume_id>',views.experiances,name='experiances'),
    path('certificate/<int:resume_id>',views.certificate,name='certificate'),
    path('award/<int:resume_id>',views.award,name='award'),
    path('cv/<int:resume_id>',views.cv,name='cv'),
]
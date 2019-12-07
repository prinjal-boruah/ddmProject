from django.urls import include,path
from . import views
from . views import * #includes login, register
urlpatterns = [
    path('educationlist/', views.schoolCollegeView, name="educationlist"),
    
    path('api/schools', views.SchoolList.as_view()),
    path('api/schools/<int:pk>/', views.SchoolDetail.as_view()),
    path('api/colleges', views.CollegeList.as_view()),
    path('api/colleges/<int:pk>/', views.CollegeDetail.as_view()),
    
    path('api/login', login),
    path('api/register', Register),
]
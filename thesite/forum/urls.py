from django.urls import path 
from django.views.decorators.cache import cache_page
from .views import *

urlpatterns = [
    path('', ForumHome.as_view(), name='home'), #http://127.0.0.1:8000/
    path('about/', about, name='about'),
    path('adpage/', AddPage.as_view(), name='add_page'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', ForumCategory.as_view(), name='category')
    
] 

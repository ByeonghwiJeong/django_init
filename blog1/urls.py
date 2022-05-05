from . import views
from django.urls import path

app_name = 'blog1'
# URL Reverse에서 namespace역할 하게됨

urlpatterns = [
  path('', views.post_list),
]
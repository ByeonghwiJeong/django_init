from atexit import register
from django.urls import path, re_path, register_converter
from . import views
from .converters import YearConverter, MonthConverter, DayConverter


register_converter(YearConverter, 'year')
register_converter(MonthConverter, 'month')
register_converter(DayConverter, 'day')

app_name = 'instagram'
# URL Reverse에서 namespace역할 하게됨

urlpatterns = [
  path('new/', views.post_new, name='post_new'),
  path('<int:pk>/edit/', views.post_edit, name='post_edit'),

  path('', views.post_list, name='post_list'), 
  # views.post_list() XXXX주의
  path('<int:pk>/', views.post_detail, name='post_detail'),
  
  # path('2/', views.post_detail),
  # path('3/', views.post_detail),
  # re_path(r'(?P<pk>\d+)$', views.post_detail),
  # 위에것가 의미가 같음
  # pk 가 int나 문자열로 넘어오는가 차이

  # path('archives/<int:year>/', views.archives_year)
  # re_path(r'archives/(?P<year>20\d{2})/', views.archives_year)

  #register_converter
  # path('archives/<year:year>/', views.archives_year)
  path('archive/', views.post_archive, name='post_archive'),
  path('archive/<year:year>/', views.post_archive_year, name='post_archive_year'),
  # path('archive/<year:year>/<month:month>', views.post_archive_month, name='post_archive_month'),
  # path('archive/<year:year>/<month:month>/<day:day>', views.post_archive_day, name='post_archive_day'),
]
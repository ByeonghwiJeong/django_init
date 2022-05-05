from django.conf import settings
from django.db import models



class Profile(models.Model):
  user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
  address = models.CharField(max_length=100)
  zipcode = models.CharField(max_length=6)
  # validators = [] : 숫자의 형태로만 입력이 될수 있도록 할수있음
  # 유효성 검사 로직에 제한걸기

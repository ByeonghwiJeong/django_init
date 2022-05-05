from django.conf import settings
from django.db import models
from django.urls import reverse
from django.core.validators import MinLengthValidator
# from django.contrib.auth.models import User

class Post(models.Model):
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  message = models.TextField(
    validators = [MinLengthValidator(10)]
  )
  photo = models.ImageField(blank=True, upload_to = 'instagram/post/%Y/%m%d')
  tag_set = models.ManyToManyField('Tag', blank=True) 
  # Tag는 아래에있으므로 'Tag'문자열로 준다
  # Tag를 달지않을수도 있으므로 blank 옵션을 지정한다
  is_public = models.BooleanField(default=False, verbose_name="공개여부")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  #Java의 toString
  def __str__(self):
    # return f"Custom Post object ({self.id})"
    return self.message


  def get_absolute_url(self):
    return reverse('instagram:post_detail', args=[self.pk])    


  class Meta:
    ordering = ['-id']


# 아래항목 추가후 admin > list_display 에서 message_length 추가

  # def message_length(self):
  #   return len(self.message)

# message_length 컬럼 네이밍을 "메세지 글사수" 로 변경!! 

  # message_length.short_description = "메세지 글자수서

class Comment(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE, limit_choices_to={'is_public': False}) # CASCADE() xx
  # Post 를 문자열로 'Post'라고 사용할수도있고 현재앱이 instagram에 있으므로 그앱안에서 Post찾음
  # 'instagram.Post' 처럼 사용도 가능함
  # CASCADE : FK참조하는 모델의 Record도 삭제 - default값
  # post_id라는 필드가 생성됨
  # post = 에서 post는 가상의 필드 실제 DB필드와는 다름
  message = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  

class Tag(models.Model):
  name = models.CharField(max_length=50, unique=True)
  # Tag이름의 unique 보장
  # post_set = models.ManyToManyField(Post)
  # Post class에서 구현
  def __str__(self):
    return self.name
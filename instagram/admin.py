from django.contrib import admin
from .models import Post, Comment, Tag
from django.utils.safestring import mark_safe

# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  list_display = ['id', 'photo_tag', 'message','message_length', 'is_public', 'created_at', 'updated_at' ]
  # 첫번째 항목에 링크가 지정되어있어서 다른항목에 지정하려함
  list_display_links = ['message']
  # message column에 대한 검색 지원기능
  search_fields = ['message']

  list_filter = ['created_at', 'is_public']
  
# def message_length(self):
#   return len(self.message)
# models에서 정의한 위에 값을 아래와 같이 admin에서 표현할 수있음

  def photo_tag(self, post):
    if post.photo:
      return mark_safe(f'<img src="{post.photo.url}" style="width: 72px;" />')
    return None

  def message_length(self, post):
    return f"{len(post.message)} 글자"


@admin.register(Comment)
class CommetAdmin(admin.ModelAdmin):
  pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
  pass
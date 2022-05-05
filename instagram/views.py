from django.views.generic import ListView, DetailView, ArchiveIndexView
from django.views.generic.dates import YearArchiveView
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Post
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm
# (생성용)
def post_new(request):
  if request.method == 'POST':
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
      post = form.save()
      return redirect(post)
  else:
    form = PostForm()
    
  return render(request, 'instagram/post_form.html',{
    'form': form,
  })
# (수정용) 위랑 바뀌는것 많이없음
def post_edit(request, pk):
  post = get_object_or_404(Post, pk=pk)
  if request.method == 'POST':
    form = PostForm(request.POST, request.FILES, instance=post)
    if form.is_valid():
      post = form.save()
      return redirect(post)
  else:
    form = PostForm(instance=post)
    
  return render(request, 'instagram/post_form.html',{
    'form': form,
  })


# post_list = login_required(ListView.as_view(model=Post, paginate_by=10))

# @method_decorator(login_required, name='dispatch')
# class PostListView(ListView):
#   model = Post
#   paginate_by = 10

# post_list = PostListView.as_view()
# ==================================================

class PostListView(LoginRequiredMixin, ListView):
  model = Post
  paginate_by = 10

post_list = PostListView.as_view()



# post_list = ListView.as_view(model=Post)

# 클래스 기반뷰로 참조되는 post_list 3가지 맞추어줌
# @login_required
# def post_list(request):
#   qs = Post.objects.all()
#   q = request.GET.get('q', '') #q를 못가져올때는 ''빈문자열 get
#   if q:
#     qs = qs.filter(message__icontains=q)
#   # instagram/templates/instagram/post_list.html
#   # 위 경로에서 아래에 있는 'post_list':qs 의 post_list 참
#   return render(request, 'instagram/post_list.html', {
#     'post_list': qs,  # 마지막 ,
#     'q': q,
#   })

# pk 를 100으로 넘겨주면 does not exist error 발생
# def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
#   post = get_object_or_404(Post, pk=pk)

#   # try:
#   #   post = Post.objects.get(pk=pk)
#   # except Post.DoesNotExist:
#   #   raise Http404


#   return render(request, 'instagram/post_detail.html',{
#     'post':post,
#   })

# is_public이 True인 케이스만 보여주기
# post_detail = DetailView.as_view(
#   model=Post,
#   queryset=Post.objects.filter(is_public=True))

#인증되지 않은경우에는 is_public=True
class PostDetailView(DetailView):
  model = Post
  # queryset = Post.objects.filter(is_public=True)
  def get_queryset(self):
      qs = super().get_queryset()
      if not self.request.user.is_authenticated:
        qs = qs.filter(is_public=True)
      return qs

post_detail = PostDetailView.as_view()


# def archives_year(request, year):
#   return HttpResponse(f"{year}년 archives")

post_archive = ArchiveIndexView.as_view(model=Post, date_field='created_at', paginate_by=10)

post_archive_year = YearArchiveView.as_view(model=Post, date_field='created_at', make_object_list = True)
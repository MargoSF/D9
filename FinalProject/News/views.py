from email.headerregistry import Group
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import render
from django.utils.decorators import method_decorator
from datetime import datetime
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.views.generic.edit import CreateView
from django_filters.views import FilterView
from .forms import PostForm
from .models import Author, Category, Post
from .filters import PostFilter
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.http import HttpResponse
from django.contrib.auth import logout
from django.shortcuts import render, redirect, get_object_or_404


class PostsList(ListView):
    model = Post
    ordering = '-posting_time'
    template_name = 'posts.html'
    context_object_name = 'posts'


    def get_context_date(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_post'] = "Новые статьи в пятницу"
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        con = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        con['filterset'] = self.filterset
        return con


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'posts'

class SearchPosts(FilterView):
    model = Post
    filterset_name = 'search.html'
    paginate_by = 10
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context
    
class PostsCreate(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_types = Post.posts
        return super().form_valid(form)
            
class ArticlesCreate(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_types = Post.article
        return super().form_valid(form)

class PostEdit(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post_edit.html'

class ProtectedView(LoginRequiredMixin, TemplateView):
    template_name = 'prodected_page.html'

class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts')       

def index(request):
    return HttpResponse("Вы на главной странице приложения NewsPaper!")

class CategoryListView(ListView):
    model = Post
    template_name = 'category_list.html'
    context_object_name = 'category_news_list'

    def get_queryset(self):
        self.category = get_object_or_404(Category, id = self.kwargs['pk'])
        queryset = Post.objects.filter(category = self.category).order_by('-posting_time')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_subscriber'] = self.request.user not in self.category.subscribers.all()
        context['category'] = self.category
        return context


@login_required
def subscribe(request, pk):
    user =request.user
    category = Category.objects.get(id=pk)
    category.subscribers.add(user)
    message = 'Вы успешно подписались на рассылку новостей категории'
    return render(request, 'subscribe.html', {'category': category, 'message': message})
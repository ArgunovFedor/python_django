from django.shortcuts import render, redirect
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView

# Create your views here.
from app_blog.forms import BlogForm
from app_blog.models import Blog
from app_media.models import File


class BlogListView(ListView):
    permission_required = 'app_users.view_blog'
    template_name = 'blogs/blog_list.html'
    model = Blog
    context_object_name = 'blog_list'
    queryset = Blog.objects.all()


class BlogCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'app_users.create_blog'
    template_name = 'blogs/blog_create.html'
    model = Blog
    form_class = BlogForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        result = super().form_valid(form)
        pk = self.object.pk
        files = self.request.FILES.getlist('file_field')
        for file in files:
            instance = File(file=file, blog_id=pk)
            instance.save()
        return redirect(f'/blogs/{pk}/')


class BlogDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'app_users.view_news'
    template_name = 'blogs/blog_detail.html'
    model = Blog
    context_object_name = 'blog_detail'

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context['files_list'] = File.objects.filter(blog_id=pk)
        return context


class BlogUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'app_users.update_news'
    template_name = 'blogs/blog_update.html'
    model = Blog
    fields = ['name', 'description', 'files']

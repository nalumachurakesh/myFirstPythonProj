from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
# from django.utils import timezone

# Create your views here.
from .forms import BlogPostForm, BlogPostModelForm
from .models import BlogPost

# def blog_post_detail_page(request, slug):
#     # request -> Django -> response
#     # print("Django says", request.method, request.path, request.user)
#     querySet = BlogPost.objects.filter(slug = slug)
#     if querySet.count() == 0:
#         raise Http404

#     obj = querySet.first() # querySet.last() or querySet[0]
#     # obj = get_object_or_404(BlogPost, id = blog_id)
#     # try:
#     #     obj = BlogPost.objects.get(id = blog_id)
#     # except BlogPost.DoesNotExist:
#     #     raise Http404
#     # except ValueError:
#     #     raise Http404
#     template_name = 'blog_post_detail.html'
#     context = {"object" : obj}
#     return render(request, template_name, context)


# CRUD

# GET -> Retrieve / List
# POST -> CREATE / Update/ Delete
# Create Retrieve Update Delete

def blog_post_list_view(request):
    # List out objects
    # Could be search
    # now = timezone.now()
    # qs = BlogPost.objects.published()  # below line is same as this
    qs = BlogPost.objects.all().published()  # queryset => list of python object
    # qs = BlogPost.objects.filter(published_date__lte = now) # gte = greater than and equal to
    template_name = 'blog/list.html'
    context = {'object_list': qs}
    return render(request, template_name, context)


# def blog_post_create_view1(request):
#     # Create objects
#     # Use a form
#     form = BlogPostForm(request.POST or None)
#     if form.is_valid():
#         # print(form.cleaned_data)
#         # title = form.cleaned_data['title']
#         obj = BlogPost.objects.create(**form.cleaned_data)
#         form = BlogPostForm()
#     template_name = 'blog/form.html'
#     context = {'form': form}
#     return render(request, template_name, context)


# @login_required
@staff_member_required
def blog_post_create_view(request):
    # Create objects
    # Use a form
    # if not request.user.is_authenticated:
    #     return render(request, "not-a-user.html",{})
    form = BlogPostModelForm(request.POST or None)
    if form.is_valid():
        # below line can be used to save directly without modifications
        # form.save()

        # below way is used to modify the data before saving
        obj = form.save(commit=False)
        # obj.title = form.cleaned_data.get("title")+"0"
        obj.user = request.user
        obj.save()

        form = BlogPostModelForm()
    template_name = 'blog/form.html'
    context = {'form': form}
    return render(request, template_name, context)


def blog_post_detail_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/detail.html'
    context = {"object": obj}
    return render(request, template_name, context)


def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    form = BlogPostModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    template_name = 'form.html'
    context = { 'form': form, "title":f"Update {obj.title}"}
    return render(request, template_name, context)


def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/delete.html'
    if request.method == "POST":
        obj.delete()
        return redirect("/blog")
    context = {"object": obj}
    return render(request, template_name, context)

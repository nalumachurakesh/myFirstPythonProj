from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.

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


#CRUD

#GET -> Retrieve / List
#POST -> CREATE / Update/ Delete
#Create Retrieve Update Delete

def blog_post_list_view(request):
    #List out objects
    #Could be search
    qs = BlogPost.objects.all() # queryset => list of python object
    template_name = 'blog/list.html'
    context = {'object_list': qs}
    return render(request, template_name, context)

def blog_post_create_view(request):
    # Create objects
    # Use a form
    template_name = 'blog/create.html'
    context = {'form': None}
    return render(request, template_name, context)


def blog_post_detail_view(request, slug):
    obj = get_object_or_404(BlogPost, slug = slug)
    template_name = 'blog/detail.html'
    context = {"object" : obj} 
    return render(request, template_name, context)

def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug = slug)
    template_name = 'blog/detail.html'
    context = {"object" : obj, 'form': None} 
    return render(request, template_name, context)

def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug = slug)
    template_name = 'blog/delete.html'
    context = {"object" : obj} 
    return render(request, template_name, context)
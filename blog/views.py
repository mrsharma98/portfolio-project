from django.shortcuts import render, get_object_or_404

from .models import Blog

def allblogs(request):
    blogs = Blog.objects
    return render(request, 'blog/allblogs.html', {'blogs':blogs})


def detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    # get_object_or404(name_of_the_model,
    #                    pk=the_primary_key_of_that_particular_blog)
    # pk = primary key
    # and blog_id : primary key of our particular blog

    print(detailblog)

    return render(request, 'blog/detail.html', {'blog':detailblog})

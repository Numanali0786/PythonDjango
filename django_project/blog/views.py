from django.shortcuts import render

posts = [
    {
        'author' : 'numan',
        'title' : 'post 1',
        'content' : 'content 1',
        'date_posted' : 'august 1'
    },

    {
        'author' : 'ali',
        'title' : 'post 2',
        'content' : 'content 2',
        'date_posted' : 'august 2'
    }
]

def home(request):
   
    context = {
        'posts' : posts
    }


    return render(request ,'blog/home.html', context)


def about(request):
   
    return render(request ,'blog/about.html', {'title' : 'about'})

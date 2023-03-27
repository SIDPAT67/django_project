from django.shortcuts import render

posts = [
    {
        'author': 'Sid',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': '15 March 2023'
    },
    {
        'author': 'Cat',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': '16 March 2023'
    }
]



def home(request):
    context = {
        'posts': posts
        }
    return render(request, 'blog/home.html', context)
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

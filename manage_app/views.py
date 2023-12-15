from django.shortcuts import render
from . models import MovieInfo

from . forms import MovieForm
# Create your views here.


def base(request):
    return render(request,'base.html')

def create(request):
    #frm=MovieForm
    if request.POST:
        frm = MovieForm(request.POST)
        if frm.is_valid():
            frm.save()
    else:
        frm = MovieForm()

    ''' we changed this as post in above 
        title = request.POST.get('title')
        year = request.POST.get('year')
        summary = request.POST.get('summary')
        movie_obj = MovieInfo(title=title,year=year,summary=summary)
        movie_obj.save()'''

    return render(request,'create.html',{'frm': frm})


def list(request):

    movie_data= MovieInfo.objects.all()
    print(movie_data)
    return render(request,'list.html',{'movies' :movie_data}) #here we give the key as specified in for loop so can store as dictionary.

def edit(request,pk):
    instance_to_edit = MovieInfo.objects.get(pk=pk)
    if request.POST:
       frm = MovieForm(request.POST,instance=instance_to_edit)
       if frm.is_valid():
           instance_to_edit.save()


       ''' title = request.POST.get('title')
        year = request.POST.get('year')
        summary = request.POST.get('summary')
        instance_to_edit.title=title
        instance_to_edit.year=year
        instance_to_edit.summary=summary
        instance_to_edit.save()'''

    else:

        frm=MovieForm(instance=instance_to_edit)
    return render(request,'create.html',{'frm': frm})


def delete(request,pk):
    instance = MovieInfo.objects.get(pk=pk)
    instance.delete()
    movie_data= MovieInfo.objects.all()
    return render(request,'list.html',{'movies' :movie_data}) 


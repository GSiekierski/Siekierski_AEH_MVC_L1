from django.shortcuts import render, redirect, get_object_or_404
from .form import MovieForm
from .models import Movie

def movie_list(request):
    movies= Movie.objects.all()
    return render(request,'movies/movie_list.html', {'movies': movies})

def movie_add(request):
    if request.method=="POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form=MovieForm()
    return render(request, 'movies/movie_form.html', {'form': form})

def movie_edit(request, pk):
    movie=get_object_or_404(Movie, pk=pk)
    if request.method=='POST':
        form=MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form=MovieForm(instance=movie)
    return render(request,'movies/movie_form.html',{'form': form, 'edit': True})

def movie_delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('movie_list')
    return render(request, 'movies/movie_confirm_delete.html', {'movie': movie})
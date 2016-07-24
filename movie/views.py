from django.shortcuts import render, get_object_or_404

from .models import Entry, Genre, Archive, Season, Episode, Type
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    context = {
        'ratings': Entry.objects.all().order_by('-rate_date')[:20]
    }
    return render(request, 'home.html', context)


def explore(request):
    entries = Entry.objects.all().order_by('-rate_date', '-inserted_date')
    paginator = Paginator(entries, 50)
    page = request.GET.get('page')
    try:
        ratings = paginator.page(page)
    except PageNotAnInteger:
        ratings = paginator.page(1)
    except EmptyPage:
        ratings = paginator.page(paginator.num_pages)
    context = {
        'ratings': ratings,
        'archive': Archive.objects.all(),
    }
    return render(request, 'entry.html', context)


def book(request):
    return render(request, 'book.html')


def about(request):
    return render(request, 'about.html', {'archive': Archive.objects.all()})


def entry_details(request, const):
    # MyModel.objects.extra(select={'length':'Length(name)'}).order_by('length')
    def get_seasons(imdb_id):
        entry = Entry.objects.get(const=imdb_id)
        seasons = Season.objects.filter(entry=entry)
        season_episodes = []
        for s in seasons:
            episodes = Episode.objects.filter(season=s)
            season_episodes.append([s.number, episodes])
        return season_episodes

    context = {
        'entry': get_object_or_404(Entry, const=const),
        'archive': Archive.objects.filter(const=const).order_by('-rate_date'),
    }
    if context['entry'].type.name == 'series':
        context['episodes'] = get_seasons(const)

    return render(request, 'entry_details.html', context)


def entry_groupby_year(request):
    year_counter = []
    for y in Entry.objects.order_by('-year').values('year').distinct():
        year_counter.append((y['year'], Entry.objects.filter(year=y['year']).count()))
    context = {
        'year_counter': year_counter,
        'counter': len(year_counter),
        'max': max(year_counter, key=lambda x: x[0])[0],
        'min': min(year_counter, key=lambda x: x[0])[0],
    }
    context['diff'] = int(context['max']) - int(context['min'])
    return render(request, 'entry_groupby_year.html', context)


def entry_show_from_year(request, year):
    context = {
        'year': Entry.objects.order_by('-rate').filter(year=year),
        'counter': Entry.objects.order_by().filter(year=year).count(),
        'what_year': year,
    }
    return render(request, 'entry_show_from_year.html', context)


def entry_groupby_genre(request):
    context = {
        'genre': Genre.objects.all(),
        'counter': Genre.objects.all().count()
    }
    return render(request, 'entry_groupby_genre.html', context)


def entry_show_from_genre(request, genre):
    context = {
        'genre': Genre.objects.get(name=genre).entry_set.all(),
        'counter': Genre.objects.get(name=genre).entry_set.all().count(),
        'genre_name': genre,
    }
    return render(request, 'entry_show_from_genre.html', context)
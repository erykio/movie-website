import django
import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()
from django.db.models import Q, Subquery, OuterRef

import pytz
from django.contrib.auth import get_user_model
from importer.utils import import_ratings_from_csv

from accounts.models import *
import sys
user = User.objects.all().first()
from django.utils.timezone import now

from mysite.settings import MEDIA_ROOT
from api.mixins import GetTitleMixin, GetUserMixin
from lists.models import Favourite

User = get_user_model()
collection_id = 119

from titles.tmdb_api import TmdbWrapper, PopularMoviesTmdbTask, TitleUpdater, MovieTmdb, TmdbResponseMixin, \
    PopularPeopleTmdbTask, \
    NowPlayingMoviesTmdbTask, UpcomingMoviesTmdbTask, PopularTVTmdbTask, TmdbTaskRunner

from titles.models import Title, Person, Collection, Upcoming, Popular, NowPlaying, CurrentlyWatchingTV, CastTitle, \
    CrewTitle

# Season, Person, CrewTitle, Popular, Title, Keyword, Genre, CastTitle, Collection, NowPlaying, Upcoming = [
#     apps.get_model('titles.' + model_name) for model_name in
#     [
#         'Season', 'Person', 'CrewTitle', 'Popular', 'Title', 'Keyword', 'Genre', 'CastTitle', 'Collection', 'NowPlaying', 'Upcoming'
#     ]
# ]
# print(Keyword.objects.all().count())
# c = Collection.objects.get(id=119)
# print(c)
# print(c.titles.all())
# t = c.titles.all()[0]
# print(t.collection.all())

title_in_collection = 'tt0120737'
xfiles = 'tt0106179'
tbbt = 'tt0898266'
# Title.objects.filter(imdb_id=title_in_collection).delete()
# TmdbWrapper().get(title_in_collection, call_updater=True)
# person, created = Person.objects.update_or_create(pk=1000,
#     defaults={'name': 'testo tsetst', 'image_path': ''}
# )
# person2, created2 = Person.objects.update_or_create(pk=1001,
#     defaults={'name': 'testo tsetst', 'image_path': ''}
# )
# Title.objects.filter(imdb_id=xfiles).delete()
# TmdbWrapper().get(xfiles, call_updater=True)

def database_is_clean():
    title_in_collection = 'tt0120737'
    TmdbWrapper().get(title_in_collection, call_updater=True)
    PopularMoviesTmdbTask().get()
    User.objects.create_user(username='test', password='123')
    User.objects.create_user(username='test2', password='123')
# database_is_clean()

# print(Person.objects.get(pk=17051).name)
# print(Person.objects.get(pk=17051).slug)
# for p in Person.objects.all():
#     if not p.slug:
#         print(p.name)
#         print(p.slug)
# print(Title.objects.all().count())

def clean_models():
    Upcoming.objects.all().delete()
    Popular.objects.all().delete()
    NowPlaying.objects.all().delete()


def create_rating_duplicat():
    r = Rating.objects.filter(user__username='test', title__name__icontains='jedi').last()
    print(r)
    r.rate = 2
    # r.pk = None
    # r.rate_date = now().today()
    r.save()
    # print(Rating.objects.filter(user__username='test', title__name__icontains='jedi'))


def restart_favs():
    user = User.objects.get(username='test')
    Favourite.objects.filter(user=user).delete()
    t = ['It', 'Thor: Ragnarok', 'Justice League']
    for i, x in enumerate(t, 1):
        Favourite.objects.create(user=user, title=Title.objects.get(name=x), order=i)

    print(Favourite.objects.filter(user=user))

# restart_favs()

# create_rating_duplicat()
# t = GetTitleMixin()
# u = GetUserMixin()
# t.url_kwarg = 'user_pk'
# print(t.model)
# print(t.model_name)
# print(t.model_instance_name)
# print(t.instance)
# print(t.title)

# c = CurrentlyWatchingTV.objects.all()
# print(c.delete())
# print(Title.objects.all().first().pk)

# p = Person.objects.all().first()
# user = User.objects.get(username__icontains='test2')
# print(user)
# c = CastTitle.objects.filter(person=p)
# newest_user = Rating.objects.filter(user=user, title=OuterRef('title')).order_by('-rate_date')

# qs = qs.annotate(request_user_rate=Subquery(newest_user.values('rate')[:1]))

# print(c)
# c = c.annotate(
#     request_user_rate=Subquery(newest_user.values('rate')[:1])
# )
#
# for x in c:
#     print(x.request_user_rate, x)

def add_crew_to_person():
    p = Person.objects.get(pk=17051)
    print(p)
    CrewTitle.objects.create(title=Title.objects.all().first(), person=p)


def test_queryset():
    r = Rating.objects.filter(user__username='test')
    r = Rating.objects.filter(user__username='test').values('title')
    print(r)
    print(Title.objects.filter(rating__user__username='test').distinct().filter(pk__in=[4773]))


def test_csv():
    user = User.objects.get(username='test')
    import_ratings_from_csv(user, 'G:/code/PycharmProjects/movie website/media/accounts/ratings december 2017 — kopia (2).csv')
    # update_user_ratings_csv(user, 'G:/code/PycharmProjects/movie website/media/accounts/imdb.csv')

print(Title.objects.all().first().pk)
# test_queryset()
# test_csv()
# add_crew_to_person()



# query = Title.objects.filter(
#     Q(casttitle__person=p) | Q(crewtitle__person=p)
# ).order_by('-release_date')
# print(p)
# print(query)

# Title - Subquery(Rating)
# Person - Subquery(Rating)

# query = Rating.objects.filter(
#     Q(casttitle__person=OuterRef('pk')) | Q(crewtitle__person=OuterRef('pk'))
# ).order_by('-release_date')
# qs = Person.objects.all().annotate(
#     test=Subquery(query.values('pk')[:1])
# )
# print(qs)
# for q in qs:
#     print(q)

# Title.objects.all().delete()
# clean_models()

# def get_daily():
    # print('1')
    # PopularPeopleTmdbTask().get()
    # print('2')
    # PopularMoviesTmdbTask().get()
    # print('3')
    # NowPlayingMoviesTmdbTask().get()
    # print('4')
    # UpcomingMoviesTmdbTask().get()
    # print('5')
    # PopularTVTmdbTask().get()

# print(TmdbResponseMixin().source_file_path)
# get_daily()
# t = Title.objects.filter(imdb_id=tbbt).delete()
# print(t)
# print(Title.objects.filter(release_date).values('release_date__year').order_by('-release_date__year'))
# TmdbTaskRunner().run()

#
# TmdbWrapper().get(tbbt)
# Title.objects.get(tmdb_id=7859).similar.all().count()

# from titles.tasks import task_update_title
# t = Title.objects.get(imdb_id='tt4587656')
# task_update_title.delay(t.pk)
#
# # print(t.similar.all())
# print('updated', t.updated, 'being_updated', t.being_updated)


def get_person(value):
    person, created = Person.objects.update_or_create(
        pk=value['id'], defaults={'name': value['name'], 'image_path': value['profile_path'] or ''}
    )
    return person


# UserFollow.objects.all().delete()

# u = UserFollow.objects.all().first()
# u2 = UserFollow(follower=u.follower, followed=u.followed, pk=0)
# UserFollow.objects.all().delete()
# u2.save()
# print(UserFollow.objects.all().values_list('pk'))

# for t in Title.objects.all():
#     print(t.overview)

# def random_date():
#     start = datetime(2010, 1, 1, tzinfo=pytz.utc)
#     end = datetime.now(tz=pytz.utc)
#     return start + timedelta(seconds=random.randint(0, int((end - start).total_seconds())))
#
#
# def get_random_title():
#     idtitle = random.randint(1, Title.objects.count())
#     return Title.objects.filter(id=idtitle).first()
#
#
# def get_random_rated_title(user):
#     titles = Title.objects.filter(rating__user=user).values_list('const', flat=True).distinct()
#     return Title.objects.get(const=random.choice(titles))
#
#
# def get_random_recommended_title(user):
#     titles = Title.objects.filter(watchlist__user=user).values_list('const', flat=True).distinct()
#     return Title.objects.get(const=random.choice(titles))
#
# def get_random_user(user):
#     us = User.objects.exclude(username=user.username).values_list('id', flat=True)
#     return User.objects.get(id=random.choice(us))


# for i in range(15):
#     # better nicknames?
#     username = 'dummy' + str(i)
#     password = '123123'
#     user, created = User.objects.get_or_create(username=username)
#     user.set_password(password)
#     user.save()
#
#     if not Rating.objects.filter(user=user).exists():
#         r = random.randint(0, random.randint(1, 1000))
#         r2 = random.randint(0, random.randint(1, 120))
#         r3 = random.randint(0, random.randint(1, 200))
#         r4 = random.randint(0, random.randint(1, 200))
#         r5 = random.randint(0, random.randint(1, 10))
#
#         for j in range(r):
#             rate = random.randint(1, 10)
#             title = get_random_title()
#             if title:
#                 d = random_date()
#                 if not Rating.objects.filter(user=user, title=title, rate_date=d).exists():
#                     Rating.objects.get_or_create(user=user, title=title, rate=rate, rate_date=d)
#
#         for j in range(r2):
#             title = get_random_title()
#             if title:
#                 d = random_date()
#                 if not Favourite.objects.filter(user=user, title=title).exists():
#                     Favourite.objects.get_or_create(user=user, title=title, added_date=d)
#
#         for j in range(r3):
#             title = get_random_title()
#             if title:
#                 d = random_date()
#                 if not Watchlist.objects.filter(user=user, title=title).exists():
#                     Watchlist.objects.get_or_create(user=user, title=title, added_date=d)
#
#         for j in range(r4):
#             title = get_random_rated_title(user)
#             if title:
#                 d = random_date()
#                 rate = random.randint(1, 10)
#                 if not Rating.objects.filter(user=user, title=title, rate_date=d).exists():
#                     Rating.objects.get_or_create(user=user, title=title, rate=rate, rate_date=d)
#
#         for j in range(r5):
#             u = get_random_user(user)
#             UserFollow.objects.get_or_create(user_follower=user, user_followed=u)
#         # recommend titles to followed (they should not be unrecommended when the user is deleted)
#
#     # else:
#     #     Rating.objects.filter(user=user).delete()


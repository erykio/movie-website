import django, os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()
from django.db.models import Count, CharField, Value, ForeignKey, Avg, Expression, Case, When, IntegerField
from django.contrib.auth.models import User
import re, pytz
from datetime import datetime
from django.utils import timezone
from users.models import *
from recommend.models import *
from django.shortcuts import redirect
user = User.objects.all().first()
print(user.username)
print(user.userprofile)

# titles = Title.objects.extra(select={
#     'seen_by_user': """SELECT rating.rate FROM movie_rating as rating
#         WHERE rating.title_id = movie_title.id AND rating.user_id = %s LIMIT 1""",
#     'has_in_watchlist': """SELECT 1 FROM movie_watchlist as watchlist
#         WHERE watchlist.title_id = movie_title.id AND watchlist.user_id = %s AND watchlist.deleted = false""",
#     'has_in_favourites': """SELECT 1 FROM movie_favourite as favourite
#         WHERE favourite.title_id = movie_title.id AND favourite.user_id = %s"""
# }, select_params=[1] * 3)

# titles = Rating.objects.extra(select={
#     'seen_by_user': """SELECT rate FROM auth_user, movie_title
#         WHERE auth_user.id = user_id = %s AND movie_title.slug = %s LIMIT 1""",
# }, select_params=[1, 'inferno-2016'])

followed = User.objects.extra(select={
    'seen_by_user': """
        SELECT
            rating.rate
        FROM
            movie_rating as rating,
            movie_title as title
        WHERE
            rating.title_id = title.id
        AND
            rating.user_id = auth_user.id
        AND
            title.slug = 'inferno-2016'
        LIMIT 1""",
    }
)
for f in followed:
    print(f, f.seen_by_user)
# ratings = Rating.objects.raw('SELECT *')
# raw will get me user object?
# print(titles.query)
# print(titles)
# print(titles.first().seen_by_user)
# print(redirect(user.userprofile.watchlist_url()))
#
# profile = UserProfile.objects.get(user__username='test')
# print(profile.user.username)
#
# genres = Genre.objects.annotate(num=Count('title')).order_by('-num')
# for g in genres:
#     print(g.name, g.num)
#
#
# x = User.objects.filter(rating__title__slug='inferno-2016').distinct()
# print(x)
# x = Rating.objects.filter(title__slug='inferno-2016')
# print(x)
# a = Title.objects.filter(rating__user__id=1).annotate(seen_by_user=Count('rating__user__id'))
# print(a.first().seen_by_user)
# print(a)

# a = Title.objects.annotate(
#     seen_by_user=Count(
#         Case(When(rating__user__id=1, then=1), output_field=IntegerField())
#     ),
#     has_in_watchlist=Count(
#         Case(When(watchlist__user__id=1, then=1), output_field=IntegerField())
#     ),
#     has_in_favourites=Count(
#         Case(When(favourite__user__id=1, then=1), output_field=IntegerField())
#     ),
# )


from django.db.models.expressions import F
from django.db.models.aggregates import Max

# Chapters.objects.annotate(last_chapter_pk=Max('novel__chapter__pk')
#             ).filter(pk=F('last_chapter_pk'))
# def average_rating_of_title(title):
#     # avg_all_ratings = title.rating_set.values('rate').aggregate(avg=Avg('rate'))
#     sum_rate = 0
#     ids_of_users = title.rating_set.values_list('user', flat=True).order_by('user').distinct()
#     title_ratings = Rating.objects.filter(title=title)
#     for user_id in ids_of_users:
#         latest_rating = title_ratings.filter(user__id=user_id).first()
#         sum_rate += latest_rating.rate
#     if sum_rate:
#         avg_rate = round(sum_rate / len(ids_of_users), 1)
#         return '{} ({} users)'.format(avg_rate, len(ids_of_users))
#     return None

# x = Rating.objects.filter(title__slug='inferno-2016').annotate(current_rating=Max('rate_date'))
# for rat in x:
#     print(rat, rat.current_rating)
#
# latest_ratings_of_users = User.objects.filter(rating__title__slug='inferno-2016').annotate(current_rating=Max('rating__rate_date'), rate=F('rating__rate'))#.aggregate(a=Avg('rating__rate'))
# latest_ratings_of_users = User.objects.filter(rating__title__slug='inferno-2016').annotate(current_rating=Max('rating__rate_date')).values('rating__rate')#.aggregate(a=Avg('rating__rate'))
# # can get users/dates and manually get AVG. maybe its still better
# # av = latest_ratings_of_users.values('current_rating').aggregate(a=Avg('current_rating'))
# for rat in latest_ratings_of_users:
#     print(rat)
#
# # print(a.query)
# # print(a.first().seen_by_user)
# # for t in a:
# #     print(t.seen_by_user, t.has_in_watchlist, t.has_in_favourites, t.name)
# #
#
#
# a = Rating.objects.filter(user=user, title__slug='inferno-2016').first()
# print(a)
#
# x = Rating.objects.filter(title__slug='inferno-2016').order_by('user', '-rate_date').distinct('user').values_list('rate', flat=True)
# for a in x:
#     print(a)

# print(x.aggregate(av=Avg('rate')))

# titles = Title.objects.extra(select={
#     'seen_by_user': """SELECT rating.rate FROM movie_rating as rating
#         WHERE rating.title_id = movie_title.id AND rating.user_id = %s LIMIT 1""",
#     'has_in_watchlist': """SELECT 1 FROM movie_watchlist as watchlist
#         WHERE watchlist.title_id = movie_title.id AND watchlist.user_id = %s AND watchlist.deleted = false""",
#     'has_in_favourites': """SELECT 1 FROM movie_favourite as favourite
#         WHERE favourite.title_id = movie_title.id AND favourite.user_id = %s"""
# }, select_params=[1] * 3)


# users = User.objects.filter().extra(select={
#     'seen_by_user': """SELECT rating.rate FROM movie_rating as rating
#         WHERE rating.title_id = movie_title.id AND rating.user_id = %s LIMIT 1""",
#     'has_in_watchlist': """SELECT 1 FROM movie_watchlist as watchlist
#         WHERE watchlist.title_id = movie_title.id AND watchlist.user_id = %s AND watchlist.deleted = false""",
#     'has_in_favourites': """SELECT 1 FROM movie_favourite as favourite
#         WHERE favourite.title_id = movie_title.id AND favourite.user_id = %s"""
# }, select_params=[1] * 3)
# titles = Title.objects.annotate(
#     seen_by_user=Count(
#         Case(When(rating__user=request.user, then=1), output_field=IntegerField())
#     ),
#     has_in_watchlist=Count(
#         Case(When(watchlist__user=request.user, then=1), output_field=IntegerField())
#     ),
#     has_in_favourites=Count(
#         Case(When(favourite__user=request.user, then=1), output_field=IntegerField())
#     ),
# )
# users = UserFollow.objects.filter(user_follower=user).annotate(
#     seen_by_followed=Count(
#         Case(When(user_follower=))
#     )
# )

# title = Title.objects.get(name='Sleeping with Other People').id
# users = UserFollow.objects.filter(user_follower=user).extra(select={
#     'seen_by_followed': """SELECT rate from movie_rating as rating, movie_title as title
#         WHERE rating.title_id = title.id AND title.id = %s AND rating.user_id = users_userfollow.user_followed_id
#         ORDER BY rating.rate_date DESC LIMIT 1""",
#     'has_in_recommend': """SELECT 1 from recommend_recommendation as recommend, movie_title as title
#         WHERE recommend.title_id = title.id AND title.id = %s AND recommend.user_id = users_userfollow.user_followed_id""", # 1 max so no need for limit
# }, select_params=[title] * 2)
# for u in users:
#     print(u.user_followed, u.seen_by_followed, u.has_in_recommend)
#
# for u in users.values('user_followed', 'seen_by_followed'):
#     print(u)
#
# title = Title.objects.filter().first()
# print(title.get_absolute_url())
title = Title.objects.get(name='Inferno')
# r = Rating.objects.filter(title=title, user=user)
# current = r.first()
# last = r.last()
# print(current.rate_date, current.rate)
# print(last.rate_date, last.rate)
# def next_rating_days_diff(r):
#     next_rating = Rating.objects.filter(user=user, title=title, rate_date__gt=r.rate_date).last()
#     if next_rating:
#         return (next_rating.rate_date - r.rate_date).days
#     return (datetime.now().date() - r.rate_date).days
#
# def next(r):
#     previous = Rating.objects.filter(user=user, title=title, rate_date__lt=r.rate_date).first()
#     if previous:
#         return (r.rate - previous.rate, (r.rate_date - previous.rate_date).days)
#     return None
#         # return (previous.rate_date - r.rate_date).days
#     # return (datetime.now().date() - r.rate_date).days
#
# # print(next_rating_days_diff(current))
# # print(next_rating_days_diff(last))
# print(next(current))
# print(next(last))
#
# a = Recommendation.objects.filter(user=user).last()
# print(a.user, a.title)
# a = a.added_date
# print(a)

from django.template.defaultfilters import slugify

def create_slug(title, new_slug=None):
    # recursive function to get unique slug (in case of 2 titles with the same name/year)
    slug = slugify('{} {}'.format(title.name, title.year))[:70] if new_slug is None else new_slug
    if Title.objects.filter(slug=slug).exists():
        slug += 'i'
        create_slug(title, slug)
    return slug
print(create_slug(title))

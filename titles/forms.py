import re

from django import forms
from django.contrib.auth import get_user_model
from django.db.models import Q, Count

from shared.widgets import MySelectMultipleWidget
from titles.constants import TITLE_TYPE_CHOICES
from titles.models import Title, Genre, Rating
from shared.forms import SearchFormMixin


User = get_user_model()


class TitleSearchForm(SearchFormMixin, forms.Form):
    year = forms.IntegerField(required=False)
    user = forms.ModelChoiceField(queryset=User.objects.all(), required=False)
    keyword = forms.CharField(max_length=100, required=False, label='Keywords')
    genre = forms.ModelMultipleChoiceField(queryset=Genre.objects.annotate(count=Count('title')).order_by('-count'), required=False)
    type = forms.ChoiceField(choices=TITLE_TYPE_CHOICES, required=False)

    @staticmethod
    def search_keyword(value):
        if len(value) > 2:
            return Q(name__icontains=value)
        return Q(name__istartswith=value)

    @staticmethod
    def search_genre(value):
        return Q(genres__in=value)

    @staticmethod
    def search_year(value):
        return Q(release_date__year=value)

    @staticmethod
    def search_type(value):
        return Q(type=value)

    @staticmethod
    def search_user(value):
        return Q(rating__user=value)


class RateUpdateForm(forms.ModelForm):

    class Meta:
        model = Rating
        fields = ('rate_date', 'rate')

    # if searched_user:
    #     if exclude_his and req_user_id:
    #         titles = titles.filter(rating__user=request.user).exclude(rating__user=searched_user)
    #         search_result.append('Seen by you and not by {}'.format(searched_user.username))
    #     elif exclude_mine and req_user_id and req_user_id != searched_user.id:
    #         want_req_user_rate = False
    #
    #         titles = titles.filter(rating__user=searched_user).distinct().extra(select={
    #             'user_curr_rating': select_current_rating,
    #         }, select_params=[searched_user.id])
    #         titles = titles.exclude(rating__user=req_user_id)
    #         search_result.append('Seen by {} and not by me'.format(searched_user.username))
    #     elif common and req_user_id and not is_owner:
    #         titles = titles.filter(rating__user=searched_user).filter(rating__user=request.user).distinct().extra(select={
    #             'user_curr_rating': select_current_rating,
    #         }, select_params=[searched_user.id])
    #         search_result.append('Seen by you and {}'.format(searched_user.username))
    #     elif rating:
    #         titles = titles.filter(rating__user=searched_user).annotate(max_date=Max('rating__rate_date'))\
    #             .filter(rating__rate_date=F('max_date'), rating__rate=rating) \
    #             .extra(select={
    #                 'user_curr_rating': select_current_rating,
    #             }, select_params=[searched_user.id])
    #         search_result.append('Titles {} rated {}'.format(searched_user.username, rating))
    #     elif show_all_ratings:
    #         titles = Title.objects.filter(rating__user__username=searched_user.username) \
    #             .order_by('-rating__rate_date', '-rating__inserted_date')
    #         search_result.append('Seen by {}'.format(searched_user.username))
    #         search_result.append('Showing all ratings (duplicated titles)')
    #     elif not is_owner:
    #         titles = titles.filter(rating__user=searched_user).distinct().extra(select={
    #             'user_curr_rating': select_current_rating,
    #         }, select_params=[searched_user.id])
    #         search_result.append('Seen by {}'.format(searched_user.username))
    #     else:
    #         titles = titles.filter(rating__user=searched_user).order_by('-rating__rate_date')
    #         search_result.append('Seen by {}'.format(searched_user.username))
    # elif rating and req_user_id:
    #     titles = titles.filter(rating__user=request.user)\
    #         .annotate(max_date=Max('rating__rate_date'))\
    #         .filter(rating__rate_date=F('max_date'), rating__rate=rating)
    #     search_result.append('Titles you rated {}'.format(rating))
    #
    # if rate_date_year and (username or req_user_id):
    #     if rate_date_year and rate_date_month:
    #         # here must be authenticated
    #         what_user_for = searched_user or request.user
    #         titles = titles.filter(rating__user=what_user_for, rating__rate_date__year=rate_date_year,
    #                                rating__rate_date__month=rate_date_month)
    #         search_result.append('Seen in {} {}'.format(calendar.month_name[int(rate_date_month)], rate_date_year))
    #     elif rate_date_year:
    #         if username:
    #             titles = titles.filter(rating__user__username=username, rating__rate_date__year=rate_date_year)
    #         elif request.user.is_authenticated():
    #             titles = titles.filter(rating__user=request.user, rating__rate_date__year=rate_date_year)
    #         search_result.append('Seen in ' + rate_date_year)
    #
    # titles = titles.prefetch_related('director', 'genre')  # .distinct()
    # if request.user.is_authenticated() and want_req_user_rate:
    #     titles = titles.extra(select={
    #         'req_user_curr_rating': select_current_rating,
    #     }, select_params=[request.user.id])




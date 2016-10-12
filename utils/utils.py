from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from urllib.parse import urlencode
import datetime
from django.core.mail import send_mail
from django.db.models import Q

from mysite.settings import EMAIL_DEST, EMAIL_HOST_USER


def build_url(url, **kwargs):
    get = kwargs.pop('get', {})
    url += '?' + urlencode(get)
    return url


# def build_datetime_obj(obj):
#     if isinstance(obj, datetime.date):
#         return datetime.datetime(obj.year, obj.month, obj.day)
#     return None


def paginate(query_set, page, page_size=50):
    paginator = Paginator(query_set, page_size)
    try:
        ratings = paginator.page(page)
    except PageNotAnInteger:
        ratings = paginator.page(1)
    except EmptyPage:
        ratings = paginator.page(paginator.num_pages)
    return ratings


def send_email(subject, message):
    send_mail(
        subject,
        message,
        EMAIL_HOST_USER,
        [EMAIL_DEST],
        fail_silently=False,
        html_message=message,
    )


def email_watchlist():
    from movie.models import Watchlist
    delete = Watchlist.objects.to_delete()
    message = """
                <table class="table table-hover table-bordered table-condensed">
                <thead>
                    <tr>
                        <th class="text-center">title</th>
                    </tr>
                </thead>
                <tbody>
    """
    message += '\n'.join(['<tr><td><a href="http://www.imdb.com/title/{1}/">{0}</a></td></tr>'.format(
        obj.name, obj.const) for obj in delete])
    message += '</tbody></table>'
    print(message)
    send_email(subject='[imdb watchlist]', message=message)
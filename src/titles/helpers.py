from django.conf import settings
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.db.models import Subquery, IntegerField


def tmdb_image(func):
    """
    Decorator around property. Usage:
    @property
    @tmdb_image
    def poster_backdrop_user(self):
        return IMAGE_SIZES['backdrop_user']
    Property returns what kind of image it is. This decorator will return full TMDB hotlink.
    During development or when object has no image_path it returns static placeholder image to save traffic
    by simply returning a property 'self.poster_backdrop_user_placeholder'
    """

    def func_wrapper(self):
        # if self.image_path:
            # return f'https://image.tmdb.org/t/p/{func(self)}{self.image_path}'

        return getattr(self, f'{func.__name__}_placeholder')

    return func_wrapper


def static_poster(func):

    def func_wrapper(self):
        return static(f'img/posters/{func(self)}.png')

    return func_wrapper


def instance_required(func):
    """
    Decorator for APIView's post handler.
    class AddRatingAPIView(IsAuthenticatedMixin, GetTitleMixin, APIView):
        @instance_required
        def post(self, request, *args, **kwargs):
    APIView inherits GetTitleMixin so it will set self.title or return that `Ttle does not exist`
    """

    def func_wrapper(self, request, *args, **kwargs):
        message = self.set_instance(**kwargs)
        if message:
            return message

        return func(self, request, *args, **kwargs)

    return func_wrapper


class SubqueryCount(Subquery):
    """https://stackoverflow.com/a/47371514"""
    template = "(SELECT count(*) FROM (%(subquery)s) _count)"
    output_field = IntegerField()

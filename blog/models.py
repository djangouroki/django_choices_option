import datetime

from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class Post(models.Model):

    class MoonLandings(datetime.date, models.Choices):
        APOLLO_11 = 1969, 7, 20, 'Apollo 11 (Eagle)'
        APOLLO_12 = 1969, 11, 19, 'Apollo 12 (Intrepid)'
        APOLLO_14 = 1971, 2, 5, 'Apollo 14 (Antares)'
        APOLLO_15 = 1971, 7, 30, 'Apollo 15 (Falcon)'
        APOLLO_16 = 1972, 4, 21, 'Apollo 16 (Orion)'
        APOLLO_17 = 1972, 12, 11, 'Apollo 17 (Challenger)'

    apolo = models.DateField(
        _("apolo"), choices=MoonLandings.choices, default=MoonLandings.APOLLO_11)

    # ! https://docs.python.org/3/library/enum.html#module-enum
    class Rating(models.IntegerChoices):
        LOW = 1, _('low')
        MIDDLE = 2, _('midle')
        HIGH = 3, _('high')
        __empty__ = _('no rating')

    rating = models.PositiveSmallIntegerField(
        _("rating"), choices=Rating.choices, blank=True, null=True)

    CITYES = [
        ('Russia', (
            ('moskow', 'Moskow'),
            ('rostov', 'Rostov'),
            ('irkutsk', 'Irkutsk'),
        )
        ),
        ('USA', (
                ('ny', 'New York'),
                ('boston', 'Boston'),
        )
        ),
        (None, 'Unknown'),
    ]
    city = models.CharField(_("city"), max_length=50,
                            choices=CITYES, blank=True)

    month = models.PositiveSmallIntegerField(
        _("month"), choices=settings.MONTHS, blank=False, default=3)

    SU = 'Su'
    MO = 'Mo'
    TU = 'Tu'
    WE = 'We'
    TH = 'Th'
    FR = 'Fr'
    SA = 'Sa'
    WEEK_DAYS = [
        (None, 'empty'),
        (SU, 'Sunday'),
        (MO, 'Monday'),
        (TU, 'Tuesday'),
        (WE, 'Wednesday'),
        (TH, 'Thursday'),
        (FR, 'Friday'),
        (SA, 'Saturday'),
    ]

    week = models.CharField(_("week"), max_length=50,
                            choices=WEEK_DAYS, blank=True)

    name = models.CharField(_("name"), max_length=150)
    slug = models.SlugField(_("url"))

    class Meta:
        verbose_name = _("post")
        verbose_name_plural = _("posts")
        db_table = 'posts'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})

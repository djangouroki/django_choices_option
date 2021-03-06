# Generated by Django 3.1 on 2020-10-04 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200912_0731'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='month',
            field=models.PositiveSmallIntegerField(choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')], default=1, verbose_name='month'),
            preserve_default=False,
        ),
    ]

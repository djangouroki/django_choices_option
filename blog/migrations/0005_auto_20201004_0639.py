# Generated by Django 3.1 on 2020-10-04 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20201004_0632'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='city',
            field=models.CharField(blank=True, choices=[('Russia', (('moskow', 'Moskow'), ('rostov', 'Rostov'), ('irkutsk', 'Irkutsk'))), ('USA', (('ny', 'New York'), ('boston', 'Boston'))), (None, 'Unknown')], max_length=50, verbose_name='city'),
        ),
        migrations.AlterField(
            model_name='post',
            name='week',
            field=models.CharField(blank=True, choices=[(None, 'empty'), ('Su', 'Sunday'), ('Mo', 'Monday'), ('Tu', 'Tuesday'), ('We', 'Wednesday'), ('Th', 'Thursday'), ('Fr', 'Friday'), ('Sa', 'Saturday')], max_length=50, verbose_name='week'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluationcriteria',
            name='evaluation',
            field=models.ForeignKey(related_name='restaurantdishes', to='web.Evaluation'),
        ),
    ]

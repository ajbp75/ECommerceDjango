# Generated by Django 4.0.5 on 2022-06-16 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_imagem',
            field=models.CharField(default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9UJ59dr2BIhE0iqFmjj8ea7mbmbW9qsENPg&usqp=CAU', max_length=500),
        ),
    ]

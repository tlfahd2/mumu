# Generated by Django 4.2.7 on 2023-11-20 15:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('profile_path', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('profile_path', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('adult', models.BooleanField()),
                ('title', models.CharField(max_length=100)),
                ('overview', models.TextField(blank=True, null=True)),
                ('popularity', models.FloatField(blank=True, null=True)),
                ('poster_path', models.TextField(blank=True, null=True)),
                ('release_date', models.DateField(blank=True, null=True)),
                ('runtime', models.IntegerField(blank=True, null=True)),
                ('vote_average', models.FloatField(blank=True, null=True)),
                ('vote_count', models.IntegerField(blank=True, null=True)),
                ('trailer', models.TextField(blank=True, null=True)),
                ('actors', models.ManyToManyField(to='movies.actor')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.director')),
                ('genres', models.ManyToManyField(to='movies.genre')),
                ('like_users', models.ManyToManyField(blank=True, related_name='like_movies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('rank', models.FloatField()),
                ('is_like', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('like_users', models.ManyToManyField(related_name='hate_users', to=settings.AUTH_USER_MODEL)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_comments', to='movies.review')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_comment_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

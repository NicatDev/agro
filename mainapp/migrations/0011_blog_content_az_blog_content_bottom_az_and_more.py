# Generated by Django 5.0.4 on 2024-04-25 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_blog_content_bottom'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='content_az',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='content_bottom_az',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='blog',
            name='content_bottom_en',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='blog',
            name='content_bottom_ru',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='blog',
            name='content_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='content_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='title_az',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='title_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='title_ru',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='blogcategory',
            name='name_az',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='blogcategory',
            name='name_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='blogcategory',
            name='name_ru',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_az',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ru',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description_az',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='location_az',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='location_en',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='location_ru',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_az',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_ru',
            field=models.CharField(max_length=200, null=True),
        ),
    ]

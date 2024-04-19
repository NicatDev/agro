# Generated by Django 5.0.4 on 2024-04-17 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_partner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instagram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('href', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name='message',
            old_name='full_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='subject',
            new_name='phone',
        ),
        migrations.AddField(
            model_name='message',
            name='surname',
            field=models.CharField(default='s', max_length=200),
            preserve_default=False,
        ),
    ]

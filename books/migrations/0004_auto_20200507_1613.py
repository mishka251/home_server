# Generated by Django 2.2.4 on 2020-05-07 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20200507_1100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookfile',
            name='file_path',
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='author',
            name='surname',
            field=models.CharField(max_length=200, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='bookfile',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='books.Author', verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='bookfile',
            name='genres',
            field=models.ManyToManyField(to='books.BookGenre', verbose_name='Жанры'),
        ),
        migrations.AlterField(
            model_name='bookfile',
            name='name',
            field=models.CharField(max_length=100, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='bookgenre',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Название'),
        ),
    ]

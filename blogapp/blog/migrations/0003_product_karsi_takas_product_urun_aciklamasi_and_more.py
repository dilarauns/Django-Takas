# Generated by Django 4.2.5 on 2023-12-20 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_person_email_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='karsi_takas',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='urun_aciklamasi',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='urun_durum',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='urun_kategori',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='urun_mekani',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='sehir',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='urun_adi',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
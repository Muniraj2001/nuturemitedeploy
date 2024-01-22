# Generated by Django 4.2.7 on 2023-11-30 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0038_alter_customer_state_alter_orderplaced_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='images',
        ),
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('Bihar', 'Bihar'), ('Gujrat', 'Gujrat'), ('Assam', 'Assam'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Haryana', 'Haryana'), ('Goa', 'Goa'), ('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'), ('Chandigarh', 'Chandigarh'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Daman and Diu', 'Daman and Diu'), ('Delhi', 'Delhi'), ('Chattisgarh', 'Chattisgarh')], max_length=100),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Packed', 'packed'), ('Cancel', 'Cancel'), ('Accepted', 'Accepted'), ('Delivered', 'Delivered'), ('Pending', 'Pending'), ('On The Wey', 'On The Way')], default='pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='popular',
            name='category',
            field=models.CharField(choices=[('DH', 'Digestive Health'), ('VM', 'Vitamins&Minerals'), ('SH', 'Sexual health'), ('MH', 'Men Health'), ('HS', 'Herbal, Specialty Supplements'), ('WH', 'Women health'), ('OG', 'Organic'), ('IH', 'Immune Health'), ('AN', 'Antioxidants'), ('GH', 'General Health'), ('PC', 'Personal Care'), ('AV', 'Ayurvedic')], max_length=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('DH', 'Digestive Health'), ('VM', 'Vitamins&Minerals'), ('SH', 'Sexual health'), ('MH', 'Men Health'), ('HS', 'Herbal, Specialty Supplements'), ('WH', 'Women health'), ('OG', 'Organic'), ('IH', 'Immune Health'), ('AN', 'Antioxidants'), ('GH', 'General Health'), ('PC', 'Personal Care'), ('AV', 'Ayurvedic')], max_length=2),
        ),
        migrations.AlterField(
            model_name='product1',
            name='category',
            field=models.CharField(choices=[('DH', 'Digestive Health'), ('VM', 'Vitamins&Minerals'), ('SH', 'Sexual health'), ('MH', 'Men Health'), ('HS', 'Herbal, Specialty Supplements'), ('WH', 'Women health'), ('OG', 'Organic'), ('IH', 'Immune Health'), ('AN', 'Antioxidants'), ('GH', 'General Health'), ('PC', 'Personal Care'), ('AV', 'Ayurvedic')], max_length=2),
        ),
        migrations.AlterField(
            model_name='specialoffer',
            name='category',
            field=models.CharField(choices=[('DH', 'Digestive Health'), ('VM', 'Vitamins&Minerals'), ('SH', 'Sexual health'), ('MH', 'Men Health'), ('HS', 'Herbal, Specialty Supplements'), ('WH', 'Women health'), ('OG', 'Organic'), ('IH', 'Immune Health'), ('AN', 'Antioxidants'), ('GH', 'General Health'), ('PC', 'Personal Care'), ('AV', 'Ayurvedic')], max_length=2),
        ),
    ]
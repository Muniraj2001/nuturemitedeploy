# Generated by Django 4.2.7 on 2023-11-20 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_shop_alter_customer_state_alter_orderplaced_status_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Shop',
        ),
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Gujrat', 'Gujrat'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'), ('Assam', 'Assam'), ('Delhi', 'Delhi'), ('Chandigarh', 'Chandigarh'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Haryana', 'Haryana'), ('Daman and Diu', 'Daman and Diu'), ('Bihar', 'Bihar'), ('Goa', 'Goa'), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('Chattisgarh', 'Chattisgarh')], max_length=100),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Packed', 'packed'), ('Delivered', 'Delivered'), ('On The Wey', 'On The Way'), ('Accepted', 'Accepted'), ('Cancel', 'Cancel'), ('Pending', 'Pending')], default='pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('WH', 'Women health'), ('IH', 'Immune Health'), ('AV', 'Ayurvedic'), ('MH', 'Men Health'), ('OG', 'Organic'), ('GH', 'General Health'), ('DH', 'Digestive Health'), ('SH', 'Sexual health'), ('HS', 'Herbal, Specialty Supplements'), ('PC', 'Personal Care'), ('VM', 'Vitamins&Minerals'), ('AN', 'Antioxidants')], max_length=2),
        ),
        migrations.AlterField(
            model_name='product1',
            name='category',
            field=models.CharField(choices=[('WH', 'Women health'), ('IH', 'Immune Health'), ('AV', 'Ayurvedic'), ('MH', 'Men Health'), ('OG', 'Organic'), ('GH', 'General Health'), ('DH', 'Digestive Health'), ('SH', 'Sexual health'), ('HS', 'Herbal, Specialty Supplements'), ('PC', 'Personal Care'), ('VM', 'Vitamins&Minerals'), ('AN', 'Antioxidants')], max_length=2),
        ),
        migrations.AlterField(
            model_name='specialoffer',
            name='category',
            field=models.CharField(choices=[('WH', 'Women health'), ('IH', 'Immune Health'), ('AV', 'Ayurvedic'), ('MH', 'Men Health'), ('OG', 'Organic'), ('GH', 'General Health'), ('DH', 'Digestive Health'), ('SH', 'Sexual health'), ('HS', 'Herbal, Specialty Supplements'), ('PC', 'Personal Care'), ('VM', 'Vitamins&Minerals'), ('AN', 'Antioxidants')], max_length=2),
        ),
    ]
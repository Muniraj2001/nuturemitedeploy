# Generated by Django 4.2.7 on 2024-01-04 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0104_alter_customer_state_alter_orderplaced_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Gujrat', 'Gujrat'), ('Daman and Diu', 'Daman and Diu'), ('Chandigarh', 'Chandigarh'), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('Delhi', 'Delhi'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Goa', 'Goa'), ('Assam', 'Assam'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Bihar', 'Bihar'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Haryana', 'Haryana'), ('Chattisgarh', 'Chattisgarh'), ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'), ('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands')], max_length=100),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('On The Wey', 'On The Way'), ('Delivered', 'Delivered'), ('Packed', 'packed'), ('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Cancel', 'Cancel')], default='pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='popular',
            name='category',
            field=models.CharField(choices=[('B12', 'Vitamin B12'), ('C', 'Vitamin C'), ('DH', 'Digestive Health'), ('A', 'Vitamin A'), ('HS', 'Herbal, Specialty Supplements'), ('E', 'Vitamin E'), ('D3', 'Vitamin D3'), ('VM', 'Vitamins&Minerals'), ('SH', 'Sexual health'), ('PC', 'Personal Care'), ('OG', 'Organic'), ('K', 'Vitamin K'), ('AV', 'Ayurvedic'), ('AN', 'Antioxidants'), ('MH', 'Men Health'), ('IH', 'Immune Health'), ('GH', 'General Health'), ('WH', 'Women health')], max_length=3),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('B12', 'Vitamin B12'), ('C', 'Vitamin C'), ('DH', 'Digestive Health'), ('A', 'Vitamin A'), ('HS', 'Herbal, Specialty Supplements'), ('E', 'Vitamin E'), ('D3', 'Vitamin D3'), ('VM', 'Vitamins&Minerals'), ('SH', 'Sexual health'), ('PC', 'Personal Care'), ('OG', 'Organic'), ('K', 'Vitamin K'), ('AV', 'Ayurvedic'), ('AN', 'Antioxidants'), ('MH', 'Men Health'), ('IH', 'Immune Health'), ('GH', 'General Health'), ('WH', 'Women health')], max_length=3),
        ),
        migrations.AlterField(
            model_name='product1',
            name='category',
            field=models.CharField(choices=[('B12', 'Vitamin B12'), ('C', 'Vitamin C'), ('DH', 'Digestive Health'), ('A', 'Vitamin A'), ('HS', 'Herbal, Specialty Supplements'), ('E', 'Vitamin E'), ('D3', 'Vitamin D3'), ('VM', 'Vitamins&Minerals'), ('SH', 'Sexual health'), ('PC', 'Personal Care'), ('OG', 'Organic'), ('K', 'Vitamin K'), ('AV', 'Ayurvedic'), ('AN', 'Antioxidants'), ('MH', 'Men Health'), ('IH', 'Immune Health'), ('GH', 'General Health'), ('WH', 'Women health')], max_length=3),
        ),
        migrations.AlterField(
            model_name='shopnow',
            name='category',
            field=models.CharField(choices=[('B12', 'Vitamin B12'), ('C', 'Vitamin C'), ('DH', 'Digestive Health'), ('A', 'Vitamin A'), ('HS', 'Herbal, Specialty Supplements'), ('E', 'Vitamin E'), ('D3', 'Vitamin D3'), ('VM', 'Vitamins&Minerals'), ('SH', 'Sexual health'), ('PC', 'Personal Care'), ('OG', 'Organic'), ('K', 'Vitamin K'), ('AV', 'Ayurvedic'), ('AN', 'Antioxidants'), ('MH', 'Men Health'), ('IH', 'Immune Health'), ('GH', 'General Health'), ('WH', 'Women health')], max_length=3),
        ),
        migrations.AlterField(
            model_name='specialoffer',
            name='category',
            field=models.CharField(choices=[('B12', 'Vitamin B12'), ('C', 'Vitamin C'), ('DH', 'Digestive Health'), ('A', 'Vitamin A'), ('HS', 'Herbal, Specialty Supplements'), ('E', 'Vitamin E'), ('D3', 'Vitamin D3'), ('VM', 'Vitamins&Minerals'), ('SH', 'Sexual health'), ('PC', 'Personal Care'), ('OG', 'Organic'), ('K', 'Vitamin K'), ('AV', 'Ayurvedic'), ('AN', 'Antioxidants'), ('MH', 'Men Health'), ('IH', 'Immune Health'), ('GH', 'General Health'), ('WH', 'Women health')], max_length=3),
        ),
    ]

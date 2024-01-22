# Generated by Django 4.0.6 on 2024-01-22 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0158_alter_customer_state_alter_orderplaced_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Haryana', 'Haryana'), ('Chattisgarh', 'Chattisgarh'), ('Daman and Diu', 'Daman and Diu'), ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('Bihar', 'Bihar'), ('Goa', 'Goa'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'), ('Chandigarh', 'Chandigarh'), ('Gujrat', 'Gujrat'), ('Delhi', 'Delhi'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Assam', 'Assam'), ('Himachal Pradesh', 'Himachal Pradesh')], max_length=100),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Packed', 'packed'), ('Cancel', 'Cancel'), ('On The Wey', 'On The Way'), ('Accepted', 'Accepted'), ('Delivered', 'Delivered')], default='pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='popular',
            name='category',
            field=models.CharField(choices=[('B12', 'Vitamin B12'), ('IH', 'Immune Health'), ('SH', 'Sexual health'), ('PC', 'Personal Care'), ('D3', 'Vitamin D3'), ('AV', 'Ayurvedic'), ('A', 'Vitamin A'), ('DH', 'Digestive Health'), ('WH', 'Women health'), ('AN', 'Antioxidants'), ('K', 'Vitamin K'), ('E', 'Vitamin E'), ('C', 'Vitamin C'), ('MH', 'Men Health'), ('GH', 'General Health'), ('OG', 'Organic'), ('HS', 'Herbal, Specialty Supplements'), ('VM', 'Vitamins&Minerals')], max_length=3),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('B12', 'Vitamin B12'), ('IH', 'Immune Health'), ('SH', 'Sexual health'), ('PC', 'Personal Care'), ('D3', 'Vitamin D3'), ('AV', 'Ayurvedic'), ('A', 'Vitamin A'), ('DH', 'Digestive Health'), ('WH', 'Women health'), ('AN', 'Antioxidants'), ('K', 'Vitamin K'), ('E', 'Vitamin E'), ('C', 'Vitamin C'), ('MH', 'Men Health'), ('GH', 'General Health'), ('OG', 'Organic'), ('HS', 'Herbal, Specialty Supplements'), ('VM', 'Vitamins&Minerals')], max_length=3),
        ),
        migrations.AlterField(
            model_name='product1',
            name='category',
            field=models.CharField(choices=[('B12', 'Vitamin B12'), ('IH', 'Immune Health'), ('SH', 'Sexual health'), ('PC', 'Personal Care'), ('D3', 'Vitamin D3'), ('AV', 'Ayurvedic'), ('A', 'Vitamin A'), ('DH', 'Digestive Health'), ('WH', 'Women health'), ('AN', 'Antioxidants'), ('K', 'Vitamin K'), ('E', 'Vitamin E'), ('C', 'Vitamin C'), ('MH', 'Men Health'), ('GH', 'General Health'), ('OG', 'Organic'), ('HS', 'Herbal, Specialty Supplements'), ('VM', 'Vitamins&Minerals')], max_length=3),
        ),
        migrations.AlterField(
            model_name='shopnow',
            name='category',
            field=models.CharField(choices=[('B12', 'Vitamin B12'), ('IH', 'Immune Health'), ('SH', 'Sexual health'), ('PC', 'Personal Care'), ('D3', 'Vitamin D3'), ('AV', 'Ayurvedic'), ('A', 'Vitamin A'), ('DH', 'Digestive Health'), ('WH', 'Women health'), ('AN', 'Antioxidants'), ('K', 'Vitamin K'), ('E', 'Vitamin E'), ('C', 'Vitamin C'), ('MH', 'Men Health'), ('GH', 'General Health'), ('OG', 'Organic'), ('HS', 'Herbal, Specialty Supplements'), ('VM', 'Vitamins&Minerals')], max_length=3),
        ),
        migrations.AlterField(
            model_name='specialoffer',
            name='category',
            field=models.CharField(choices=[('B12', 'Vitamin B12'), ('IH', 'Immune Health'), ('SH', 'Sexual health'), ('PC', 'Personal Care'), ('D3', 'Vitamin D3'), ('AV', 'Ayurvedic'), ('A', 'Vitamin A'), ('DH', 'Digestive Health'), ('WH', 'Women health'), ('AN', 'Antioxidants'), ('K', 'Vitamin K'), ('E', 'Vitamin E'), ('C', 'Vitamin C'), ('MH', 'Men Health'), ('GH', 'General Health'), ('OG', 'Organic'), ('HS', 'Herbal, Specialty Supplements'), ('VM', 'Vitamins&Minerals')], max_length=3),
        ),
    ]

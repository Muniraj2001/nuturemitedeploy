# Generated by Django 4.2.7 on 2024-01-10 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0130_alter_customer_state_alter_orderplaced_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Bihar', 'Bihar'), ('Goa', 'Goa'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Delhi', 'Delhi'), ('Chattisgarh', 'Chattisgarh'), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('Gujrat', 'Gujrat'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'), ('Assam', 'Assam'), ('Haryana', 'Haryana'), ('Chandigarh', 'Chandigarh'), ('Daman and Diu', 'Daman and Diu'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands')], max_length=100),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Packed', 'packed'), ('Delivered', 'Delivered'), ('Cancel', 'Cancel'), ('Accepted', 'Accepted'), ('Pending', 'Pending'), ('On The Wey', 'On The Way')], default='pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='popular',
            name='category',
            field=models.CharField(choices=[('B12', 'Vitamin B12'), ('SH', 'Sexual health'), ('HS', 'Herbal, Specialty Supplements'), ('GH', 'General Health'), ('PC', 'Personal Care'), ('WH', 'Women health'), ('K', 'Vitamin K'), ('VM', 'Vitamins&Minerals'), ('MH', 'Men Health'), ('DH', 'Digestive Health'), ('OG', 'Organic'), ('A', 'Vitamin A'), ('D3', 'Vitamin D3'), ('AV', 'Ayurvedic'), ('AN', 'Antioxidants'), ('E', 'Vitamin E'), ('C', 'Vitamin C'), ('IH', 'Immune Health')], max_length=3),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('B12', 'Vitamin B12'), ('SH', 'Sexual health'), ('HS', 'Herbal, Specialty Supplements'), ('GH', 'General Health'), ('PC', 'Personal Care'), ('WH', 'Women health'), ('K', 'Vitamin K'), ('VM', 'Vitamins&Minerals'), ('MH', 'Men Health'), ('DH', 'Digestive Health'), ('OG', 'Organic'), ('A', 'Vitamin A'), ('D3', 'Vitamin D3'), ('AV', 'Ayurvedic'), ('AN', 'Antioxidants'), ('E', 'Vitamin E'), ('C', 'Vitamin C'), ('IH', 'Immune Health')], max_length=3),
        ),
        migrations.AlterField(
            model_name='product1',
            name='category',
            field=models.CharField(choices=[('B12', 'Vitamin B12'), ('SH', 'Sexual health'), ('HS', 'Herbal, Specialty Supplements'), ('GH', 'General Health'), ('PC', 'Personal Care'), ('WH', 'Women health'), ('K', 'Vitamin K'), ('VM', 'Vitamins&Minerals'), ('MH', 'Men Health'), ('DH', 'Digestive Health'), ('OG', 'Organic'), ('A', 'Vitamin A'), ('D3', 'Vitamin D3'), ('AV', 'Ayurvedic'), ('AN', 'Antioxidants'), ('E', 'Vitamin E'), ('C', 'Vitamin C'), ('IH', 'Immune Health')], max_length=3),
        ),
        migrations.AlterField(
            model_name='shopnow',
            name='category',
            field=models.CharField(choices=[('B12', 'Vitamin B12'), ('SH', 'Sexual health'), ('HS', 'Herbal, Specialty Supplements'), ('GH', 'General Health'), ('PC', 'Personal Care'), ('WH', 'Women health'), ('K', 'Vitamin K'), ('VM', 'Vitamins&Minerals'), ('MH', 'Men Health'), ('DH', 'Digestive Health'), ('OG', 'Organic'), ('A', 'Vitamin A'), ('D3', 'Vitamin D3'), ('AV', 'Ayurvedic'), ('AN', 'Antioxidants'), ('E', 'Vitamin E'), ('C', 'Vitamin C'), ('IH', 'Immune Health')], max_length=3),
        ),
        migrations.AlterField(
            model_name='specialoffer',
            name='category',
            field=models.CharField(choices=[('B12', 'Vitamin B12'), ('SH', 'Sexual health'), ('HS', 'Herbal, Specialty Supplements'), ('GH', 'General Health'), ('PC', 'Personal Care'), ('WH', 'Women health'), ('K', 'Vitamin K'), ('VM', 'Vitamins&Minerals'), ('MH', 'Men Health'), ('DH', 'Digestive Health'), ('OG', 'Organic'), ('A', 'Vitamin A'), ('D3', 'Vitamin D3'), ('AV', 'Ayurvedic'), ('AN', 'Antioxidants'), ('E', 'Vitamin E'), ('C', 'Vitamin C'), ('IH', 'Immune Health')], max_length=3),
        ),
    ]
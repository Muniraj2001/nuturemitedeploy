# Generated by Django 4.2.7 on 2024-01-04 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0095_payment_order_alter_customer_state_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='order',
        ),
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Gujrat', 'Gujrat'), ('Daman and Diu', 'Daman and Diu'), ('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'), ('Chandigarh', 'Chandigarh'), ('Chattisgarh', 'Chattisgarh'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Bihar', 'Bihar'), ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Haryana', 'Haryana'), ('Assam', 'Assam'), ('Goa', 'Goa'), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Delhi', 'Delhi')], max_length=100),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('Cancel', 'Cancel'), ('Accepted', 'Accepted'), ('Packed', 'packed'), ('On The Wey', 'On The Way'), ('Pending', 'Pending')], default='pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='popular',
            name='category',
            field=models.CharField(choices=[('B12', 'Vitamin B12'), ('MH', 'Men Health'), ('D3', 'Vitamin D3'), ('OG', 'Organic'), ('GH', 'General Health'), ('VM', 'Vitamins&Minerals'), ('HS', 'Herbal, Specialty Supplements'), ('E', 'Vitamin E'), ('AV', 'Ayurvedic'), ('PC', 'Personal Care'), ('AN', 'Antioxidants'), ('SH', 'Sexual health'), ('IH', 'Immune Health'), ('A', 'Vitamin A'), ('C', 'Vitamin C'), ('K', 'Vitamin K'), ('DH', 'Digestive Health'), ('WH', 'Women health')], max_length=3),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('B12', 'Vitamin B12'), ('MH', 'Men Health'), ('D3', 'Vitamin D3'), ('OG', 'Organic'), ('GH', 'General Health'), ('VM', 'Vitamins&Minerals'), ('HS', 'Herbal, Specialty Supplements'), ('E', 'Vitamin E'), ('AV', 'Ayurvedic'), ('PC', 'Personal Care'), ('AN', 'Antioxidants'), ('SH', 'Sexual health'), ('IH', 'Immune Health'), ('A', 'Vitamin A'), ('C', 'Vitamin C'), ('K', 'Vitamin K'), ('DH', 'Digestive Health'), ('WH', 'Women health')], max_length=3),
        ),
        migrations.AlterField(
            model_name='product1',
            name='category',
            field=models.CharField(choices=[('B12', 'Vitamin B12'), ('MH', 'Men Health'), ('D3', 'Vitamin D3'), ('OG', 'Organic'), ('GH', 'General Health'), ('VM', 'Vitamins&Minerals'), ('HS', 'Herbal, Specialty Supplements'), ('E', 'Vitamin E'), ('AV', 'Ayurvedic'), ('PC', 'Personal Care'), ('AN', 'Antioxidants'), ('SH', 'Sexual health'), ('IH', 'Immune Health'), ('A', 'Vitamin A'), ('C', 'Vitamin C'), ('K', 'Vitamin K'), ('DH', 'Digestive Health'), ('WH', 'Women health')], max_length=3),
        ),
        migrations.AlterField(
            model_name='shopnow',
            name='category',
            field=models.CharField(choices=[('B12', 'Vitamin B12'), ('MH', 'Men Health'), ('D3', 'Vitamin D3'), ('OG', 'Organic'), ('GH', 'General Health'), ('VM', 'Vitamins&Minerals'), ('HS', 'Herbal, Specialty Supplements'), ('E', 'Vitamin E'), ('AV', 'Ayurvedic'), ('PC', 'Personal Care'), ('AN', 'Antioxidants'), ('SH', 'Sexual health'), ('IH', 'Immune Health'), ('A', 'Vitamin A'), ('C', 'Vitamin C'), ('K', 'Vitamin K'), ('DH', 'Digestive Health'), ('WH', 'Women health')], max_length=3),
        ),
        migrations.AlterField(
            model_name='specialoffer',
            name='category',
            field=models.CharField(choices=[('B12', 'Vitamin B12'), ('MH', 'Men Health'), ('D3', 'Vitamin D3'), ('OG', 'Organic'), ('GH', 'General Health'), ('VM', 'Vitamins&Minerals'), ('HS', 'Herbal, Specialty Supplements'), ('E', 'Vitamin E'), ('AV', 'Ayurvedic'), ('PC', 'Personal Care'), ('AN', 'Antioxidants'), ('SH', 'Sexual health'), ('IH', 'Immune Health'), ('A', 'Vitamin A'), ('C', 'Vitamin C'), ('K', 'Vitamin K'), ('DH', 'Digestive Health'), ('WH', 'Women health')], max_length=3),
        ),
    ]

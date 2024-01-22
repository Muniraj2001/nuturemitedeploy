# Generated by Django 4.2.7 on 2024-01-09 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0124_alter_customer_state_alter_orderplaced_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Assam', 'Assam'), ('Haryana', 'Haryana'), ('Goa', 'Goa'), ('Bihar', 'Bihar'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Gujrat', 'Gujrat'), ('Delhi', 'Delhi'), ('Chattisgarh', 'Chattisgarh'), ('Chandigarh', 'Chandigarh'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Daman and Diu', 'Daman and Diu'), ('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'), ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli')], max_length=100),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('On The Wey', 'On The Way'), ('Packed', 'packed'), ('Pending', 'Pending'), ('Delivered', 'Delivered'), ('Cancel', 'Cancel'), ('Accepted', 'Accepted')], default='pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='popular',
            name='category',
            field=models.CharField(choices=[('D3', 'Vitamin D3'), ('AV', 'Ayurvedic'), ('MH', 'Men Health'), ('AN', 'Antioxidants'), ('IH', 'Immune Health'), ('HS', 'Herbal, Specialty Supplements'), ('B12', 'Vitamin B12'), ('K', 'Vitamin K'), ('DH', 'Digestive Health'), ('PC', 'Personal Care'), ('C', 'Vitamin C'), ('E', 'Vitamin E'), ('GH', 'General Health'), ('WH', 'Women health'), ('A', 'Vitamin A'), ('VM', 'Vitamins&Minerals'), ('SH', 'Sexual health'), ('OG', 'Organic')], max_length=3),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('D3', 'Vitamin D3'), ('AV', 'Ayurvedic'), ('MH', 'Men Health'), ('AN', 'Antioxidants'), ('IH', 'Immune Health'), ('HS', 'Herbal, Specialty Supplements'), ('B12', 'Vitamin B12'), ('K', 'Vitamin K'), ('DH', 'Digestive Health'), ('PC', 'Personal Care'), ('C', 'Vitamin C'), ('E', 'Vitamin E'), ('GH', 'General Health'), ('WH', 'Women health'), ('A', 'Vitamin A'), ('VM', 'Vitamins&Minerals'), ('SH', 'Sexual health'), ('OG', 'Organic')], max_length=3),
        ),
        migrations.AlterField(
            model_name='product1',
            name='category',
            field=models.CharField(choices=[('D3', 'Vitamin D3'), ('AV', 'Ayurvedic'), ('MH', 'Men Health'), ('AN', 'Antioxidants'), ('IH', 'Immune Health'), ('HS', 'Herbal, Specialty Supplements'), ('B12', 'Vitamin B12'), ('K', 'Vitamin K'), ('DH', 'Digestive Health'), ('PC', 'Personal Care'), ('C', 'Vitamin C'), ('E', 'Vitamin E'), ('GH', 'General Health'), ('WH', 'Women health'), ('A', 'Vitamin A'), ('VM', 'Vitamins&Minerals'), ('SH', 'Sexual health'), ('OG', 'Organic')], max_length=3),
        ),
        migrations.AlterField(
            model_name='shopnow',
            name='category',
            field=models.CharField(choices=[('D3', 'Vitamin D3'), ('AV', 'Ayurvedic'), ('MH', 'Men Health'), ('AN', 'Antioxidants'), ('IH', 'Immune Health'), ('HS', 'Herbal, Specialty Supplements'), ('B12', 'Vitamin B12'), ('K', 'Vitamin K'), ('DH', 'Digestive Health'), ('PC', 'Personal Care'), ('C', 'Vitamin C'), ('E', 'Vitamin E'), ('GH', 'General Health'), ('WH', 'Women health'), ('A', 'Vitamin A'), ('VM', 'Vitamins&Minerals'), ('SH', 'Sexual health'), ('OG', 'Organic')], max_length=3),
        ),
        migrations.AlterField(
            model_name='specialoffer',
            name='category',
            field=models.CharField(choices=[('D3', 'Vitamin D3'), ('AV', 'Ayurvedic'), ('MH', 'Men Health'), ('AN', 'Antioxidants'), ('IH', 'Immune Health'), ('HS', 'Herbal, Specialty Supplements'), ('B12', 'Vitamin B12'), ('K', 'Vitamin K'), ('DH', 'Digestive Health'), ('PC', 'Personal Care'), ('C', 'Vitamin C'), ('E', 'Vitamin E'), ('GH', 'General Health'), ('WH', 'Women health'), ('A', 'Vitamin A'), ('VM', 'Vitamins&Minerals'), ('SH', 'Sexual health'), ('OG', 'Organic')], max_length=3),
        ),
        migrations.CreateModel(
            name='ProductPack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('weight', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('in_stock', models.BooleanField(default=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
            ],
        ),
    ]

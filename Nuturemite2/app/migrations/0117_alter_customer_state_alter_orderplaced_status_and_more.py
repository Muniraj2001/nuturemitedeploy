# Generated by Django 4.2.7 on 2024-01-08 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0116_coupon_expiration_date_alter_customer_state_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Daman and Diu', 'Daman and Diu'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Delhi', 'Delhi'), ('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'), ('Haryana', 'Haryana'), ('Chandigarh', 'Chandigarh'), ('Goa', 'Goa'), ('Chattisgarh', 'Chattisgarh'), ('Bihar', 'Bihar'), ('Gujrat', 'Gujrat'), ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Assam', 'Assam')], max_length=100),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('Packed', 'packed'), ('Cancel', 'Cancel'), ('On The Wey', 'On The Way'), ('Pending', 'Pending'), ('Accepted', 'Accepted')], default='pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='popular',
            name='category',
            field=models.CharField(choices=[('OG', 'Organic'), ('HS', 'Herbal, Specialty Supplements'), ('MH', 'Men Health'), ('B12', 'Vitamin B12'), ('SH', 'Sexual health'), ('D3', 'Vitamin D3'), ('A', 'Vitamin A'), ('E', 'Vitamin E'), ('WH', 'Women health'), ('K', 'Vitamin K'), ('IH', 'Immune Health'), ('GH', 'General Health'), ('AN', 'Antioxidants'), ('VM', 'Vitamins&Minerals'), ('PC', 'Personal Care'), ('AV', 'Ayurvedic'), ('C', 'Vitamin C'), ('DH', 'Digestive Health')], max_length=3),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('OG', 'Organic'), ('HS', 'Herbal, Specialty Supplements'), ('MH', 'Men Health'), ('B12', 'Vitamin B12'), ('SH', 'Sexual health'), ('D3', 'Vitamin D3'), ('A', 'Vitamin A'), ('E', 'Vitamin E'), ('WH', 'Women health'), ('K', 'Vitamin K'), ('IH', 'Immune Health'), ('GH', 'General Health'), ('AN', 'Antioxidants'), ('VM', 'Vitamins&Minerals'), ('PC', 'Personal Care'), ('AV', 'Ayurvedic'), ('C', 'Vitamin C'), ('DH', 'Digestive Health')], max_length=3),
        ),
        migrations.AlterField(
            model_name='product1',
            name='category',
            field=models.CharField(choices=[('OG', 'Organic'), ('HS', 'Herbal, Specialty Supplements'), ('MH', 'Men Health'), ('B12', 'Vitamin B12'), ('SH', 'Sexual health'), ('D3', 'Vitamin D3'), ('A', 'Vitamin A'), ('E', 'Vitamin E'), ('WH', 'Women health'), ('K', 'Vitamin K'), ('IH', 'Immune Health'), ('GH', 'General Health'), ('AN', 'Antioxidants'), ('VM', 'Vitamins&Minerals'), ('PC', 'Personal Care'), ('AV', 'Ayurvedic'), ('C', 'Vitamin C'), ('DH', 'Digestive Health')], max_length=3),
        ),
        migrations.AlterField(
            model_name='shopnow',
            name='category',
            field=models.CharField(choices=[('OG', 'Organic'), ('HS', 'Herbal, Specialty Supplements'), ('MH', 'Men Health'), ('B12', 'Vitamin B12'), ('SH', 'Sexual health'), ('D3', 'Vitamin D3'), ('A', 'Vitamin A'), ('E', 'Vitamin E'), ('WH', 'Women health'), ('K', 'Vitamin K'), ('IH', 'Immune Health'), ('GH', 'General Health'), ('AN', 'Antioxidants'), ('VM', 'Vitamins&Minerals'), ('PC', 'Personal Care'), ('AV', 'Ayurvedic'), ('C', 'Vitamin C'), ('DH', 'Digestive Health')], max_length=3),
        ),
        migrations.AlterField(
            model_name='specialoffer',
            name='category',
            field=models.CharField(choices=[('OG', 'Organic'), ('HS', 'Herbal, Specialty Supplements'), ('MH', 'Men Health'), ('B12', 'Vitamin B12'), ('SH', 'Sexual health'), ('D3', 'Vitamin D3'), ('A', 'Vitamin A'), ('E', 'Vitamin E'), ('WH', 'Women health'), ('K', 'Vitamin K'), ('IH', 'Immune Health'), ('GH', 'General Health'), ('AN', 'Antioxidants'), ('VM', 'Vitamins&Minerals'), ('PC', 'Personal Care'), ('AV', 'Ayurvedic'), ('C', 'Vitamin C'), ('DH', 'Digestive Health')], max_length=3),
        ),
        migrations.CreateModel(
            name='ProductPack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('weight', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('is_out_of_stock', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='packs', to='app.product')),
            ],
        ),
    ]

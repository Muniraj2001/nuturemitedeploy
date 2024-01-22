# Generated by Django 4.2.7 on 2024-01-04 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0099_alter_customer_state_alter_orderplaced_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='order',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='app.orderplaced'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Arunachal Pradesh', 'Arunachal Pradesh'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'), ('Assam', 'Assam'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Haryana', 'Haryana'), ('Goa', 'Goa'), ('Delhi', 'Delhi'), ('Gujrat', 'Gujrat'), ('Chattisgarh', 'Chattisgarh'), ('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'), ('Bihar', 'Bihar'), ('Chandigarh', 'Chandigarh'), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('Daman and Diu', 'Daman and Diu')], max_length=100),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Cancel', 'Cancel'), ('Pending', 'Pending'), ('On The Wey', 'On The Way'), ('Delivered', 'Delivered'), ('Packed', 'packed')], default='pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='popular',
            name='category',
            field=models.CharField(choices=[('A', 'Vitamin A'), ('MH', 'Men Health'), ('WH', 'Women health'), ('DH', 'Digestive Health'), ('VM', 'Vitamins&Minerals'), ('PC', 'Personal Care'), ('IH', 'Immune Health'), ('B12', 'Vitamin B12'), ('HS', 'Herbal, Specialty Supplements'), ('D3', 'Vitamin D3'), ('OG', 'Organic'), ('AN', 'Antioxidants'), ('E', 'Vitamin E'), ('K', 'Vitamin K'), ('GH', 'General Health'), ('C', 'Vitamin C'), ('AV', 'Ayurvedic'), ('SH', 'Sexual health')], max_length=3),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('A', 'Vitamin A'), ('MH', 'Men Health'), ('WH', 'Women health'), ('DH', 'Digestive Health'), ('VM', 'Vitamins&Minerals'), ('PC', 'Personal Care'), ('IH', 'Immune Health'), ('B12', 'Vitamin B12'), ('HS', 'Herbal, Specialty Supplements'), ('D3', 'Vitamin D3'), ('OG', 'Organic'), ('AN', 'Antioxidants'), ('E', 'Vitamin E'), ('K', 'Vitamin K'), ('GH', 'General Health'), ('C', 'Vitamin C'), ('AV', 'Ayurvedic'), ('SH', 'Sexual health')], max_length=3),
        ),
        migrations.AlterField(
            model_name='product1',
            name='category',
            field=models.CharField(choices=[('A', 'Vitamin A'), ('MH', 'Men Health'), ('WH', 'Women health'), ('DH', 'Digestive Health'), ('VM', 'Vitamins&Minerals'), ('PC', 'Personal Care'), ('IH', 'Immune Health'), ('B12', 'Vitamin B12'), ('HS', 'Herbal, Specialty Supplements'), ('D3', 'Vitamin D3'), ('OG', 'Organic'), ('AN', 'Antioxidants'), ('E', 'Vitamin E'), ('K', 'Vitamin K'), ('GH', 'General Health'), ('C', 'Vitamin C'), ('AV', 'Ayurvedic'), ('SH', 'Sexual health')], max_length=3),
        ),
        migrations.AlterField(
            model_name='shopnow',
            name='category',
            field=models.CharField(choices=[('A', 'Vitamin A'), ('MH', 'Men Health'), ('WH', 'Women health'), ('DH', 'Digestive Health'), ('VM', 'Vitamins&Minerals'), ('PC', 'Personal Care'), ('IH', 'Immune Health'), ('B12', 'Vitamin B12'), ('HS', 'Herbal, Specialty Supplements'), ('D3', 'Vitamin D3'), ('OG', 'Organic'), ('AN', 'Antioxidants'), ('E', 'Vitamin E'), ('K', 'Vitamin K'), ('GH', 'General Health'), ('C', 'Vitamin C'), ('AV', 'Ayurvedic'), ('SH', 'Sexual health')], max_length=3),
        ),
        migrations.AlterField(
            model_name='specialoffer',
            name='category',
            field=models.CharField(choices=[('A', 'Vitamin A'), ('MH', 'Men Health'), ('WH', 'Women health'), ('DH', 'Digestive Health'), ('VM', 'Vitamins&Minerals'), ('PC', 'Personal Care'), ('IH', 'Immune Health'), ('B12', 'Vitamin B12'), ('HS', 'Herbal, Specialty Supplements'), ('D3', 'Vitamin D3'), ('OG', 'Organic'), ('AN', 'Antioxidants'), ('E', 'Vitamin E'), ('K', 'Vitamin K'), ('GH', 'General Health'), ('C', 'Vitamin C'), ('AV', 'Ayurvedic'), ('SH', 'Sexual health')], max_length=3),
        ),
    ]
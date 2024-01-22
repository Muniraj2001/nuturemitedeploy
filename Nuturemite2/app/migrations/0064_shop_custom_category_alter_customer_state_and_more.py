# Generated by Django 4.2.7 on 2023-12-25 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0063_alter_customer_state_alter_orderplaced_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='custom_category',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Haryana', 'Haryana'), ('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Delhi', 'Delhi'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Gujrat', 'Gujrat'), ('Bihar', 'Bihar'), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('Chattisgarh', 'Chattisgarh'), ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Assam', 'Assam'), ('Chandigarh', 'Chandigarh'), ('Goa', 'Goa'), ('Daman and Diu', 'Daman and Diu')], max_length=100),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('Accepted', 'Accepted'), ('Pending', 'Pending'), ('Cancel', 'Cancel'), ('On The Wey', 'On The Way'), ('Packed', 'packed')], default='pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='popular',
            name='category',
            field=models.CharField(choices=[('SH', 'Sexual health'), ('AV', 'Ayurvedic'), ('VM', 'Vitamins&Minerals'), ('MH', 'Men Health'), ('GH', 'General Health'), ('DH', 'Digestive Health'), ('OG', 'Organic'), ('AN', 'Antioxidants'), ('IH', 'Immune Health'), ('PC', 'Personal Care'), ('WH', 'Women health'), ('HS', 'Herbal, Specialty Supplements')], max_length=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('SH', 'Sexual health'), ('AV', 'Ayurvedic'), ('VM', 'Vitamins&Minerals'), ('MH', 'Men Health'), ('GH', 'General Health'), ('DH', 'Digestive Health'), ('OG', 'Organic'), ('AN', 'Antioxidants'), ('IH', 'Immune Health'), ('PC', 'Personal Care'), ('WH', 'Women health'), ('HS', 'Herbal, Specialty Supplements')], max_length=2),
        ),
        migrations.AlterField(
            model_name='product1',
            name='category',
            field=models.CharField(choices=[('SH', 'Sexual health'), ('AV', 'Ayurvedic'), ('VM', 'Vitamins&Minerals'), ('MH', 'Men Health'), ('GH', 'General Health'), ('DH', 'Digestive Health'), ('OG', 'Organic'), ('AN', 'Antioxidants'), ('IH', 'Immune Health'), ('PC', 'Personal Care'), ('WH', 'Women health'), ('HS', 'Herbal, Specialty Supplements')], max_length=2),
        ),
        migrations.AlterField(
            model_name='shopnow',
            name='category',
            field=models.CharField(choices=[('SH', 'Sexual health'), ('AV', 'Ayurvedic'), ('VM', 'Vitamins&Minerals'), ('MH', 'Men Health'), ('GH', 'General Health'), ('DH', 'Digestive Health'), ('OG', 'Organic'), ('AN', 'Antioxidants'), ('IH', 'Immune Health'), ('PC', 'Personal Care'), ('WH', 'Women health'), ('HS', 'Herbal, Specialty Supplements')], max_length=2),
        ),
        migrations.AlterField(
            model_name='specialoffer',
            name='category',
            field=models.CharField(choices=[('SH', 'Sexual health'), ('AV', 'Ayurvedic'), ('VM', 'Vitamins&Minerals'), ('MH', 'Men Health'), ('GH', 'General Health'), ('DH', 'Digestive Health'), ('OG', 'Organic'), ('AN', 'Antioxidants'), ('IH', 'Immune Health'), ('PC', 'Personal Care'), ('WH', 'Women health'), ('HS', 'Herbal, Specialty Supplements')], max_length=2),
        ),
    ]
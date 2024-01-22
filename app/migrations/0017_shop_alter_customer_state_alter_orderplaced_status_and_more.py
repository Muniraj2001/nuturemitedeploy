# Generated by Django 4.2.7 on 2023-11-20 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_blogpost_alter_customer_state_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_sale', models.BooleanField(default=False)),
                ('sale_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('image_url', models.URLField()),
            ],
        ),
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Gujrat', 'Gujrat'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Chattisgarh', 'Chattisgarh'), ('Chandigarh', 'Chandigarh'), ('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'), ('Goa', 'Goa'), ('Daman and Diu', 'Daman and Diu'), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Delhi', 'Delhi'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Haryana', 'Haryana')], max_length=100),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('Accepted', 'Accepted'), ('Pending', 'Pending'), ('On The Wey', 'On The Way'), ('Packed', 'packed'), ('Cancel', 'Cancel')], default='pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('AN', 'Antioxidants'), ('OG', 'Organic'), ('DH', 'Digestive Health'), ('AV', 'Ayurvedic'), ('PC', 'Personal Care'), ('IH', 'Immune Health'), ('VM', 'Vitamins&Minerals'), ('WH', 'Women health'), ('GH', 'General Health'), ('MH', 'Men Health'), ('SH', 'Sexual health'), ('HS', 'Herbal, Specialty Supplements')], max_length=2),
        ),
        migrations.AlterField(
            model_name='product1',
            name='category',
            field=models.CharField(choices=[('AN', 'Antioxidants'), ('OG', 'Organic'), ('DH', 'Digestive Health'), ('AV', 'Ayurvedic'), ('PC', 'Personal Care'), ('IH', 'Immune Health'), ('VM', 'Vitamins&Minerals'), ('WH', 'Women health'), ('GH', 'General Health'), ('MH', 'Men Health'), ('SH', 'Sexual health'), ('HS', 'Herbal, Specialty Supplements')], max_length=2),
        ),
        migrations.AlterField(
            model_name='specialoffer',
            name='category',
            field=models.CharField(choices=[('AN', 'Antioxidants'), ('OG', 'Organic'), ('DH', 'Digestive Health'), ('AV', 'Ayurvedic'), ('PC', 'Personal Care'), ('IH', 'Immune Health'), ('VM', 'Vitamins&Minerals'), ('WH', 'Women health'), ('GH', 'General Health'), ('MH', 'Men Health'), ('SH', 'Sexual health'), ('HS', 'Herbal, Specialty Supplements')], max_length=2),
        ),
    ]
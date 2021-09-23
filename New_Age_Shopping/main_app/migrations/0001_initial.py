# Generated by Django 3.1.3 on 2021-09-23 08:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import main_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturedSliderProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('featured_product_name', models.CharField(max_length=180)),
                ('featured_product_description', models.CharField(max_length=200)),
                ('featured_product_active', models.BooleanField(default=True)),
                ('featured_product_image', models.ImageField(upload_to=main_app.models.FeaturedSliderProduct.image_rename, verbose_name='Featured Product Image')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Level1ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('category_level1', models.CharField(help_text='Level1 category like electronics, health and beauty, sports and entertainment', max_length=150, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Level2ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('category_level2', models.CharField(help_text='s Level2 like mobiles, laptop, soap etc.', max_length=150, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=300, null=True)),
                ('category_name_level1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.level1productcategory')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('transcation_id', models.CharField(max_length=100, null=True)),
                ('complete', models.BooleanField(default=False)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductDiscount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('product_discount_active', models.BooleanField(blank=True, default=False, null=True)),
                ('product_discount_name', models.CharField(blank=True, max_length=180, null=True)),
                ('product_discount_description', models.CharField(blank=True, max_length=250, null=True)),
                ('product_discount_percentage', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('slug', models.SlugField(blank=True, max_length=300, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductInventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('product_inventory_name', models.CharField(blank=True, max_length=180, null=True)),
                ('product_inventory_quantity', models.IntegerField()),
                ('slug', models.SlugField(blank=True, max_length=300, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=20, null=True)),
                ('last_name', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.BigIntegerField(blank=True, null=True)),
                ('shipping_district', models.CharField(blank=True, max_length=200, null=True)),
                ('shipping_address', models.CharField(blank=True, max_length=200, null=True)),
                ('shipping_zip', models.CharField(blank=True, max_length=200, null=True)),
                ('payment_option', models.CharField(blank=True, max_length=200, null=True)),
                ('checkout_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Shipping Addresses',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('brand_name', models.CharField(max_length=100)),
                ('product_category_description', models.CharField(blank=True, max_length=250, null=True)),
                ('slug', models.SlugField(blank=True, max_length=300, null=True)),
                ('category_name_level2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.level2productcategory')),
            ],
            options={
                'verbose_name': 'Product Category',
                'verbose_name_plural': 'Product Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('product_name', models.CharField(max_length=500)),
                ('product_description', models.CharField(max_length=1000)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('product_availability', models.BooleanField(default=True)),
                ('product_image_src', models.ImageField(upload_to=main_app.models.Product.image_rename, verbose_name='Product Image')),
                ('slug', models.SlugField(blank=True, max_length=300, null=True)),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.productcategory')),
                ('product_discount', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_query_name='discount', to='main_app.productdiscount')),
                ('product_quantity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_query_name='quantity', to='main_app.productinventory')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=1, null=True)),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('complete', models.BooleanField(default=False)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.order')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.product')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-added_date'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, max_length=250)),
                ('comment', models.CharField(blank=True, max_length=250)),
                ('rate', models.IntegerField(default=1)),
                ('ip', models.CharField(blank=True, max_length=20)),
                ('status', models.CharField(choices=[('New', 'New'), ('True', 'True'), ('False', 'False')], default='New', max_length=10)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

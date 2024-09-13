import json
from .models import Category, Brand, Product, ProductImage

from celery import shared_task


def process_json_file(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
        for item in data:
            category, created = Category.objects.get_or_create(name=item['category_name'])
            brand, created = Brand.objects.get_or_create(name=item['brand_name'])
            product = Product(
                name=item['name'],
                description=item['description'],
                material=item.get('material'),
                code=item['code'],
                rating=item.get('rating'),
                price=item['current_price'],
                old_price=item.get('old_price'),
                off_percent=item.get('off_percent'),
                category=category,
                brand=brand,
                shop_name=item.get('shop_name'),
                link=item.get('link'),
                status=item['status'],
                colors=item.get('colors', []),
                sizes=item.get('sizes', []),
                region=item.get('region'),
                currency=item.get('currency'),
                is_active=True
            )
            product.save()


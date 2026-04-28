from decimal import Decimal

from django.core.management.base import BaseCommand

from products.models import Product


DEMO_PRODUCTS = [
    {
        'name': 'Apple iPhone 15 Pro 256GB',
        'description': 'A17 Pro 芯片，轻量化钛金属机身，120Hz ProMotion 显示屏，影像体验强。',
        'price': Decimal('7999.00'),
        'stock': 35,
        'image_url': 'https://images.unsplash.com/photo-1592750475338-74b7b21085ab?auto=format&fit=crop&w=1200&q=80',
    },
    {
        'name': 'Huawei MateBook 14 2025',
        'description': '14 英寸 2K 触控全面屏，轻薄便携，适合办公与学习。',
        'price': Decimal('6299.00'),
        'stock': 28,
        'image_url': 'https://images.unsplash.com/photo-1517336714739-489689fd1ca8?auto=format&fit=crop&w=1200&q=80',
    },
    {
        'name': 'Xiaomi Redmi K80 Pro',
        'description': '高性能旗舰芯片，电竞级散热系统，长续航快充。',
        'price': Decimal('3999.00'),
        'stock': 52,
        'image_url': 'https://images.unsplash.com/photo-1603898037225-1f5a6f4f8a6d?auto=format&fit=crop&w=1200&q=80',
    },
    {
        'name': 'Sony WH-1000XM5 降噪耳机',
        'description': '行业领先主动降噪，舒适佩戴，长续航，支持 Hi-Res。',
        'price': Decimal('2399.00'),
        'stock': 40,
        'image_url': 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?auto=format&fit=crop&w=1200&q=80',
    },
    {
        'name': 'iPad Air 11 英寸',
        'description': '轻薄高性能平板，支持手写笔，适合学习记录与创作。',
        'price': Decimal('4599.00'),
        'stock': 24,
        'image_url': 'https://images.unsplash.com/photo-1561154464-82e9adf32764?auto=format&fit=crop&w=1200&q=80',
    },
    {
        'name': 'Logitech MX Master 3S 鼠标',
        'description': '办公旗舰鼠标，静音按键，人体工学设计，多设备切换。',
        'price': Decimal('699.00'),
        'stock': 80,
        'image_url': 'https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?auto=format&fit=crop&w=1200&q=80',
    },
    {
        'name': 'Nintendo Switch OLED',
        'description': '7 英寸 OLED 屏幕，掌机与主机二合一，多场景娱乐。',
        'price': Decimal('2399.00'),
        'stock': 31,
        'image_url': 'https://images.unsplash.com/photo-1605901309584-818e25960a8f?auto=format&fit=crop&w=1200&q=80',
    },
    {
        'name': 'Kindle Paperwhite',
        'description': '高分辨率电子墨水屏，防眩光设计，阅读更专注。',
        'price': Decimal('1099.00'),
        'stock': 70,
        'image_url': 'https://images.unsplash.com/photo-1481627834876-b7833e8f5570?auto=format&fit=crop&w=1200&q=80',
    },
    {
        'name': 'Dyson V12 无线吸尘器',
        'description': '强劲吸力，多场景清洁，轻量化机身，家庭清洁高效。',
        'price': Decimal('3899.00'),
        'stock': 16,
        'image_url': 'https://images.unsplash.com/photo-1558317374-067fb5f30001?auto=format&fit=crop&w=1200&q=80',
    },
    {
        'name': 'Midea 1.5匹 变频空调',
        'description': '高效节能，静音运行，智能控温，适合卧室客厅。',
        'price': Decimal('2899.00'),
        'stock': 22,
        'image_url': 'https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?auto=format&fit=crop&w=1200&q=80',
    },
    {
        'name': 'Canon EOS R50 微单相机',
        'description': '轻便机身，自动对焦快速，支持 4K 视频拍摄。',
        'price': Decimal('5499.00'),
        'stock': 14,
        'image_url': 'https://images.unsplash.com/photo-1516035069371-29a1b244cc32?auto=format&fit=crop&w=1200&q=80',
    },
    {
        'name': 'Nike Air Max 跑步鞋',
        'description': '缓震舒适，透气鞋面，适合日常通勤与运动跑步。',
        'price': Decimal('899.00'),
        'stock': 63,
        'image_url': 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=1200&q=80',
    },
]


class Command(BaseCommand):
    help = '创建电商演示商品数据（名称/描述/价格/库存/图片）'

    def add_arguments(self, parser):
        parser.add_argument('--reset', action='store_true', help='清空现有商品后再创建演示数据')

    def handle(self, *args, **options):
        if options['reset']:
            Product.objects.all().delete()
            self.stdout.write(self.style.WARNING('已清空现有商品数据。'))

        created = 0
        for item in DEMO_PRODUCTS:
            _, is_created = Product.objects.get_or_create(
                name=item['name'],
                defaults={
                    'description': item['description'],
                    'price': item['price'],
                    'stock': item['stock'],
                    'image_url': item['image_url'],
                    'is_active': True,
                },
            )
            if is_created:
                created += 1

        self.stdout.write(self.style.SUCCESS(f'演示商品导入完成，本次新增 {created} 条。'))

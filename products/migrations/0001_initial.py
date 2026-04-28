from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='商品名称')),
                ('description', models.TextField(blank=True, verbose_name='描述')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='价格')),
                ('stock', models.PositiveIntegerField(default=0, verbose_name='库存')),
                ('image_url', models.URLField(blank=True, verbose_name='图片链接')),
                ('is_active', models.BooleanField(default=True, verbose_name='上架')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={'ordering': ['-created_at']},
        ),
    ]

from django.db import models


class Product(models.Model):
    name = models.CharField('商品名称', max_length=120)
    description = models.TextField('描述', blank=True)
    price = models.DecimalField('价格', max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField('库存', default=0)
    image_url = models.URLField('图片链接', blank=True)
    is_active = models.BooleanField('上架', default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

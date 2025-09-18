from django.db import models
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, unique=True) # Slug field for URL-friendly representation of the name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self): 
        return self.name 

class Size(models.Model):
    name = models.CharField(max_length=30) 

    def __str__(self):
        return self.name
    
class Prodct(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, unique=True)
    color = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products') # Foreign key relationship to Category , если удалить категорию, удалятся и товары этой категории, related_name делает обратную связь 
    main_image = models.ImageField(upload_to='products/main/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True) # Устанавливается при создании
    updated_at = models.DateTimeField(auto_now=True) # Обновляется при каждом сохранении

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class ProductSize(models.Model):
    product = models.ForeignKey(Prodct, on_delete=models.CASCADE, related_name='product_size') # Связь с продуктом
    size = models.ForeignKey(Size, on_delete=models.CASCADE) # Связь с размером
    stock = models.PositiveIntegerField(default=0) # Количество на складе

    # class Meta:
    #     unique_together = ('product', 'size') # Уникальность комбинации продукт-размер

    def __str__(self):
        return f"{self.product.name} - {self.size.name} (Stock: {self.stock})"
    

class ProductImage(models.Model):
    product = models.ForeignKey(Prodct, on_delete=models.CASCADE, related_name='images') # Связь с продуктом
    image = models.ImageField(upload_to='products/extra/') # Дополнительные изображения продукта

    def __str__(self):
        return f"Image for {self.product.name}"
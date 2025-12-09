from django.db import models

class Users(models.Model):
    name = models.CharField(verbose_name='Имя пользователя', max_length=20)
    surname = models.CharField('Фамилия пользователя', max_length=25)
    phone = models.CharField('Номер телефона')
    bio = models.TextField('Описание')

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
    
    def __str__(self):
        return f"{self.surname} {self.name}"


class Categories(models.Model):
    name = models.CharField('Название', max_length=20)
    description = models.CharField('Описание', max_length=100)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
    
    def __str__(self):
        return f"{self.name}"
    
class Discounts(models.Model):
    name = models.CharField('Название скидки', max_length=20)
    type = models.CharField('Тип скидки', max_length=25)
    value = models.DecimalField('Размер скидки', max_length=100, max_digits=4, decimal_places=2)
    start_date = models.DateField('Начальная дата')
    end_date = models.DateField('Конечная дата')

    class Meta:
        verbose_name = "Название скидки"
        verbose_name_plural = "Названия скидок"
        
    def __str__(self):
        return f"{self.name}"
    
class Orders(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    created_at = models.DateTimeField('Дата оформления')
    status = models.CharField('Статус', max_length=25)
    payment_method = models.CharField('Способ оплаты', max_length=20)
    customer_name = models.CharField('Имя покупателя', max_length=30)
    total_amount = models.DecimalField('Сумма заказа', max_length=1000000, max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        
    def __str__(self):
        return f"{self.id}"
    
class Products(models.Model):
    name = models.CharField('Название', max_length=30)
    description = models.CharField('Описание', max_length=100)
    ingredients = models.CharField('Состав', max_length=200)
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    price = models.DecimalField('Цена', max_length=1000000, max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
    
    def __str__(self):
        return f"{self.name}"
    
class Reviews(models.Model):
    created_at = models.DateTimeField('Дата оформления')
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    rating = models.IntegerField('Оценка')
    comment = models.TextField('Комментарий', max_length=1000)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
    
    def __str__(self):
        return f"{self.id}"
    
class Wishlists(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Избранное"
        verbose_name_plural = "Избранные"
    
    def __str__(self):
        return f"{self.id}"
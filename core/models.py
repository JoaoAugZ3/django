from django.db import models

class Seller(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    description = models.CharField(max_length=100, default='Sem detalhes', blank=False, null=False)
    delivery = models.BooleanField(default=False)
    withdrawal = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Vendedor'
        verbose_name_plural = 'Vendedores'

    def __str__(self):
        return f'{self.name}'
    
    def quant_product(self):
        return self.produtos.count()

class Product(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    observation = models.CharField(max_length=100, default='Sem mais detalhes', blank=False, null=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='produtos')
    

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return f'{self.name} - R$ {self.price}'


class Buyer(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    telephone = models.CharField(max_length=14, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False)

    class Meta:
        verbose_name = 'Comprador'
        verbose_name_plural = 'Compradores'

    def __str__(self):
        return f'{self.name} - {self.telephone}'
entrega_choices = [
    ('delivery', ' Delivery'),
    ('retirada', 'Retirada')
]
class Sale(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, related_name='pedidos')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='vendas')
    amount = models.IntegerField()
    delivery = models.CharField(max_length=100, choices=entrega_choices)


    class Meta:
        verbose_name = 'Venda'
        verbose_name_plural = 'Vendas'


    def __str__(self):
        return f'{self.id}'


    def seller(self):
        return self.product.seller

    def total_value(self):
        return f'R$ {self.product.price * self.amount}'
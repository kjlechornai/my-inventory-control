from django.db import models
from django.db.models import Sum
from support.models import Project, Requestor, Work
from main.models import Item

class ReceivedItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    date_received = models.DateField(auto_now=True)
    quantity = models.IntegerField()
    project = models.ManyToManyField(Project)

    def __str__(self):
        return self.item.title

    def total_received(self):
        return ReceivedItem.objects.filter(
            item__title=self.item).aggregate(Sum('quantity'))['quantity__sum']
        


class IssuedItem(models.Model):
    request_id = models.CharField(max_length = 50, default=1)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    issued_date = models.DateField(auto_now=True)
    quantity = models.IntegerField()
    collector = models.ForeignKey(Requestor, on_delete=models.CASCADE)
    work = models.ManyToManyField(Work)
    for_project = models.BooleanField(default=True)


    def __str__(self):
        return self.item.title
    
    def total_issued(self):
        return IssuedItem.objects.filter(
            item__title=self.item).aggregate(Sum('quantity'))['quantity__sum']
        

class BalanceItemQuantity(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Items balance quantities'        
        ordering = ['-item__item_id']

    def __str__(self):
        return self.item.title

    @property    
    def get_stock(self):
        received_qty = ReceivedItem.objects.filter(
            item__title=self.item).aggregate(Sum('quantity'))['quantity__sum']

        issued_qty = IssuedItem.objects.filter(
            item__title=self.item).aggregate(Sum('quantity'))['quantity__sum']


        if received_qty is not None and issued_qty is not None:
            return received_qty - issued_qty
        elif received_qty is not None and issued_qty is None:
            return received_qty
        elif received_qty is None and issued_qty is None:
            return 0
    

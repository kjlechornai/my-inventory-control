from django.db import models
from django.db.models import Sum
from django.shortcuts import reverse
from support.models import Location, Shelf


class Category(models.Model):
    catname = models.CharField(max_length=100)
    category_slug = models.SlugField(unique=True)

    def __str__(self):
        return self.catname

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('catname', )


class Item(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100, blank=True, null=True)
    unit = models.CharField(max_length=50, default=1)
    slug = models.SlugField(unique=True)
    location = models.ManyToManyField(Location)
    shelve_label = models.ManyToManyField(Shelf, blank=True)
    item_id = models.CharField(max_length=20, blank=True, null=True)
    category = models.ForeignKey(Category, default=1, on_delete=models.SET_DEFAULT)
    sub_category = models.CharField(max_length=50, default=1)

    class Meta:
        ordering = ('-item_id',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("main:product", kwargs={"slug": self.slug})


    def get_add_to_cart_url(self):
        return reverse("cart:add-to-cart", kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse("cart:remove-from-cart", kwargs={
            'slug': self.slug
        })

  

    
class ItemImage(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    featured = models.BooleanField(default=False)
    thumbnail = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.item.title



# CATEGORY_CHOICES = (
#     ('S', 'Shirt'),
#     ('SW', 'Sport wear'),
#     ('OW', 'Outwear')
# )

# LABEL_CHOICES = (
#     ('P', 'primary'),
#     ('S', 'secondary'),
#     ('D', 'danger')
# )

# ADDRESS_CHOICES = (
#     ('B', 'Billing'),
#     ('S', 'Shipping'),
# )


# class Item2(models.Model):
#     title = models.CharField(max_length=100)
#     price = models.FloatField()
#     discount_price = models.FloatField(blank=True, null=True)
#     category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
#     label = models.CharField(choices=LABEL_CHOICES, max_length=1)
#     slug = models.SlugField()
#     description = models.TextField()
#     image = models.ImageField()

#     def __str__(self):
#         return self.title

   


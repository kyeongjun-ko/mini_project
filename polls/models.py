from django.db import models

class StoreDB(models.Model):
    idx = models.IntegerField(default=0)
    area = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    addr1 = models.CharField(max_length=200)
    addr2 = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    open_info = models.CharField(max_length=100)
    close_info = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    target1_code = models.CharField(max_length=100)
    target1_etc = models.CharField(max_length=100)
    target2_code = models.CharField(max_length=100)
    target2_etc = models.CharField(max_length=100)
    item_code = models.CharField(max_length=100)
    item_etc = models.CharField(max_length=100)
    lat = models.CharField(max_length=100)
    lng = models.CharField(max_length=100)
    img_name = models.CharField(max_length=100)
    sup_obj = models.CharField(max_length=100)
    sup_num = models.CharField(max_length=100)
    sup_item = models.CharField(max_length=100)
    img_src = models.CharField(max_length=200)

    def __str__(self):
        return self.idx
        return self.area
        return self.name
        return self.addr1
        return self.addr2
        return self.zipcode
        return self.open_info
        return self.close_info
        return self.type
        return self.target1_code
        return self.target1_etc
        return self.target2_code
        return self.target2_etc
        return self.item_code
        return self.item_etc
        return self.lat
        return self.lng
        return self.img_name
        return self.sup_obj
        return self.sup_num
        return self.sup_item
        return self.img_src
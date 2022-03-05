from django.db import models

# 위 구문은 삭제하면 안됨.
class Question(models.Model):
    area = models.CharField(max_length=20)
    item_code = models.CharField(max_length=20)
    target2_code = models.CharField(max_length=50)
    addr2 = models.CharField(max_length=200)
    lng = models.CharField(max_length=200)
    addr1 = models.CharField(max_length=200)
    open_info = models.CharField(max_length=200)
    target2_etc = models.CharField(max_length=200)
    type = models.IntegerField(default=0)
    close_info = models.CharField(max_length=200)
    zipcode = models.IntegerField(default=0)
    img_name = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    target1_code = models.CharField(max_length=200)
    idx = models.CharField(max_length=50)
    item_etc = models.CharField(max_length=200)
    lat = models.CharField(max_length=200)


    def __str__(self):
        return self.area
        return self.item_code
        return self.target2_code
        return self.addr2
        return self.lng
        return self.addr1
        return self.open_info
        return self.target2_etc
        return self.type
        return self.close_info
        return self.zipcode
        return self.img_name
        return self.name
        return self.target1_code
        return self.idx
        return self.item_etc
        return self.lat

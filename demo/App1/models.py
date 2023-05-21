from django.db import models


class SocietyList(models.Model):
    societyName = models.CharField(max_length=122,  unique=True)
    regno = models.CharField(max_length=122)
    address = models.TextField()
    date_add_society = models.DateField()

    def __str__(self):
        return self.societyName
    
class MembersList(models.Model):
    societyName = models.CharField(max_length=122)
    memberName = models.CharField(max_length=122,  unique=True)
    flatno = models.CharField(max_length=122)
    openingBalance = models.IntegerField()
    closingBalance = models.IntegerField()
    date_add_member = models.DateField()

    def __str__(self):
        return self.memberName
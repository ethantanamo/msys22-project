from unicodedata import name
from django.db import models
from django.utils import timezone

class Position(models.Model):
    name = models.CharField(max_length = 300)
    
    objects = models.Manager()

    def getName(self):
        return (self.name)

    def __str__(self):
        return ('Position Name: ' + str(self.name))

class Candidate(models.Model):
    first_name = models.CharField(max_length = 300)
    last_name = models.CharField(max_length = 300)
    nickname = models.CharField(max_length = 300)
    # slogan = models.CharField(max_length = 300) ***must be OPTIONAL*** 
    # position_id = models.CharField(max_length = 300) ***must be foreign key*** must come from position model
    objects = models.Manager()

    def getFirstName(self):
        return self.first_name
    def getLastName(self):
        return self.last_name
    def getNickname(self):
        return self.nickname
    # def getSlogan(self):
    #     return self.slogan


    def __str__(self):
        return str(self.pk) + " " + str(self.sku) + ": " + str(self.brand) + ", " + str(self.mouth_size) + ", " + str(self.size) + ", " + str(self.color) + ", supplied by " + str(self.supplied_by) + ", " + str(self.cost) + ": " + str(self.current_quantity)



class User(models.Model):
    username = models.CharField(max_length = 300)
    password = models.CharField(max_length = 300)
    first_name = models.CharField(max_length = 300)
    last_name = models.CharField(max_length = 300)
    birthday = models.DateTimeField(blank=True, null=True)
    sex = models.CharField(max_length = 300)

    def getUsername(self):
        return (self.username)

    def getPassword(self):
        return (self.password)

    def getFirstName(self):
        return (self.first_name)

    def getLastName(self):
        return (self.last_name)
    
    def getBirthday(self):
        return (self.birthday)

    def getSex(self):
        return (self.sex)

    def __str__(self):
        return ('pk: ' + str('PK HHAH') + ' ' + str(self.username)+ ', ' + str(self.first_name) + ' ' + str(self.last_name) + ', ' + str(self.birthday) + ', ' + str(self.sex))

class Vote(models.Model):
   ## user_id = self.position_id must come from candidate mode 
   candidate_id = models.ForeignKey(Candidate, on_delete=models.CASCEDE)
   commentme = models.CharField(max_length = 300)
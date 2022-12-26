from tortoise.models import Model
from tortoise import fields

class Student(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    club = fields.ManyToManyField('models.Club', related_name='club')
    school = fields.ForeignKeyField('models.School', related_name='school')
    
    def __str__(self):
        return self.name
    
class Club(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class School(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    
    def __str__(self):
        return self.name
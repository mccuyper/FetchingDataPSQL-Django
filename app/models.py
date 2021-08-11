from django.db import models

class FetchIt(models.Model):
    ''' every value should be the same as your column name in the DB 
        for instance if your table has column id you shoud 
        create id = models.IntegerField(...) '''
    user_id = models.IntegerField(primary_key=True)
    d_name = models.CharField(max_length=254)
    direction = models.CharField(max_length=254)
    created_on = models.DateTimeField()  
    duration = models.IntegerField()

    # https://docs.djangoproject.com/en/3.2/ref/models/options/#db-table
    class Meta:
        db_table = "cdr" # name of your table in DB 
    
    # optional for represantation 
    def __str__(self):
        return self.d_name
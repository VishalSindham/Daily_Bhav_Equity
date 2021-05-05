from django.db import models

# Create your models here.

class Bhav(models.Model):
    SC_CODE      = models.IntegerField(primary_key=True)
    SC_NAME      = models.CharField(max_length=100)
    SC_GROUP     = models.CharField(max_length=10)
    SC_TYPE      = models.CharField(max_length=10)
    OPEN         = models.CharField(max_length=100)
    HIGH         = models.CharField(max_length=100)
    LOW          = models.CharField(max_length=100)
    CLOSE        = models.CharField(max_length=100)
    LAST         = models.CharField(max_length=100) 
    PREVCLOSE    = models.CharField(max_length=100)
    NO_TRADES    = models.CharField(max_length=100)
    NO_OF_SHRS   = models.CharField(max_length=100)
    NET_TURNOV   = models.CharField(max_length=100)
    TDCLOINDI    = models.CharField(max_length=100)
    """SC_CODE,
    SC_NAME,
    SC_GROUP,
    SC_TYPE,
    OPEN,
    HIGH,
    LOW,
    CLOSE,
    LAST,
    PREVCLOSE,
    NO_TRADES,
    NO_OF_SHRS,
    NET_TURNOV,
    TDCLOINDI
"""
from django.db import models

class MarketItem(models.Model):
    m_gu_name = models.CharField(max_length=100)
    m_type_code = models.CharField(max_length=10)
    a_name = models.CharField(max_length=100)
    a_price = models.IntegerField()
    p_seq = models.IntegerField()
    m_type_name = models.CharField(max_length=100)
    a_unit = models.CharField(max_length=100, null=True, blank=True)
    m_gu_code = models.CharField(max_length=10)
    add_col = models.CharField(max_length=100, null=True, blank=True)
    m_name = models.CharField(max_length=100)
    p_date = models.DateField()
    p_year_month = models.CharField(max_length=10)
    a_seq = models.IntegerField()
    m_seq = models.IntegerField()

from django.db import models

# Create your models here.
class Goods(models.Model):
    """商品モデル"""
    class Meta:
        #テーブル名を定義
        db_table = 'goods'

    #テーブルのカラムに対応するフィールドを定義
    goods_name = models.CharField(verbose_name='商品名', max_length=255)
    price = models.IntegerField(verbose_name='価格', null=True, blank=True)
    categ = models.CharField(verbose_name='カテゴリ名',max_length=255)

    def __str__(self):
        return self.goods_name
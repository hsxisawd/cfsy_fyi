from django.db import models

# Create your models here.

class fyi(models.Model):
      E_language=models.CharField('语言简写',max_length=50)
      C_language=models.CharField('语言',max_length=70)
      def toDict(self):
          return {'E':self.E_language,'C':self.C_language}
      class Meta:
         db_table = "fyi_language"  # 更改表名
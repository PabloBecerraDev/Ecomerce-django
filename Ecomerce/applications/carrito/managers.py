from django.db import models


class CarritoManager(models.Manager):

    def getCartByUser(self, UserId):
        try:
            return self.get(user = UserId)
        except self.model.DoesNotExist:
            return None
        

class ItemCarritoManager(models.Manager):
    pass
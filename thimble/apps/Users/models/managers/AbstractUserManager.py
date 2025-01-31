from django.db import models

class AbstractUserManager(models.Manager):

	def update_following(self, pk, increment):
		try:
			if increment:
				self.filter(id=pk).update(following=models.F("following") + 1)
			else:
				self.filter(id=pk).update(following=models.F("following") - 1)
		except:
			raise

	def update_followers(self, pk, increment):
		try:
			if increment:
				self.filter(id=pk).update(followers=models.F("followers") + 1)
			else:
				self.filter(id=pk).update(followers=models.F("followers") - 1)
		except:
			raise
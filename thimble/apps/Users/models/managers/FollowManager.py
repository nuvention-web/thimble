from django.db import models

class FollowManager(models.Manager):
	
	def get_is_following(self, follower, followee):
		try:
			followee_object_id = followee.pk
			followee_content_type = followee.get_ct()
			follower_object_id = follower.pk
			follower_content_type = follower.get_ct()

			row = self.filter(followee_object_id=followee_object_id, 
							  followee_content_type=followee_content_type, 
							  follower_object_id=follower_object_id, 
							  follower_content_type=follower_content_type)
			
			if len(row) == 0:
				return False
		except:
			raise
		return True

	def get_following(self, follower):
		try:
			follower_object_id = follower.pk
			follower_content_type = follower.get_ct()
			rows = self.filter(follower_content_type=follower_content_type, follower_object_id=follower_object_id).values_list('followee_object_id', flat=True)
			if len(rows) == 0:
				return None
			return rows
		except:
			raise
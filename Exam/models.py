from django.db import models

class Resume(models.Model):
    name = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='photos/')
    skills = models.CharField(max_length=255) # bu yerga qanaqa ishlarni bilasiz oshalrni yozasiz
    aboutme = models.TextField()
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    language = models.CharField(max_length=355)
    follow_me_on_facebook = models.CharField(max_length=255)
    follow_me_on_twitter = models.CharField(max_length=255)
    follow_me_on_google = models.CharField(max_length=255)
    follow_me_on_instagram = models.CharField(max_length=255)
    def save(self, *args, **kwargs):
        if self.pk:
            deleted_count, _ = Resume.objects.filter(user=self.user).exclude(pk=self.pk).delete()

        super().save(*args, **kwargs)




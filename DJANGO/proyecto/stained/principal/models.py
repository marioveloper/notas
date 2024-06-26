from django.db import models
from django.contrib.auth.models import User
from .utils import generate_ref_code, generate_rank
import datetime
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    code = models.CharField(max_length=12, blank=True)
    recommended_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='ref_by')
    updated = models.DateTimeField(default=datetime.datetime.now())
    created = models.DateTimeField(default=datetime.datetime.now())
    rank = models.CharField(max_length=20, blank=True, default='Sin rango')
    wallet = models.CharField(max_length=200, blank=True)
    referrals = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    f_inicio = models.DateTimeField(default=datetime.datetime.now())
    days = models.IntegerField(default=0)
    #f_fin = models.DateTimeField(default=(datetime.datetime.now()+datetime.timedelta(days=30)))
    active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}-{self.code}"

    def get_recommened_profiles(self):
        qs = Profile.objects.all()
        my_recs = []
        for profile in qs:
            profile.set_days()
            if profile.recommended_by == self.user and profile.active:
                my_recs.append(profile)
        return my_recs

    def save(self, *args, **kwargs):
        if self.code == "":
            code = generate_ref_code()
            self.code = code
            self.rank = 'Sin rango'
        super().save(*args, **kwargs)

    def set_referrals(self):
        qs = Profile.objects.all()
        iterator = 0
        for profile in qs:
            if profile.recommended_by == self.user and profile.active:
                iterator+=1
        self.referrals = iterator
        self.save()

    def set_rank(self):
        referrals = self.referrals
        self.rank = generate_rank(referrals)
        self.save()

    def set_points(self):
        self.points = self.referrals*30
        self.save()

    def set_days(self):
        f_inicio = self.f_inicio
        f_fin = f_inicio + datetime.timedelta(days=31)
        ahora = datetime.datetime.now(tz = datetime.timezone.utc)
        days = f_fin-ahora
        days = int(str(days).split()[0])
        self.days = days
        self.save()

from django.db import models
from django.contrib import auth
from django.db.models import Sum


class MasangaUserManager(auth.models.UserManager):
    def verified_users(self):
        from allauth.account.models import EmailAddress
        not_veryfied = EmailAddress.objects.filter(verified=False)\
            .values_list('user', flat=True)
        return self.model.objects.filter(is_active=True)\
            .exclude(id__in=not_veryfied)


class User(auth.models.AbstractUser):
    USERNAME_FIELD = 'username'

    is_public = models.BooleanField('Info public?', default=False)

    newsletter = models.BooleanField('Newsletter?', default=False)

    subscribed = models.BooleanField('Subscribed to emails?', default=True)

    stripe_customer_id = models.CharField('Stripe Customer Id', max_length=200,
                                          null=True, blank=True, default=None,
                                          db_index=True)

    greeted = models.BooleanField('Greeted?', default=False)

    objects = MasangaUserManager()

    @property
    def is_runner(self):
        return self.runs.all().exists() or \
            self.sponsorships_recieved.all().exists() or \
            self.challenges_recieved.all().exists()

    @property
    def is_sponsor(self):
        return self.sponsorships_given.all().exists() or \
            self.challenges_given.all().exists()

    @property
    def amount_earned(self):
        spship_amount = self.sponsorships_recieved.all()\
            .aggregate(a_sum=Sum('amount_paid'))['a_sum'] or 0
        challenges_amount = self.challenges_recieved.filter(status='paid')\
            .aggregate(a_sum=Sum('amount'))['a_sum'] or 0
        return spship_amount + challenges_amount

    @property
    def amount_donated(self):
        given_spships = self.sponsorships_given.all()
        spship_amount = sum([sp.amount_paid for sp in given_spships])
        challenges_amount = self.challenges_given.filter(status='paid')\
            .aggregate(a_sum=Sum('amount'))['a_sum'] or 0
        return spship_amount + challenges_amount

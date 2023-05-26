from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class SamaajMemberMaster(models.Model):
    """
    Table for member of the samaaj whose,
    data will be stored.
    """

    first_name = models.CharField(_("First Name"), max_length=256)
    middle_name = models.CharField(_("Father / Husband Name"), max_length=256)
    mother_name = models.CharField(_("Mothers Name"), max_length=256)
    last_name = models.CharField(_("Last Name"), max_length=256)
    # recent_photo = models.ImageField(_("Recent Photo"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def full_name(self) -> str:
        return (
            f"{self.first_name} {self.middle_name} {self.mother_name} {self.last_name}"
        )

    def __str__(self) -> str:
        return (
            f"{self.first_name} {self.middle_name} {self.mother_name} {self.last_name}"
        )


class SamaajMemberMosaadMaster(models.Model):
    """
    Mosaad of samaaj member will be stored here.

    """

    samaaj_member = models.ForeignKey(SamaajMemberMaster, on_delete=models.PROTECT)
    name = models.CharField(_("Mosaad Name"), max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name} - mosaad of {self.samaaj_member.full_name}"


class SamaajMemberMobileNumberMaster(models.Model):
    """
    Mobile numbers of Samaaj Members will be stored here.
    The whatsapp number will be identified by boolean
    is_whatsapp.

    """

    samaaj_member = models.ForeignKey(SamaajMemberMaster, on_delete=models.PROTECT)
    mobile_number = models.CharField(_("Mobile Number"), max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.mobile_number} - mobile number of {self.samaaj_member.full_name}"


class SamaajMemberEmailAddressMaster(models.Model):
    """
    Email Address of Samaaj Members will be stored here.
    """

    samaaj_member = models.ForeignKey(SamaajMemberMaster, on_delete=models.PROTECT)
    email_id = models.EmailField(_("Email Address"), max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.email_id} - Email Address of {self.samaaj_member.full_name}"

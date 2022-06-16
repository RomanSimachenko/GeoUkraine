from django.db import models
from django.utils.translation import gettext as _


class Universities(models.Model):
    """Universities"""
    id = models.PositiveBigIntegerField(_("id"), primary_key=True, unique=True)
    parent_id = models.PositiveBigIntegerField(
        _("parent ID"), null=True, blank=True)
    place_id = models.CharField(_("place id"), max_length=200, null=True, blank=True)

    name = models.CharField(_("name"), max_length=1000)
    short_name = models.CharField(
        _("short name"), max_length=300, null=True, blank=True)
    name_en = models.CharField(
        _("name en"), max_length=1000, null=True, blank=True)

    phone = models.CharField(_("phone"), max_length=16)
    email = models.EmailField(_("email"))
    site = models.CharField(_("site"), max_length=200, null=True, blank=True)

    address = models.CharField(_("address"), max_length=400)
    address_u = models.CharField(
        _("address u"), max_length=400, null=True, blank=True)
    is_from_crimea = models.CharField(_("is from crimea"), default="ні", max_length=5)

    type_name = models.CharField(_("type name"), max_length=100)
    financing = models.CharField(
        _("financing"), max_length=100, null=True, blank=True)
    governance = models.CharField(
        _("governance"), max_length=200, null=True, blank=True)

    registration_year = models.PositiveIntegerField(
        _("registration year"), null=True, blank=True)
    edrpou = models.PositiveIntegerField(_("edrpou"))

    post_index = models.PositiveIntegerField(_("post index"))
    post_index_u = models.PositiveIntegerField(
        _("post index u"), null=True, blank=True)

    koatuu_id = models.PositiveIntegerField(_("koatuu id"))
    koatuu_id_u = models.PositiveIntegerField(
        _("koatuu id u"), null=True, blank=True)

    region_name = models.CharField(_("region name"), max_length=200)
    region_name_u = models.CharField(
        _("region name u"), max_length=200, null=True, blank=True)

    koatuu_name = models.CharField(_("koatuu name"), max_length=100)
    koatuu_name_u = models.CharField(
        _("koatuu name u"), max_length=100, null=True, blank=True)

    director_post = models.CharField(
        _("director post"), max_length=100, null=True, blank=True)
    director_fio = models.CharField(
        _("director fio"), max_length=200, null=True, blank=True)

    close_date = models.CharField(_("close date"), null=True, blank=True, max_length=30)
    primitki = models.TextField(_("primitki"), null=True, blank=True)

    lat = models.FloatField(_("latitude"))
    lng = models.FloatField(_("longitude"))

    def __str__(self) -> str:
        return f"{self.id} - {self.name}"

    class Meta:
        ordering = ('id',)
        verbose_name = "university"
        verbose_name_plural = "universities"


class Regions(models.Model):
    id = models.PositiveBigIntegerField(_("ID"), primary_key=True, unique=True)
    name = models.CharField(_("name"), max_length=500)
    universities = models.ManyToManyField(Universities)

    def __str__(self) -> str:
        return f"{self.id}: {self.name}"

    class Meta:
        ordering = ('id',)
        verbose_name = "region"
        verbose_name_plural = "regions"

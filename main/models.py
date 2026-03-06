from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions


def staff_photo_dimensions(photo):
    w, h = get_image_dimensions(photo)

    if not photo:
        raise ValidationError('Rasmni kiriting!')

    else:
        if w / h != 0.75:
            raise ValidationError("Nisbati 3x4 bo'lgan rasmni kiriting!")


'''
class MakeSingleModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(MakeSingleModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj
        
'''


class StaffModel(models.Model):  # DONE!
    main_title = models.CharField('Ismi ', max_length=64, help_text="Hodimning ismi")
    photo = models.ImageField('Foto rasmi ', upload_to="Hodimlar", validators=[staff_photo_dimensions],
                              help_text="Hodimning foto rasmi (o'lcahmi 3x4 nisbatda bo'lgan rasmni kiriting)")
    title = models.CharField('Vazifasi ', max_length=64, help_text="Hodimning vazifasi")
    info = models.TextField("Ma'lumot ", blank=True, null=True, help_text="Hodim haqida ma'lumot yoki habar")
    twitter = models.URLField('Twitter linki ', max_length=200, blank=True, null=True,
                              help_text="Hodimning twitterdagi profilidagi linki mavjud bo'lmasa bo'sh qoldiring")
    facebook = models.URLField('Facebook linki ', max_length=200, blank=True, null=True,
                               help_text="Hodimning facebookdagi profilidagi linki mavjud bo'lmasa bo'sh qoldiring")
    instagram = models.URLField('Instagram linki ', max_length=200, blank=True, null=True,
                                help_text="Hodimning instagramdagi profilidagi linki mavjud bo'lmasa bo'sh qoldiring")
    linkedin_box = models.URLField('linkedin-box linki ', max_length=200, blank=True, null=True,
                                   help_text="Hodimning linkedin_box profilidagi linki mavjud bo'lmasa bo'sh qoldiring")

    created_at = models.DateTimeField('Kiritilgan vaqti', auto_now_add=True, null=True)
    updated_at = models.DateTimeField("O'zgartirilgan vaqti", auto_now=True, null=True)

    # admin_object = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return ""

    class Meta:
        verbose_name = "Hodimlar"
        verbose_name_plural = "Hodimlar"


class NewsModel(models.Model):  # DONE!
    image = models.ImageField('Foto rasmi ', upload_to="Yangiliklar", help_text="Yangiliklardagi rasm")
    title = models.CharField('Yangiliklar nomi ', max_length=45, help_text="Yangilikdagi mavzuning nomi")
    message = models.TextField('Yangiliklardagi habar ', help_text="Yangilikdagi o'zgarishlardagi habarlar")
    created_at = models.DateTimeField('Kiritilgan vaqti', auto_now_add=True, null=True)
    updated_at = models.DateTimeField("O'zgartirilgan vaqti", auto_now=True, null=True)

    def __str__(self):
        return ""

    class Meta:
        verbose_name = "Yangiliklar"
        verbose_name_plural = "Yangiliklar"


class GalaryModel(models.Model):  # DONE 100%
    photo = models.ImageField('Foto rasmi ', upload_to="Rasmlar",
                              help_text="Gallereyadagi rasm (Bolalar rasmi, Bog'chaning rasmi ...)")
    main_title = models.CharField('Gallereya nomi ', blank=False, max_length=32,
                                  help_text="Gallereyadagi assosiy mavzuning nomi")
    title = models.CharField("Gallereya ma'lumoti ", max_length=32, null=True, blank=True,
                             help_text="Gallereydagi ma'lumot (Gallereyadagi mavzu lekin assosiysi emas)")
    message = models.TextField('Gallereya habari ', blank=True, null=True,
                               help_text="Gallereyadagi habarlar (Gallereyada ma'lumotni yozmasez, bo'sh qoldiring)")
    created_at = models.DateTimeField('Kiritilgan vaqti', auto_now_add=True, null=True)
    updated_at = models.DateTimeField("O'zgartirilgan vaqti", auto_now=True, null=True)

    def __str__(self):
        return ""

    class Meta:
        verbose_name = "Gallereya"
        verbose_name_plural = "Gallereya"


class ContactModel(models.Model):  # DONE! 100%
    location = models.TextField('Manzil (address) ', help_text="Bog'chaning manzili")
    email = models.EmailField('Email manzil ', help_text="Bog'chaning emaili")
    contact_num = models.CharField('Kontakt raqam ', max_length=32,
                                   help_text="Bog'chaning kontakt raqami (Aloqaga kirib bo'ladigan raqam)")
    twitter = models.URLField("Twitter linki ", max_length=200, blank=True, null=True,
                              help_text="Bog'chaning twitterdagi gruppaning linki mavjud bo'lmasa bo'sh qoldiring")
    facebook = models.URLField('Facebook linki ', max_length=200, blank=True, null=True,
                               help_text="Bog'chaning facebookdagi gruppaning linki mavjud bo'lmasa bo'sh qoldiring")
    instagram = models.URLField('Instagram linki ', max_length=200, blank=True, null=True,
                                help_text="Bog'chaning instagramdagi gruppaning linki mavjud bo'lmasa bo'sh qoldiring")
    skype = models.URLField('Skype linki ', max_length=200, blank=True, null=True,
                            help_text="Bog'chaning skype dagi gruppaning linki mavjud bo'lmasa bo'sh qoldiring")
    linkedin_box = models.URLField('linkedin-box linki ', max_length=200, blank=True, null=True, help_text=
    "Bog'chaning linkedin_box dagi gruppaning linki mavjud bo'lmasa bo'sh qoldiring")

    updated_at = models.DateTimeField("O'zgartirilgan vaqti", auto_now=True, null=True)

    def __str__(self):
        return ""

    class Meta:
        verbose_name = "Kontakt"
        verbose_name_plural = "Kontakt"


class BannerModel(models.Model):
    title = models.CharField('Bannerning nomi ', max_length=48, null=True,
                             help_text="Bannerdagi mavzu yoki uning nomi")  # APPROX 48
    message = models.TextField("Bannerdagi ma'lumot ", max_length=216, null=True, blank=True,
                               help_text="Bannerdagi ma'lumot mavjud bo'lmasa bo'sh qoldiring")

    updated_at = models.DateTimeField("O'zgartirilgan vaqti", auto_now=True, null=True)

    def __str__(self):
        return ""

    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = "Banner"


class Customer(models.Model):  # it is not ready yet totally but we can get an answer!!
    name = models.CharField('Ismi ', max_length=120, help_text="Habar yuboruvchining ismi")
    phone_number = models.CharField('Telefon raqami ', max_length=13, help_text="Habar yuboruvchining telefon raqami")
    message = models.TextField('Habari ', max_length=1500, help_text="Habar yuboruvchining habari (yuborgan ma'lumoti)")
    # models.CharField('Message ', max_length=1500)
    created_at = models.DateTimeField('Kiritilgan vaqti', auto_now_add=True, null=True)

    def __str__(self):
        return ""

    class Meta:
        verbose_name = "Habarlar"
        verbose_name_plural = "Habarlar"

# ALL OF THEM AT THE ABOVE GET METHOD

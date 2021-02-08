from django.db import models, transaction
from django.contrib.auth.models import AbstractUser, Group, UserManager
from django.core.validators import RegexValidator


class Role(models.Model):
    name = models.CharField(max_length=36, default="Пользователь", blank=False, null=False, unique=True, verbose_name="Наименование")

    class Meta:
        verbose_name = "Роль"
        verbose_name_plural = "Роли"
        constraints = [
            models.UniqueConstraint(fields=["name"], name="role_name_uniq")
        ]


class Account(AbstractUser):
    objects = UserManager()
    phone_regex = RegexValidator(regex=r'^\+?7?\d{9,15}$',
                                 message="Телефонный номер должен иметь формат: '+7 999 999 9999'.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    first_name = models.CharField(verbose_name='Имя', max_length=50, null=True, blank=True)
    last_name = models.CharField(verbose_name='Фамилия', max_length=50, null=True, blank=True)
    middle_name = models.CharField(verbose_name='Отчество', max_length=50, null=True, blank=True)
    phone = models.CharField(verbose_name='Телефон', max_length=50, null=True, blank=True)
    birthday = models.DateField(verbose_name='День рождения', null=True, blank=True)
    birthday_changed = models.BooleanField(verbose_name='Пользователь сменил день рождения', default=False)
    reset_token = models.CharField(verbose_name='Ключ сброса пароля', max_length=50, null=True, blank=True)
    role = models.ForeignKey(Role, to_field='name', default="Пользователь", verbose_name='Уровень', null=True, blank=True, on_delete=models.SET_NULL)
    email = models.EmailField(max_length=255, verbose_name='E-mail', blank=False, unique=True)

    class Meta :
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    @transaction.atomic
    def save(self, *args, **kwargs):
        if not Role.objects.filter(name="Пользователь").exists():
            Role.objects.create(name="Пользователь")
        return super(Account, self).save(*args, **kwargs)


    def __str__(self) :
        return self.email

    # def send_reset_email(self) :
    #     subject = ''
    #     self.reset_token = PasswordResetTokenGenerator().make_token(self)
    #     self.save()
    #     email_message = EmailMultiAlternatives(subject, '', settings.EMAIL_HOST_FROM, [self.email])
    #
    #     html_email = loader.render_to_string('reset_email_template.html',
    #                                          {'host' : settings.HOST, 'token' : self.reset_token})
    #     email_message.attach_alternative(html_email, 'text/html')
    #     email_message.send()

class Favorites(models.Model):
    profile = models.ForeignKey(Account, verbose_name='Пользователь', on_delete=models.CASCADE)

    offers = models.ManyToManyField('board.SaleProduct', verbose_name='Объявление')

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'

    def __str__(self):
        return self.profile.email



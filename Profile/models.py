from django.db import models
from enum import Enum


class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"


class UserProfile(models.Model):
    # Personal Information
    first_name = models.CharField(max_length=255)  # نام (اجباری)
    last_name = models.CharField(max_length=255)  # نام خانوادگی (اجباری)
    national_code = models.CharField(max_length=10, unique=True)  # کد ملی (اجباری)
    gender = models.CharField(
        max_length=6,
        choices=[(tag.name, tag.value) for tag in Gender],
        blank=True,
        null=True
    )
    passport_number = models.CharField(max_length=50, blank=True, null=True)  # شماره پاسپورت (اختیاری)
    passport_expiry_date = models.DateField(blank=True, null=True)  # تاریخ انقضای پاسپورت (اختیاری)
    is_foreign = models.BooleanField(default=False)  # خارجی هست یا نه (اختیاری)
    date_of_birth = models.DateField(blank=True, null=True)  # تاریخ تولد (اختیاری)

    # Contact Information
    landline_number = models.CharField(max_length=15, blank=True, null=True)  # شماره تلفن ثابت (اختیاری)
    mobile_number = models.CharField(max_length=15)  # شماره موبایل (اجباری)
    address = models.TextField(blank=True, null=True)  # آدرس (اختیاری)

    # Profile Picture
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)  # عکس پرسنلی (اختیاری)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class UserBankInfo(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='bank_info')  # ارتباط یک به یک با پروفایل کاربر

    # Banking Information
    card_number = models.CharField(max_length=16)  # شماره کارت (اجباری)
    account_number = models.CharField(max_length=20, blank=True, null=True)  # شماره حساب (اختیاری)
    iban = models.CharField(max_length=24, blank=True, null=True)  # شماره شبا (اختیاری)

    def __str__(self):
        return f"Bank Info for {self.user.national_code} {self.user.last_name} {self.card_number}"

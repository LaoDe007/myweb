from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from web01 import models
from web01.utils.bootstrap import BootStrapModelForm
from web01.utils.encrypt import md5


class AdminModelForm(BootStrapModelForm):
    # render_value=True 输入密码不一致之后会不会消失
    confirm_password = forms.CharField(label="确认密码",
                                       widget=forms.PasswordInput(render_value=True)
                                       )

    class Meta:
        model = models.Admin
        fields = "__all__"
        widgets = {
            "password": forms.PasswordInput(render_value=True),
        }

    def clean_password(self):
        # 返回什么，此字段以后保存到数据库就是什么
        pwd = self.cleaned_data.get("password")
        return md5(pwd)

    def clean_confirm_password(self):
        # print(self.cleaned_data)
        # 已经是加密完的密码了
        pwd = self.cleaned_data.get("password")
        confirm = md5(self.cleaned_data.get("confirm_password"))
        if confirm != pwd:
            raise ValidationError("密码不一致")

        # 返回什么，此字段以后保存到数据库就是什么
        return confirm


class AdminEditModelForm(BootStrapModelForm):
    class Meta:
        model = models.Admin
        fields = ['username']


class AdminResetModelForm(BootStrapModelForm):
    confirm_password = forms.CharField(label="确认密码",
                                       widget=forms.PasswordInput(render_value=True)
                                       )

    class Meta:
        model = models.Admin
        fields = ['password', 'confirm_password']
        widgets = {
            "password": forms.PasswordInput(render_value=True),
        }

    def clean_password(self):
        # 返回什么，此字段以后保存到数据库就是什么
        pwd = self.cleaned_data.get("password")
        md5_pwd = md5(pwd)

        # 数据库校验，看当前密码和新输入的密码是否一致
        exists = models.Admin.objects.filter(id=self.instance.pk, password=md5_pwd).exists()
        if exists:
            raise ValidationError("密码不能与之前的一致")
        return md5_pwd

    def clean_confirm_password(self):
        # print(self.cleaned_data)
        # 已经是加密完的密码了
        pwd = self.cleaned_data.get("password")
        confirm = md5(self.cleaned_data.get("confirm_password"))
        if confirm != pwd:
            raise ValidationError("密码不一致")

        # 返回什么，此字段以后保存到数据库就是什么
        return confirm


class InventoryDataModelForm(BootStrapModelForm):
    # part_name = forms.CharField(label="零件名称", disabled=True)

    class Meta:
        model = models.InventoryData
        fields = ["plant_code", "part_code", "person_purchase", "store_warning", "online_warning", "tpl_name"]



from django.db import models


# Create your models here.
class Admin(models.Model):
    """管理员"""
    username = models.CharField(verbose_name='用户名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=64)


class ThirdPartyLogisticsPartsData(models.Model):
    # def __str__(self):
    #     return self.name
    """三方物流表"""
    universal_choices = (
        (0, "非通用件"),
        (1, "通用件"),
    )
    part_universal = models.SmallIntegerField(verbose_name='通用件', choices=universal_choices)
    identify_code = models.CharField(verbose_name='识别码(工厂+供应商代码+零件号)', max_length=32)
    part_code = models.CharField(verbose_name='零件代号', max_length=24)
    part_name = models.CharField(verbose_name='零件名称', max_length=24)
    plant_code = models.CharField(verbose_name='工厂代码', max_length=16)
    supply_code = models.CharField(verbose_name='供应商代码', max_length=16)
    supply_name = models.CharField(verbose_name='供应商名称', max_length=16)
    person_purchase = models.CharField(verbose_name='筹措员', max_length=16)
    tpl_code = models.CharField(verbose_name='三方物流代码', max_length=16)
    tpl_name = models.CharField(verbose_name='三方物流名称', max_length=32)
    parts_num = models.BigIntegerField(verbose_name="库存数量", null=True, default=None)


class FactoryPartsData(models.Model):
    """工厂零件信息表"""
    universal_choices = (
        (0, "非通用件"),
        (1, "通用件"),
    )
    part_universal = models.SmallIntegerField(verbose_name='通用件', choices=universal_choices)
    identify_code = models.CharField(verbose_name='识别码(工厂+供应商代码+零件号)', max_length=32)
    part_code = models.CharField(verbose_name='零件代号', max_length=24, default=None)
    part_name = models.CharField(verbose_name='零件名称', max_length=24, default=None)
    plant_code = models.CharField(verbose_name='工厂代码', max_length=16, default=None)
    supply_code = models.CharField(verbose_name='供应商代码', max_length=16, default=None)
    supply_name = models.CharField(verbose_name='供应商名称', max_length=16, default=None)
    person_purchase = models.CharField(verbose_name='筹措员', max_length=16, default=None)
    tpl_code = models.CharField(verbose_name='三方物流代码', max_length=16, default=None)
    tpl_name = models.CharField(verbose_name='三方物流名称', max_length=32, default=None)
    # parts_loci = models.BigIntegerField(verbose_name="3PL库存", null=True, default=None)
    online_stock = models.BigIntegerField(verbose_name="在线需求", null=True, default=None)
    require_max = models.BigIntegerField(verbose_name="MAX日需求", null=True, default=None)
    require_one = models.BigIntegerField(verbose_name="Day1需求", null=True, default=None)
    require_two = models.BigIntegerField(verbose_name="Day2需求", null=True, default=None)
    require_three = models.BigIntegerField(verbose_name="Day3需求", null=True, default=None)
    require_four = models.BigIntegerField(verbose_name="Day4需求", null=True, default=None)
    require_five = models.BigIntegerField(verbose_name="Day5需求", null=True, default=None)
    require_six = models.BigIntegerField(verbose_name="Day6需求", null=True, default=None)
    require_seven = models.BigIntegerField(verbose_name="Day7需求", null=True, default=None)


class InventoryData(models.Model):
    """库存报警表"""
    store_warning = models.CharField(verbose_name='库存报警', max_length=64, default=None)
    online_warning = models.CharField(verbose_name='在线报警', max_length=64, default=None)
    days_store = models.CharField(verbose_name='可持续天数', max_length=64, default=None)

    universal_choices = (
        (0, "非通用件"),
        (1, "通用件"),
    )
    part_universal = models.SmallIntegerField(verbose_name='通用件', choices=universal_choices)
    identify_code = models.CharField(verbose_name='识别码(工厂+供应商代码+零件号)', max_length=32)
    part_code = models.CharField(verbose_name='零件号', max_length=64)
    part_name = models.CharField(verbose_name='零件名称', max_length=64)
    plant_code = models.CharField(verbose_name='工厂代码', max_length=16)
    supply_name = models.CharField(verbose_name='供应商名称', max_length=64)
    supply_code = models.CharField(verbose_name='供应商代码', max_length=16)
    person_purchase = models.CharField(verbose_name='筹措员', max_length=16)
    tpl_code = models.CharField(verbose_name='三方物流库代码', max_length=64)
    tpl_name = models.CharField(verbose_name='三方物流库名称', max_length=64)
    tpl_number = models.BigIntegerField(verbose_name="3PL库存", null=True, default=None)
    online_stock = models.BigIntegerField(verbose_name="在线需求", null=True, default=None)
    require_max = models.BigIntegerField(verbose_name="MAX日需求", null=True, default=None)
    require_one = models.BigIntegerField(verbose_name="Day1需求", null=True, default=None)
    require_two = models.BigIntegerField(verbose_name="Day2需求", null=True, default=None)
    require_three = models.BigIntegerField(verbose_name="Day3需求", null=True, default=None)
    require_four = models.BigIntegerField(verbose_name="Day4需求", null=True, default=None)
    require_five = models.BigIntegerField(verbose_name="Day5需求", null=True, default=None)
    require_six = models.BigIntegerField(verbose_name="Day6需求", null=True, default=None)
    require_seven = models.BigIntegerField(verbose_name="Day7需求", null=True, default=None)

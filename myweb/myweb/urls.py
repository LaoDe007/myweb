"""myweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from web01.views import account, admin, tpl, fpl, data, chart

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', admin.admin_list),
    path('login/', account.login),

    # 管理员管理
    path('admin/list/', admin.admin_list),
    path('admin/add/', admin.admin_add),
    path('admin/<int:nid>/edit/', admin.admin_edit),
    path('admin/<int:nid>/reset/', admin.admin_reset),
    path('admin/<int:nid>/delete/', admin.admin_delete),
    path('admin/multi/', admin.admin_multi),

    # 三方物流管理
    path('tpl/list/', tpl.tpl_list),
    path('tpl/multi/', tpl.tpl_multi),
    path('tpl/<int:nid>/delete/', tpl.tpl_delete),
    # path('tpl/<int:nid>/edit/', tpl.tpl_edit),

    # 工厂需求管理
    path('fpl/list/', fpl.fpl_list),
    path('fpl/multi/', fpl.fpl_multi),

    # 数据处理
    path('data/search/', data.data_search),
    path('data/multi/', data.data_multi),

    # 图表分析
    path('chart/list/', chart.chart_list),
    path('chart/bar/', chart.chart_bar),
]

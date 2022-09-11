from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse


def chart_list(request):
    return render(request, "chart_list.html")


def chart_bar(request):
    """构造柱状图数据"""
    legend = ["小王", "小李"]
    series_list = [
        {
            "name": '小王',
            "type": 'bar',
            "data":  [5, 20, 36, 10],
        },
        {
            "name": '小李',
            "type": 'bar',
            "data": [15, 40, 56, 21],
        }
    ]
    x_axis = ['1月', '2月', '3月', '4月']
    result = {
        "status": True,
        "legend": legend,
        "series_list": series_list,
        "x_axis": x_axis,
    }
    return JsonResponse(result)
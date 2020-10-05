from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views import View

import numpy_financial
# Create your views here.


class FixDeposit(View):
    def get(self, request):
        return render(request, "calculator/fd.html")

    def post(self, request):
        amount = request.POST.get('amount')
        rate = request.POST.get('rate')
        months = request.POST.get('months')
        ret_earned = float(amount) * (float(rate) / 100)
        total_amount = float(amount) + ret_earned
        print(ret_earned, total_amount)

        return JsonResponse({'status': True, 'msg': "Results", "earn": ['Total Interest Earned:', ret_earned],
                             'total': ["Maturity amount:", total_amount]})


class CarLoan(View):
    
    def get(self, request):
      
        return render(request, "calculator/car.html")

    def post(self, request):
        price = request.POST.get('price')
        payment = request.POST.get('payment')
        rate = request.POST.get('rate')
        years = request.POST.get('years')

        load_value = float(price) - float(payment)
        year_interest = load_value * (float(rate) / 100)  # 一年的利息
        total_interest = year_interest * float(years)  # 全部的利息
        total_price = total_interest + load_value      # 贷款+利息
        month_pay = total_price / (float(years) * 12)  # 每个月共多少钱
        print(total_price)
        print(month_pay)

        ret_msg = {'status': True, 'msg': "Results", "pay": ['Monthly Repayment', month_pay],
                   'total': ["Total Interest", total_interest], 'load': ["Load + Interest", total_price]}

        return JsonResponse(ret_msg)


class HomeLoan(View):

    def get(self, request):
        return render(request, "calculator/home.html")

    def post(self, request):
        amount = request.POST.get('amount')
        rate = request.POST.get('rate')
        year = request.POST.get('year')

        ret_pmt = numpy_financial.pmt(float(rate)/100/12, float(year)*12, float(amount))
        ret_pmt = abs(ret_pmt)
        month_pay = round(ret_pmt, 2)
        total_amount = month_pay * float(year)*12
        total_amount = round(total_amount, 2)
        total_interest = total_amount - float(amount)
        total_interest = round(total_interest, 2)
        print(month_pay, total_amount, total_interest)

        ret_msg = {'status': True, 'msg': "Results", "pay": ['Monthly Repayment', month_pay], 'total': ["Total Interest", total_interest], 'loan': ["Load + Interest", total_amount]}
        return JsonResponse(ret_msg)


class Bmi(View):

    def get(self, request):
        return render(request, "calculator/bmi.html")

    def post(self, request):
        weight = request.POST.get('weight')
        cm = request.POST.get('cm')

        ret_cm = int(cm) / 100 * int(cm) / 100
        ret_bmi = float(weight) / ret_cm
        ret_bmi = round(ret_bmi, 1)
        print(ret_bmi)
        return JsonResponse({'status': True, 'msg': "Results", "bmi": ['Your BMI:', ret_bmi]})



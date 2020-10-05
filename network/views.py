from .utils import validfunc
import os
# import whois
import socket
import paramiko
import geoip2.database
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View


# Create your views here.


class Dig(View):

    def get(self, request):
        return render(request, 'network/dig.html')

    def post(self, request):
        domain = request.POST.get('domain')
        digType = request.POST.get('type')
        ret = os.popen("dig %s %s +noall +authority +answer" % (domain, digType)).read()
        ret = ret.split("\n")
        return JsonResponse({'status': True, 'msg': "Results", "ret": ret})


class Ip(View):
    def get(self, request):
        reader = geoip2.database.Reader('network/lib/GeoLite2-ASN.mmdb')
        reader_city = geoip2.database.Reader('network/lib/GeoLite2-City.mmdb')
        response = reader.asn('137.59.187.240')
        response1 = reader_city.city('137.59.187.240')
        print(response)
        print(response1.country.name)
        return render(request, 'network/ip.html')

    def post(self, request):
        reader = geoip2.database.Reader('network/lib/GeoLite2-ASN.mmdb')
        reader_city = geoip2.database.Reader('network/lib/GeoLite2-City.mmdb')
        ip = request.POST.get('ip')
        ret_valid = validfunc.ip_or_domain(ip)
        if ret_valid == "ip":
            ret_type = validfunc.ip_type(ip)
            if ret_type == "PUBLIC":
                response = reader.asn(ip)
                response1 = reader_city.city(ip)
                isp = response.autonomous_system_organization
                country = response1.country.name
                ret_json = {'status': True, 'msg': "Results", "ip": ['IP', ip], 'isp': ["ISP", isp],
                            'country': ['Country', country]}
            else:
                ret_json = {'status': True, 'msg': "Results", "ip": ['IP', ip], 'isp': ["ISP", ret_type]}

        elif ret_valid == "domain":
            ret_ip = validfunc.digLookup(ip)
            response = reader.asn(ret_ip)
            response1 = reader_city.city(ret_ip)
            isp = response.autonomous_system_organization
            country = response1.country.name
            ret_json = {'status': True, 'msg': "Results", "ip": ['IP', ret_ip], 'isp': ["ISP", isp],
                        'country': ['Country', country]}
        else:
            ret_json = {'status': True, 'msg': "Results", "ip": ['Error', "is not a valid IP address"]}

        return JsonResponse(ret_json)


class WhoIs(View):
    def get(self, request):
        return render(request, "network/whois.html")

    def post(self, request):
        domain = request.POST.get('domain')
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect('172.104.190.158', username='root', password='qq9599100..')
        stdin, stdout, stderr = client.exec_command('whois -H %s'% domain)
        total_str = ''
        whoiscan = ''
        count = 0
        for i in stdout:
            if "No match for" in i:
                count += 1
                whoiscan = domain + " is available"
                break
            else:
                total_str += i.strip() + '\n'
            print(i)
        client.close
        # ret = os.popen("whois %s" % domain).read()
        
        return JsonResponse({'status': True, 'msg': "Results", "whois": total_str, "whoiscan": whoiscan})


class IpCheckPort(View):
    def get(self, request):
        return render(request, "network/ipcheckport.html")

    def post(self, request):
        ip = request.POST.get('ip')
        port = request.POST.get('port')
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        status = sock.connect_ex((ip, int(port)))
        if status == 0:
            ret = "Port %s is open." % port
        else:
            ret = "Port %s is closed." % port
        sock.close()

        return JsonResponse({'status': True, 'msg': "Results", "check": ret})

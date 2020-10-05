from validators import domain, ipv4
from IPy import IP
import os



def ip_or_domain(item):
    ret_ip = ipv4(item)
    print(ret_ip)
    ret_domain = domain(item)
    if ret_ip:
        return 'ip'
    if ret_domain:
        return 'domain'
    return False


def ip_type(ip):
    ret_type = IP(ip).iptype()
    return ret_type


def digLookup(domain):
    ret = os.popen("dig %s +short" % (domain)).read()
    ret_ip = ret.split("\n")[-2]
    return ret_ip


if __name__ == '__main__':
    ret = ip_or_domain("172.16.1.1")
    print(ret)
    # digLookup("google.com")

import scapy.all as scapy
import optparse

def giris():
    karsvegas = optparse.OptionParser()
    karsvegas.add_option("-i","--ipadres",dest="ip_adresi",help="-i veya --ipadresi yazarak ip adresi giriniz ")
    (user_giris,arguments)=karsvegas.parse_args()
    if not user_giris.ip_adresi:
        print("ip gir la manyak")
    return user_giris.ip_adresi

def tarayici(ip):
    istek_paket = scapy.ARP(pdst="192.168.1./24")
    #scapy.ls(scapy.ARP())
    yayin_paket = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") # burası mac için
    #scapy.ls(scapy.Ether())
    paket = yayin_paket/istek_paket
    (asilPaket,gecersizPaket) = scapy.srp(paket,timeout=1)
    asilPaket.summary()

ipadresim=giris()
tarayici(ipadresim)

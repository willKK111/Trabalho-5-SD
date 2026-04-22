import paho.mqtt.client as mqtt
import ssl
import time
import random

# Configurações de Conexão
BROKER = "78262e395b904e27b6d8063d6d83424a.s1.eu.hivemq.cloud"
PORTA = 8883
USER = "admin"      
PASSWORD = "hivemQ123" 

# 1. Definir a versão da API (necessário para Paho-MQTT 2.x)
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# 2. Configurar Usuário e Senha
client.username_pw_set(USER, PASSWORD)

# 3. ATIVAR TLS (Sem isso, o código trava no connect)
client.tls_set(tls_version=ssl.PROTOCOL_TLSv1_2)

print(f"Iniciando sensor de temperatura em {BROKER}...")

try:
    client.connect(BROKER, PORTA, 60)
    
    client.loop_start()

    while True:
        # Gera um valor de temperatura entre 20°C e 35°C
        temperatura = round(random.uniform(20.0, 35.0), 2)
        
        client.publish("agro/temperatura", temperatura)
        
        status = "ALTA" if temperatura > 30 else "NORMAL"
        print(f"Enviado -> Temperatura: {temperatura}°C | Status: {status}")
        
        time.sleep(5)

except KeyboardInterrupt:
    print("\nSensoriamento de temperatura interrompido.")
    client.loop_stop()
    client.disconnect()
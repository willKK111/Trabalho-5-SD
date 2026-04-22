import paho.mqtt.client as mqtt
import ssl  # Necessário para o TLS
import time
import random

# Configurações de Conexão
BROKER = "78262e395b904e27b6d8063d6d83424a.s1.eu.hivemq.cloud"
PORTA = 8883
USER = "admin"      
PASSWORD = "hivemQ123" 

# Se estiver usando Paho-MQTT 2.0+, use a linha abaixo:
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# Configura as credenciais
client.username_pw_set(USER, PASSWORD)

# --- ESSENCIAL: Ativa a conexão segura ---
client.tls_set(tls_version=ssl.PROTOCOL_TLSv1_2)

print(f"Conectando ao broker em {BROKER}...")
try:
    client.connect(BROKER, PORTA, 60)

    client.loop_start() 

    while True:
        # Gera um valor aleatório de umidade
        umidade = round(random.uniform(10, 80), 2)
        
        # Enviando para o tópico (verifique se prefere 'agro' ou 'agros')
        result = client.publish("agro/umidade", umidade)
        
        # Verifica se o envio foi bem sucedido
        if result.rc == mqtt.MQTT_ERR_SUCCESS:
            print(f"Sensor enviando -> Umidade: {umidade}%")
        else:
            print("Falha ao enviar mensagem")
        
        time.sleep(5)

except KeyboardInterrupt:
    print("\nSimulação encerrada pelo usuário.")
    client.loop_stop()
    client.disconnect()
except Exception as e:
    print(f"Erro: {e}")
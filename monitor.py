import paho.mqtt.client as mqtt
import ssl

# Configuração da Conexão
BROKER = "78262e395b904e27b6d8063d6d83424a.s1.eu.hivemq.cloud"
PORTA = 8883
USER = "admin"
PASSWORD = "hivemQ123"

# Na versão 2, a assinatura do on_connect mudou levemente (adicionou o parâmetro reason_code_obj)
def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("Conectado com sucesso ao HiveMQ!")
        client.subscribe("#")
    else:
        print(f"Falha na conexão. Código de erro: {rc}")

def on_message(client, userdata, msg):
    print(f"Tópico: {msg.topic} | Mensagem: {msg.payload.decode()}")


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

client.tls_set(tls_version=ssl.PROTOCOL_TLSv1_2)
client.username_pw_set(USER, PASSWORD)

client.on_connect = on_connect
client.on_message = on_message

print("Tentando conectar ao Broker...")
client.connect(BROKER, PORTA, 60)

print("Iniciando loop de escuta...")
client.loop_forever()
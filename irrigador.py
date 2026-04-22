import paho.mqtt.client as mqtt
import ssl

# Configurações de Conexão
BROKER = "78262e395b904e27b6d8063d6d83424a.s1.eu.hivemq.cloud"
PORTA = 8883
USER = "admin"
PASSWORD = "hivemQ123"

# Ajuste na assinatura da função para a Versão 2 da API
def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("Conectado ao HiveMQ! Monitorando umidade...")
        client.subscribe("agro/umidade")
    else:
        print(f"Falha na conexão. Código: {rc}")

def on_message(client, userdata, msg):
    try:
        # Converte o payload para número
        umidade = float(msg.payload.decode())
        print(f"\nUmidade recebida: {umidade}%")

        if umidade < 30:
            status = "ON"
            aviso = "Solo seco! Irrigador: LIGADO"
        else:
            status = "OFF"
            aviso = "Solo úmido. Irrigador: DESLIGADO"
        
        print(aviso)
        
        # Publica a decisão no tópico do irrigador
        client.publish("agro/irrigador", status)
        
    except ValueError:
        print(f"Erro: Mensagem inválida recebida em {msg.topic}")

# 1. Inicialização com a Versão 2 da API
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# 2. Configura as credenciais
client.username_pw_set(USER, PASSWORD)

# 3. ATIVA O TLS (Obrigatório para HiveMQ Cloud)
client.tls_set(tls_version=ssl.PROTOCOL_TLSv1_2)

# Configura as funções de callback
client.on_connect = on_connect
client.on_message = on_message

print(f"Conectando ao controlador em {BROKER}...")

try:
    client.connect(BROKER, PORTA, 60)
    client.loop_forever()
except Exception as e:
    print(f"Erro ao conectar: {e}")
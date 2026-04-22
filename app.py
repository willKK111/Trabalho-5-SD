from flask import Flask, render_template
from flask_socketio import SocketIO
import paho.mqtt.client as mqtt
import ssl

# Configuração da Conexão
Porta = 8883
BROKER = "78262e395b904e27b6d8063d6d83424a.s1.eu.hivemq.cloud"
USER = "admin"
PASSWORD = "hivemQ123"

app = Flask(__name__)
# O cors_allowed_origins="*" permite que o navegador acesse o socket sem bloqueios
socketio = SocketIO(app, cors_allowed_origins="*")

# Ajuste na assinatura para a Versão 2 da API
def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("Flask conectado com sucesso ao HiveMQ!")
        client.subscribe("#")
    else:
        print(f"Falha na conexão do Flask. Código: {rc}")

def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    
    socketio.emit('mqtt_update', {'topic': msg.topic, 'value': payload})

# 1. Definir a versão da API 
mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# 2. Configurar Segurança TLS (OBRIGATÓRIO para porta 8883)
mqtt_client.tls_set(tls_version=ssl.PROTOCOL_TLSv1_2)

# 3. Configurar Credenciais
mqtt_client.username_pw_set(USER, PASSWORD)

mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message


print("Tentando conectar o Servidor ao Broker...")
mqtt_client.connect(BROKER, Porta, 60)
mqtt_client.loop_start()

@app.route('/')
def index():
    
    return render_template('index.html')

if __name__ == '__main__':
    socketio.run(app, port=5000, debug=True)
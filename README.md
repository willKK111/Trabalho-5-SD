# 🌿 SmartAgro: Simulação de Agricultura 4.0 (MQTT)
Este projeto simula um ecossistema de Agricultura 4.0 utilizando comunicação indireta baseada em mensagens. O objetivo é monitorar e atuar em uma plantação virtual através de um Broker MQTT, garantindo desacoplamento entre sensores, atuadores e o sistema de monitoramento.

## 📌 Visão Geral da Arquitetura
A aplicação utiliza o modelo Publish/Subscribe. Os sensores publicam dados de telemetria, o monitor processa essas informações e o atuador responde a comandos específicos enviados via tópicos.

Componentes do Sistema:
Sensores Virtuais:

  Sensor de Temperatura: Simula a temperatura ambiente da plantação.

  Sensor de Umidade do Solo: Simula o nível de hidratação da terra.

Atuador Virtual:

  Irrigador Automático: Ativa ou desativa com base nas mensagens recebidas.

  Sistema Consumidor (Dashboard/Monitor):

Script que centraliza a visualização dos dados e pode disparar alertas ou comandos.

## 🛠️ Tecnologias Utilizadas
Linguagem: Python 

Protocolo de Comunicação: MQTT (Message Queuing Telemetry Transport)

Broker: HiveMQ Cloud

Biblioteca Principal: paho-mqtt

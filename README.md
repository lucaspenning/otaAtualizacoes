# OTA_Atualizações

Atualização via OTA é a mais comum ultimamente, Over-the-Air “OTA”, significa que a atualização está disponível no próprio aparelho, a atualização será baixada e instalada de forma automática, logo depois disso, o próprio dispositivo inicia a atualização do sistema.

### Características:
Linguagem de programação: **Micropython**

Embarcado: **ESP32**

Firmware: **esp32-idf3-20191220-v1.12**

Ferramenta: **UpyCraft**

Broker MQTT: **IoTicos**

### Funcionamento:
O código fonte deverá ficar em um repositório público do GitHub, com versionamento de releases, o que é muito importante ser feito pois é fundamental para  funcionamento correto da atualização via OTA, então toda vez que o sistema for reiniciado, o dispositivo irá procurar a rede wifi com acesso à internet especificada em um arquivo JSON, fazendo a verificação comparado a versão atual do código presente no dispositivo com a versão do repositório do GitHub que também será especificado no arquivo JSON, sempre que haver um nova atualização ou release, então será feita a atualização automaticamente do código. 

Após realizar a verificação de versionamento caso ocorrer alguma atualização um led da cor verde deverá piscar duas vezes, caso não ocorrer nenhuma atualização o led deve piscar uma vez, também será publicada uma menssagem em um Broker MQTT com o log das atividades realizadas em questão a atualização. 

Se ocorrer falta de energia ou falta de rede internet apresentando erro na atualização um led amarelo permanecerá acesso até o problema ser resolvido e prosseguir com a atualização, em caso de erro de configuração será iniciado as ativiades do aparelho com os arquivos de versão presentes no embarcado. Ao final da rotina de atualizações se tudo ocorreu bem o led amarelo irá ser apagado. 

São 6 arquivos em MicroPython além de uma pasta nomeada como SRC, dentro desta pasta ficará nosso código de rotina para qual embarcado foi programado a realizar, neste caso foi implementado uma rotina para piscar leds.

### Configurações:
Primeiramente o arquivo que deve ser configurado é o arquivo JSON, sendo alterado o SSID e PASSWORD da rede, além do link do repositório do GitHub desejado, próximo passo será alterar as informações do MQTTClient, presentes no arquivo boot.py para o destino MQTT desejado. Logo após, pode ser feito a alteração do arquivo exemplo.py para a rotina de atividades desejadas.

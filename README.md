# OTA_Atualizações

Atualização via OTA é a mais comum ultimamente, Over-the-Air “OTA”, significa que a atualização está disponível no próprio aparelho, a atualização será baixada e instalada de forma automática, logo depois disso, o próprio dispositivo inicia a atualização do sistema.

### Características:
Linguagem de programação: **Micropython**

Embarcado: **ESP32**

Firmware: **esp32-idf3-20191220-v1.12**

Ferramenta: **UpyCraft**

Broker MQTT: **IoTicos**

### Funcionamento:
O código fonte deverá ficar em um repositório público do GitHub, com versionamento de releases, o que é muito importante ser feito pois é fundamental para  funcionamento correto da atualização via OTA, então toda vez que o sistema for reiniciado, o dispositivo irá procurar a rede wifi com acesso à internet especificada em um arquivo JSON, fazendo a verificação comparado a versão atual do código presente no dispositivo com a versão do repositório do GitHub que também será especificado no arquivo JSON, sempre que haver um nova atualização ou release e o dispositivo for reiniciado, então será feita a atualização automaticamente do código. 

Após realizar a verificação de versionamento caso ocorrer alguma atualização um led da cor verde deverá piscar duas vezes, caso não ocorrer nenhuma atualização o led deve piscar uma vez, também será publicada uma mensagem em um Broker MQTT denominado IoTicos, com o log das atividades realizadas em questão a atualização. 

Logo a ligar o aparelho um led de cor Amarelo será acesso, se ocorrer falta de energia elétrica durante o processo de atualização, assim que a energia elétrica for retomada a atualização será refeita, se tivermos falta de rede internet apresentando erro na atualização um led amarelo permanecerá acesso até o problema ser resolvido e prosseguir com a atualização, isso se dá pelo fato da rotina de atualizações só gravar a nova versão no arquivo .version assim que 100% da atualização for concluida. Ao final da rotina de atualizações se tudo ocorreu bem o led amarelo irá ser apagado. 

### Arquivos:
São 6 arquivos em MicroPython além de uma pasta nomeada como SRC, dentro desta pasta ficará nosso código de rotina para qual embarcado foi programado a realizar, neste caso foi implementado uma rotina para piscar leds.

**conf.json:** arquivo onde configuramos com as credenciais da nossa rede Wifi e repositório do GitHub;

**Ota_updater.py:** arquivo onde são realizados todos os downloads e update dos códigos com base no repositório do GitHub;

**Code_download:** arquivo onde é realizado a conexão com a rede wifi, além de atualizar os códigos existentes no dispositivo;

**.version:** arquivo onde fica guardado e sincronizado todas a informação de versionamento do projeto local do dispositivo com o repositório do GitHub;

**boot.py:** arquivo responsável rotina de atualizações ao reinicar o dispositivo, realizar a sincronização de todos os arquivos do projeto, além de publicar no broker MQTT IoTicos;

**src/exemplo.py:** arquivo onde é implementada uma rotina específica para o dispositivos, como por exemplo: leitura de sensores, controle de temperatura e etc...;

### Configurações:
Primeiramente o arquivo que deve ser configurado é o arquivo JSON, sendo alterado o SSID e PASSWORD da rede, além do link do repositório do GitHub desejado, próximo passo será alterar as informações do MQTTClient presentes no arquivo boot.py para o destino Broker MQTT configurado por você. Logo após, pode ser feito a alteração do arquivo exemplo.py para a rotina de atividades desejadas.

### Bibliotecas:
Foi utilzado a biblioteca UMQTT, com o arquivo simple.py para realizar a postagem de mensagens no Broker MQTT.


### Releases:
Caso não sejam feitas as releases corretamente (senão souber utilizar existem documentações do GitHub que poderão auxiliar nesse processo), irá ocasionar no mau funcionamento das atualizações, importante que o TAG VERSION siga o padrão 1.0, 1.1, 1.2,..., sempre matendo como base X.X;

### Documento PDF:
https://drive.google.com/file/d/1Dz_C2aP1KITh-WH6nKGxEjChyILz9Rt8/view?usp=sharing

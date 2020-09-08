# OTA_Atualizações

Atualização via OTA é a mais comum ultimamente, Over-the-Air “OTA”, significa que a atualização está disponível no próprio aparelho, a atualização será baixada e instalada de forma automática, logo depois disso, o próprio dispositivo inicia a atualização do sistema.

### Características:
Linguagem de programação: **Micropython**

Embarcado: **ESP32**

Firmware: **esp32-idf3-20191220-v1.12**

Ferramenta: **UpyCraft**

Broker MQTT: **IoTicos**

### Funcionamento:
O código fonte deverá ficar em um repositório público do GitHub, com versionamento de releases, o que é muito importante ser feito pois é fundamental para  funcionamento correto da atualização via OTA, então toda vez que o sistema for reiniciado, o dispositivo irá procurar a rede wifi com acesso à internet especificada em um arquivo JSON, fazendo a verificação comparado a versão atual do código presente no dispositivo com a versão do repositório do GitHub que também será especificado no arquivo JSON, sempre que haver um nova atualização ou release, então irá baixar e fazer a atualização automaticamente do código. Após realizar a verificação de versionamento caso ocorrer alguma atualização um led da cor verde deverá piscar 2 vezes, caso não ocorrer nenhuma atualização um led da cor vermelho deverá piscar 3 vezes, também será publicada uma menssagem em um Broker MQTT com o log das atividades realizadas em questão a atualização. Se ocorrer uma falta de energia durante a atualização assim que a energia voltar irá ser retomada a atualização, se ocorrer falta de rede internet apresentando erro na atualização um led amarelo ficará acesso até voltar a rede internet e prosseguir com a atualização. São 6 arquivos em MicroPython além de uma pasta nomeada como SRC, dentro desta pasta ficará nosso código de rotina para qual embarcado foi programado a realizar, neste caso foi implementado uma rotina para piscar leds.

### Arquivos:

### Configurações:

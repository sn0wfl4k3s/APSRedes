# **Introdução**

## **Descrição da atividade:**

Neste atividade estarei mostrando o desenvolvimento e criação de quatro aplicações sendo duas cliente e as outras duas servidor, sendo um par cliente-servidor para TCP e a outra cliente-servidor para UDP, que funcionaram conectando-se o cliente com o servidor e transferindo um determinado valor numérico para que o servidor retorne um resultado que corresponde a 25% (porcento) desse valor numérico. A aplicação cliente se conecta ao servidor, após estabelecida a conexão, o cliente envia uma dado de tipo numérico ao servidor, então o mesmo processa tal valor e retorna um valor(output) que corresponde a 25% do valor enviado pelo cliente (input), em seguida esse valor output é enviado de volta ao cliente.

### **Detalhes técnicos:**
o valor enviado pelo socket é em formato string, logo esse valor deverá passar por uma verificação e parser para converter o valor input em um dado de tipo numérico.
Adotaremos a linguagem python para esse trabalho.
Os códigos usados serão baseados na https://wiki.python.org.br/SocketBasico que é a documentação oficial para programação de sockets em python



## **Conceito de Socket e Camada de Aplicação:**

Sockets são basicamente o ponto de comunicação entre processos através da rede criando um elo bidirecional de comunicação onde é estabelecida uma conexão virtual anteriormente e compartilhamento de dados. A camada de aplicação é a mais alta dos protocolos sendo utilizada diretamente onde as aplicações atuam. Desse modo é possível criar aplicações de se comunicam da camada de aplicação diretamente para a camada de transporte através dos uso sockets, através de interfaces que geralmente os sistemas operacionais disponibilizam internamente e realizando assim uma conexão virtual TCP ponta-a-ponta usando modelos como cliente-servidor ou P2P (peer-to-peer).Sockets é a porta onde aplicações conversam entre si.

Segundo o Kurosi: " ...cada processo é semelhante a uma casa e que o socket é semelhante a uma porta. A aplicação reside em um lado da porta na casa; o protocolo da camada de transporte reside no outro lado da porta, no mundo exterior. O programador da aplicação controla tudo que está no lado da camada de aplicação da porta; contudo tem pouco controle do lado da camada de transporte."



## **Instalação e Configuração de ambiente python:**

Nessa configuração de ambiente usaremos sistema operacional windows por ser de grande uso pela maioria dos usuários. A instalação do interpretador python no ambiente windows é bem simples, basta navegar até o site https://python.org/downloads fazer o download do executável. Após o download basta executar como administrador e simplesmente dar next, next e next na instalação do python e pronto, o interpretador python já está instalado e pronto para uso. Caso não esteja, basta reiniciar a máquina.

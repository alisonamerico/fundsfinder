# FUNDSFINDER

API desenvolvida com [Django](https://www.djangoproject.com/), [Django REST Framework](https://www.django-rest-framework.org/) para consulta de um tipo de investimento: Fundos Imobiliários (ou FIIs).

## Modelagem

O processo de desenvolvimento de aplicações que utilizam o Django Rest Framework geralmente seguem a seguinte linha de implementação:

1. Modelagem;
2. Serializers;
3. ViewSets;
4. Routers

Vamos começar com a Modelagem!

Para auxiliar nessa tarefa, escolhi alguns parâmetros de uma tabela muito interessante do site [FundsExplorer](https://www.fundsexplorer.com.br/ranking):

![fundos](img-readme/funds.png)

Vamos usar os seguintes atributos:

- **Código do Fundo**: Código identificador do Fundo.
- **Setor**: Setor do Fundo Imobiliário.
- **Dividend Yield médio (12 meses)**: Dividend Yield mostra quanto um fundo paga de Dividendos (divisão de lucros) sobre o valor atual da cota.
- **Vacância Financeira**: Importante métrica que mostra ao investidor quantos ativos do Fundo Imobiliários estão inadimplentes.
- **Vacância Física**: Outra importante métrica que mostra ao investidor quantos ativos estão desocupados.
- **Quantidade de Ativos**: Quantos ativos são administrados pelo Fundo.

Com isso em mãos, podemos criar a modelagem da entidade **FundoImobiliario**.

## Serializer

Eles servem para traduzir entidades complexas, como querysets e instâncias de classes em representações simples que podem ser usadas no tráfego da web, como JSON e XML.

Esse processo é chamado de Serialização.

Serializers também servem para fazer o caminho contrário: a Desserialização.

Isto é, transformar representações simples (como JSON e XML) em representações complexas, instanciando objetos, por exemplo.

O DRF disponibiliza diversos tipos de serializers que podemos utilizar, como:

BaseSerializer: Classe base para construção de Serializers mais genéricos.
ModelSerializer: Auxilia a criação de serializadores baseados em modelos.
HyperlinkedModelSerializer: Similar ao ModelSerializer, contudo retorna um link para representar o relacionamento entre entidades (ModelSerializer retorna, por padrão, o id da entidade relacionada).
Vamos utilizar o ModelSerializer para construir o serializador da entidade FundoImobiliario.

Para isso, precisamos declarar sobre qual modelo aquele serializador irá operar e quais os campos que ele deve se preocupar.

## ViewSets

As ViewSets definem quais operações REST estarão disponíveis e como seu sistema vai responder às chamadas à sua API.

Em outros frameworks, são chamados de Resources ou Controllers.

ViewSets herdam e adicionam lógica às Views padrão do Django.

Suas responsabilidades são:

Receber os dados da Requisição (formato JSON ou XML)
Validar os dados de acordo com as regras definidas na modelagem e no Serializer
Desserializar a Requisição e instanciar objetos
Processar regras de negócio (aqui é onde implementamos a lógica dos nossos sistemas)
Formular uma resposta e responder a quem chamou sua API

Encontrei uma imagem muito interessante no [Reddit](https://www.reddit.com/r/django/comments/9grsum/a_django_rest_framework_view_inheritance_diagram/) que mostra o diagrama de herança das classes do DRF, que nos ajuda a entender melhor a estrutura interna do framework:

![drf-classes](img-readme/drf-classes.png)

Na imagem:

- Lá em cima, temos a classe View padrão do Django.
- APIView e ViewSet são classes do DRF que herdam de View e que trazem algumas configurações específicas para transformá-las em APIs, como métodos get() para tratar requisições HTTP GET e post() para tratar requisições HTTP POST.
- Logo abaixo, temos a GenericAPIView - que é a classe base para views genéricas - e a GenericViewSet - que é a base para as ViewSets (a parte da direita em roxo na imagem).
- No meio, em azul, temos os Mixins. Eles são os blocos de código responsáveis por realmente implementar as ações desejadas.
- Em seguida temos as Views que disponibilizam as funcionalidades da nossa API, como se fossem blocos de Lego. Elas estendem dos Mixins para construir a funcionalidade desejada (seja listagem, seja deleção e etc)

Por exemplo: se você quiser criar uma API que disponibilize apenas listagem de uma determinada Entidade você poderia escolher a ListAPIView.

Agora se você precisar construir uma API que disponibilize apenas as operações de criação e listagem, você poderia utilizar a ListCreateAPIView.

Agora se você precisar construir uma API “com tudo dentro” (isto é: criação, deleção, atualização e listagem), escolha a ModelViewSet: perceba que ela estende todos os Mixins disponíveis.

Para entender de vez:

- Os Mixins são como os componentes dos sanduíches do Subway :tomato: :bread: :poultry_leg: :meat_on_bone:
- As Views são como o Subway: você monta o seu, componente à componente :bread:
- As ViewSets são como o McDonalds: seu sanduíche já vem montado :hamburger:

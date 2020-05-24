# Sale-Python
Implementação da camada de Domínio:

1-sub-camada de Entidades: *Entity.cs Esta classe herda propriedades para as classes FILHAS Criar todas as Entidades necessárias conforme modelo emhttps://github.com/ranieresilva/controle-estoque.git Exemploi: 1-verificar que em Models dentro da sub-pasta Domain os nomes das classes; 1.1-onde visualiza-se CidadeModel.cs deverá ser criar uma Entidade chamada Cidade

Entidades: 1- Entity.cs 2- Cidades.cs 3 - EntradaProduto.cs 4- Estado.cs 5- Fornecedor.cs 6- GrupoProduto.cs 7- InventarioEstoque.cs 8- LocalArmazenamento.cs 9- MarcaProduto.cs 10- Pais.cs 11- Perfil.cs 12- Produto.cs 13- Pedido.cs 14- ItemPedido.cs 15- SaidaProduto.cs 16- Tipo.cs 17- UnidadeMedida.cs 18- Usuario.cs

Criação das Interfaces:

1- IBaseRepository.cs 2- ICidadesRepository.cs 3 - IEntradaProdutoRepository.cs 4- IEstadoRepository.cs 5- IFornecedorRepository.cs 6- IGrupoProdutoRepository.cs 7- IInventarioEstoqueRepository.cs 8- ILocalArmazenamentoRepository.cs 9- IMarcaProdutoRepository.cs 10- IPaisRepository.cs 11- IPerfilRepository.cs 12- IProdutoRepository.cs 13- IPedidoRepository.cs 14- IItemPedidoRepository.cs 15- ISaidaProdutoRepository.cs 16- ITipoRepository.cs 17- IUnidadeMedidaRepository.cs 18- IUsuarioRepository.cs

<img src="https://hackernoon.com/hn-images/1*YVxaXqiIYskqPauNKZ2OSA.png">

#Obs: em lugar no NET Core será usado o Python

<img src="https://drive.google.com/file/d/147AHuQvl81BNq-OU_Ac8oOQJ7_W7LPo9/view?usp=sharing>


# PYTHON SALE 

Virtual store builded on Python and Web Framework Django using software archtecture DDD 

1 - Objetivos

=> A aplicação tem como base criar uma loja virtual para cadastros de usuários e controle dos estoques de vendas, aonde no controle de estoque de vendas teremos como entidades principais(Usuário, produto, Item Pedido, Pedido). Observar-se-à que o aplicativo deverá permitir as operações básicas de cadastro e inclusão de documentação em modo offline caso não haja conectividade de Internet no momento de cadastro. 

2 - Arquitetura

=> Implementar arquitetura orientada à serviços com objetivo de proporcionar isolanilidade entre os diversos módulos.

=> Implementação da abordagem REST FULL pois assim poderá futuramente permitir que diversos devices móveis possam conectar ao aplicativo ou até mesmo consumer API’s implementadas.

O sistema possuirá as seguintes camadas abaixo:

<img src="https://pythonacademy.com.br/assets/posts/desenvolvimento-web-com-python-e-django-view/django-architecture.png">

1 - Camada model.py

 Camada à qual teremos as Entidades de Domínios e suas respectivas interfaces para conexão com o Base de Dados;


2 - Camada Views.py


  Camada à qual  teremos o controller da nossa aplicação, a views que vai fazer a comunicação entre a camada models.py da aplicação;


3- Camada urls.py

  Nesa camada existem duas a da aplicação e a do projeto. A de aplicação nós criamos para gerenciar as rotas que queremos que nossa aplicação faça. Ou seja é ela que vai faz a requisição(solicitação) na camada views.py e as Middlewares que faz o todo o processamento de requests e responses, fazendo as autenticações associadas à  usuários para solicitações usando sessões. E a do projeto que já faz as rotas automaticamente, só alterando o caminho por segurança.


4 - Camada admin.py

   Essa camada é responsável por toda gerência administrativa da aplicação. É aqui que vamos fazer o CRUD de tudo que fizermos como inserir, criar, deletar, atualizar e consequetemente será refletida na rota admin.py 


5- Camada Settings.py

   Essa camada é responsável pelas configurações do banco de dados que vamos utilizar, isso será visto com o team de Python durante o desenvolvimento do mesmo.


6 - Camada Template 

   A camada que vai mostrar o usuário do sistema que a GUI(interface) da aplicação.




Implementação da camada de Domínio:

1-sub-camada de Entidades:
*Entity.cs
Esta classe herda propriedades para as classes FILHAS
Criar todas as Entidades necessárias conforme modelo emhttps://github.com/ranieresilva/controle-estoque.git 
Exemploi:
1-verificar que em Models dentro da sub-pasta Domain os nomes das classes;
1.1-onde visualiza-se CidadeModel.cs deverá ser criar uma Entidade chamada Cidade

Entidades:
1- Entity.cs
2- Cidades.cs
3 - EntradaProduto.cs
4- Estado.cs
5- Fornecedor.cs
6- GrupoProduto.cs
7- InventarioEstoque.cs
8- LocalArmazenamento.cs
9- MarcaProduto.cs
10- Pais.cs
11- Perfil.cs
12- Produto.cs
13- Pedido.cs
14- ItemPedido.cs
15- SaidaProduto.cs
16- Tipo.cs
17- UnidadeMedida.cs
18- Usuario.cs


Criação das Interfaces:

1- IBaseRepository.cs
2- ICidadesRepository.cs
3 - IEntradaProdutoRepository.cs
4- IEstadoRepository.cs
5- IFornecedorRepository.cs
6- IGrupoProdutoRepository.cs
7- IInventarioEstoqueRepository.cs
8- ILocalArmazenamentoRepository.cs
9- IMarcaProdutoRepository.cs
10- IPaisRepository.cs
11- IPerfilRepository.cs
12- IProdutoRepository.cs
13- IPedidoRepository.cs
14- IItemPedidoRepository.cs
15- ISaidaProdutoRepository.cs
16- ITipoRepository.cs
17- IUnidadeMedidaRepository.cs
18- IUsuarioRepository.cs



module1.png
_____________________________________________________________________

The system will have the following layers:


1 - model.py layer

Layer to qualify as Domain Entities and their connection interfaces for connection to the Database;


2 - Views.py layer


Layer to qualify or control our application, a display that will communicate between a models.py layer of the application;


3- urls.py layer

In this layer there are two applications and projects. An application that we created to manage as routes that we want our application to do. That is, it makes the requirement (request) in the views.py layer and as Middleware that processes all the processing of requests and responses, doing as authentications requested to users for requests using requests. And a project that already makes the routes automatically, changing the path through security.


4 - admin.py layer

This layer is responsible for all administrative administration of the application. Here, we will CRUD everything that is generated, how to insert, create, delete, update and consequently will be reflected in the route admin.py


5- Settings.py layer

This layer is responsible for the database settings that we will use, this will be seen with the Python team during the development of the same.


6 - Layer model

A layer that shows the system user that application's GUI (interface).

<img src ="https://blog.cleancoder.com/uncle-bob/images/2012-08-13-the-clean-architecture/CleanArchitecture.jpg">


Domain layer implementation:

1-sub-layer of Entities:
* Entity.cs
This class inherits properties for the DAUGHTER classes
Create all the necessary Entities according to the model at https://github.com/ranieresilva/controle-estoque.git
Example:
1-verify that in Models within the Domain sub-folder the names of the classes;
1.1-where CidadeModel.cs is displayed, you must create an Entity called Cidade

Entities:
1- Entity.cs
2- Cities.cs
3 - EntradaProduto.cs
4- State.cs
5- Supplier.cs
6- GrupoProduto.cs
7- InventoryStore.cs
8- LocalStorage.cs
9- BrandProduct.cs
10- Pais.cs
11- Profile.cs
12- Product.cs
13- Order.cs
14- Ordered Item.cs
15- Product Output.cs
16- Type.cs
17- MeasurementUnit.cs
18- User.cs


Creation of Interfaces:

1- IBaseRepository.cs
2- ICidadesRepository.cs
3 - IEntradaProdutoRepository.cs
4- IEstadoRepository.cs
5- IF ProviderRepository.cs
6- IGrupoProdutoRepository.cs
7- IInventarioEstoqueRepository.cs
8- ILocalStorageRepository.cs
9- IMarcaProdutoRepository.cs
10- IPaisRepository.cs
11- IPerfilRepository.cs
12- IProdutoRepository.cs
13- IPedidoRepository.cs
14- IItemRequestory.cs
15- ISaidaProdutoRepository.cs
16- ITipoRepository.cs
17- MeasurementUnitRepository.cs
18- IUsuarioRepository.cs


Controle Financeiro de Despesas - API
Visão Geral
Este projeto é uma API de controle financeiro de despesas, projetada para ser consumida por um front-end em React. A API permite gerenciar clientes, despesas, receitas, parcelas, pagamentos e credores, com suporte a auditoria e armazenamento de dados bancários para pagamentos via transferência ou PIX.

Funcionalidades Principais
Gerenciamento de Clientes: Cadastro e gerenciamento de clientes.
Controle de Despesas: Registro de despesas detalhadas, incluindo despesas parceladas.
Registro de Receitas: Cadastro de fontes de receita.
Gerenciamento de Parcelas: Criação e acompanhamento automático de parcelas para despesas parceladas.
Pagamentos: Registro de pagamentos com detalhamento de forma de pagamento (PIX, transferência, boleto, etc.).
Credores e Dados Bancários: Cadastro de credores e informações bancárias associadas para pagamentos.
Auditoria: Controle de criação e atualização de registros por usuários autenticados.
Tecnologias Utilizadas
Back-End: Python com Django e Django REST Framework (ou frameworks equivalentes como Node.js/Express)
Banco de Dados: PostgreSQL/MySQL
Autenticação: Keycloak ou Django Authentication (com suporte a JWT)
Front-End: React (para consumo da API)
Estrutura do Banco de Dados
O banco de dados inclui as seguintes tabelas principais:

Usuario
Cliente
Pessoa
FonteReceita
Despesa
Parcela
Pagamento
Credor
DadosBancarios
Relacionamentos Chave
Cliente pode ter várias Pessoas, Fontes de Receita, Despesas, Credores e Bancos.
Despesa pode gerar várias Parcelas, cada uma com Pagamentos associados.
Credor pode ter informações detalhadas em DadosBancarios.
Endpoints Principais da API
/api/clientes/: CRUD para clientes.
/api/pessoas/: CRUD para pessoas associadas a clientes.
/api/receitas/: CRUD para fontes de receita.
/api/despesas/: CRUD para despesas, incluindo lógica de parcelamento automático.
/api/parcelas/: Consulta e gerenciamento de parcelas.
/api/pagamentos/: Registro de pagamentos, com detalhamento de forma de pagamento.
/api/credores/: CRUD para credores, com referência a dados bancários.
/api/dados-bancarios/: CRUD para informações bancárias de credores.
Como Executar o Projeto
Clone o repositório:

bash
Copiar código
git clone https://github.com/raderleao/controle-financeiro-pessoal.git
cd controle-financeiro-pessoal
Instale as dependências:

bash
Copiar código
pip install -r requirements.txt
Configure o banco de dados:

Atualize as configurações em settings.py para apontar para seu banco de dados PostgreSQL/MySQL.
Migre as tabelas:

bash
Copiar código
python manage.py makemigrations
python manage.py migrate
Execute o servidor de desenvolvimento:

bash
Copiar código
python manage.py runserver
Consuma a API com React:

Configure o front-end React para fazer chamadas aos endpoints da API.
Considerações de Segurança
Autenticação: Recomenda-se usar JWT com Django REST Framework ou Keycloak para autenticação robusta.
Hashing de Senhas: Utilize algoritmos de hashing seguros para senhas de usuários.
Controle de Acesso: Implemente permissões específicas para endpoints sensíveis.
Próximos Passos
Implementar autenticação com Keycloak para suportar usuários corporativos.
Adicionar testes automatizados para garantir a integridade do sistema.
Implementar notificações de vencimento para lembrar os usuários sobre parcelas pendentes.

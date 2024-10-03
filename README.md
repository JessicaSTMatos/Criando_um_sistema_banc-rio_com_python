# DIO | Criando um Sistema Bancário com Python


##**📚 Desafio | Controle de Depósitos, Saques e Extratos**  

🏆 **Objetivo:** *O desafio consiste em implementar um sistema bancário simples com funcionalidades de depósito, saque e exibição de extrato. O sistema deve seguir as seguintes regras:*

Depósitos: Somente valores positivos podem ser depositados. Esses valores devem ser armazenados e exibidos no extrato.
Saques: O cliente pode realizar até 3 saques diários, com um limite máximo de R$ 500,00 por saque. Caso o saldo da conta seja insuficiente, uma mensagem de erro deve ser exibida informando que a operação não pode ser realizada.
Extrato: Todas as operações de depósito e saque devem ser registradas e exibidas no extrato.

##💻**Resumo das Funcionalidades:**  

🧑‍💻 **Desenvolvimento:** *O sistema é composto por cinco funções principais:`depositar`, `sacar`, `exibir_extrato`, e `main`.*

Menu: Exibe as opções disponíveis para o usuário (Depositar, Sacar, Exibir Extrato, Sair).
Depositar: Solicita ao usuário o valor a ser depositado, garantindo que apenas valores positivos sejam aceitos. Em caso de sucesso, uma mensagem de confirmação é exibida.
Sacar: Permite que o usuário insira o valor a ser sacado, desde que o valor seja inferior ou igual a R$ 500,00, respeitando o limite de 3 saques por dia. O saque só é permitido se houver saldo suficiente. Caso contrário, uma mensagem de erro é exibida.
Exibir Extrato: Mostra o extrato das transações realizadas pelo cliente, incluindo depósitos e saques, além do saldo atual.
Main: Controla o fluxo do programa, permitindo que o usuário navegue entre as opções de depósito, saque e extrato.




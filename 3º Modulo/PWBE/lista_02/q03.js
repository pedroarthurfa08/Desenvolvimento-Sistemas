class ContaBancaria {
    constructor(numeroConta, nomeTitular, saldo = 0) {
        this.numeroConta = numeroConta;
        this.nomeTitular = nomeTitular;
        this.saldo = saldo;
    }

    depositar(valor) {
        if (valor > 0) {
            this.saldo += valor;
            console.log(`Depósito de R$${valor.toFixed(2)} realizado. Novo saldo: R$${this.saldo.toFixed(2)}`);
        } else {
            console.log('O valor do depósito deve ser positivo.');
        }
    }

    sacar(valor) {
        if (valor > 0 && valor <= this.saldo) {
            this.saldo -= valor;
            console.log(`Saque de R$${valor.toFixed(2)} realizado. Novo saldo: R$${this.saldo.toFixed(2)}`);
        } else if (valor > this.saldo) {
            console.log('Saldo insuficiente.');
        } else {
            console.log('O valor do saque deve ser positivo.');
        }
    }

    exibirSaldo() {
        console.log(`Saldo atual da conta ${this.numeroConta}: R$${this.saldo.toFixed(2)}`);
    }
}

const conta1 = new ContaBancaria(1234, 'Roberto Carlos', 500);

conta1.exibirSaldo();
conta1.depositar(200);
conta1.sacar(100);
conta1.exibirSaldo();

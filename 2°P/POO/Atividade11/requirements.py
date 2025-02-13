import pytest
from Empresa_transporte import Veiculo, moto, carro, caminhão, Controle_Viagens

def testVeiculo():
    veiculo = Veiculo ("98465f1r5v1rv51", 2005)
    assert veiculo.__chassi == "98465f1r5v1rv51"
    assert veiculo._ano  == 2005
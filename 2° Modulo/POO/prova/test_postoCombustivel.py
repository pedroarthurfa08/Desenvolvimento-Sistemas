# cd Programacao_Orientada_a_Objetos/Atividades/postoCombustivel
import pytest
from pedro_posto_combustivel import PostoDeCombustivel, BombaDeCombustivel, Combustivel, Gasolina, Etanol, Abastecimento, Controle_De_Abastecimentos

def test_posto_de_combustivel():
    test_um_posto = PostoDeCombustivel('Jady')
    assert test_um_posto._nome == 'Jady'
    
def test_adicionar_bomba_e_listar_bombas():
    BombaDeCombustivel.contadorId = 0
    controle = Controle_De_Abastecimentos()
    test_dois_posto = PostoDeCombustivel('Jady')
    test_dois_bombaUm = BombaDeCombustivel()
    test_dois_bombaDois = BombaDeCombustivel()

    with pytest.raises(TypeError): 
        test_dois_bombaUm.abastecer(20, controle)
    
    assert test_dois_posto.adicionar_bomba(test_dois_bombaUm) == 'Cadastrando bomba 1 ao posto Jady...'
    # assert test_dois_posto.adicionar_bomba(test_dois_bombaDois) == 'Cadastrando bomba 2 ao posto Jady...'
    
    # assert test_dois_posto.listar_bombas() == 'Bomba: 1, Bomba: 2'
    
    # with pytest.raises(TypeError, match='Bomba inválida. A bomba deve ser do tipo BombaDeCombustivel.'):
    #     test_dois_posto.adicionar_bomba(test_dois_posto)
    
def test_bomba_de_combustivel():
    BombaDeCombustivel.contadorId = 0
    test_tres_bombaUm = BombaDeCombustivel()
    assert test_tres_bombaUm._identificador == 1
    assert test_tres_bombaUm._combustivel == None
    
    test_tres_bombaDois = BombaDeCombustivel()
    assert test_tres_bombaDois._identificador == 2
    assert test_tres_bombaDois._combustivel == None
    
def test_associar_combustivel():
    BombaDeCombustivel.contadorId = 0
    test_quatro_bombaUm = BombaDeCombustivel()
    test_quatro_bombaDois = BombaDeCombustivel()
    test_quatro_combustivelGas = Gasolina(5, 'sim')
    test_quatro_combustivelEtanol = Etanol(5, 'milho')

    assert test_quatro_bombaUm.associar_combustivel(test_quatro_combustivelGas) == 'Associando Gasolina Aditivada à bomba 1...'
    assert test_quatro_bombaUm._combustivel == test_quatro_combustivelGas
    
    assert test_quatro_bombaDois.associar_combustivel(test_quatro_combustivelEtanol) == 'Associando Etanol de Milho à bomba 2...'
    assert test_quatro_bombaDois._combustivel == test_quatro_combustivelEtanol
    
    with pytest.raises(TypeError, match='Combustível inválido. O combustível deve ser do tipo Combustivel.'):
        test_quatro_bombaUm.associar_combustivel(test_quatro_bombaDois)
    with pytest.raises(TypeError, match='Combustível inválido. O combustível deve ser do tipo Combustivel.'):
        test_quatro_bombaUm.associar_combustivel('Gasolina')
    
def test_combustivel():
    test_cinco_combustivel = Combustivel('gasolina', 5)
    assert test_cinco_combustivel._nome == 'Gasolina'
    assert test_cinco_combustivel._preco_por_litro == 5
    
    with pytest.raises(ValueError, match='Nome inválido. O nome deve ser "Gasolina" ou "Etanol".'):
        Combustivel('Gas', 5.5)
    with pytest.raises(ValueError, match='Preço por litro deve ser maior que zero.'):
        Combustivel('Gasolina', -5.5)
    with pytest.raises(TypeError, match='Preço por litro deve ser um float ou inteiro.'):
        Combustivel('Etanol', '10')
    with pytest.raises(NotImplementedError, match='Método não implementado na superclasse'):
        test_cinco_combustivel.calcular_valor(10)
    
def test_gasolina():
    test_seis_gasolinaAditivada = Gasolina(5.5, 'SIM')
    assert test_seis_gasolinaAditivada._nome == 'Gasolina'
    assert test_seis_gasolinaAditivada._preco_por_litro == 5.5
    assert test_seis_gasolinaAditivada._aditivada == True
    
    test_seis_gasolinaNaoAditivada = Gasolina(5, 'NÃO')
    assert test_seis_gasolinaAditivada._nome == 'Gasolina'
    assert test_seis_gasolinaNaoAditivada._preco_por_litro == 5
    assert test_seis_gasolinaNaoAditivada._aditivada == False
    
    with pytest.raises(ValueError, match='Aditivada deve ser "Sim" ou "Não".'):
        Gasolina(5.5, 'nao')
    with pytest.raises(TypeError, match='Preço por litro deve ser um float ou inteiro.'):
        Gasolina('10', 'sim')
    with pytest.raises(ValueError, match='Preço por litro deve ser maior que zero.'):
        Gasolina(-5.5, 'não')
        
def test_etanol():
    test_sete_etanolMilho = Etanol(5, 'milho')
    assert test_sete_etanolMilho._nome == 'Etanol'
    assert test_sete_etanolMilho._preco_por_litro == 5
    assert test_sete_etanolMilho._origem == 'Milho'
    
    test_sete_etanolNaoMilho = Etanol(5.5, 'cana de açucar')
    assert test_sete_etanolNaoMilho._nome == 'Etanol'
    assert test_sete_etanolNaoMilho._preco_por_litro == 5.5
    assert test_sete_etanolNaoMilho._origem == 'Cana de açucar'
    
    with pytest.raises(TypeError, match='Preço por litro deve ser um float ou inteiro.'):
        Etanol('10', 'milho')
    with pytest.raises(ValueError, match='Origem inválida. A origem deve ser "Cana de açucar" ou "Milho".'):
        Etanol(5, 'cevada')
        
def test_gasolina_e_etanol_calcular_valor():
    test_oito_gasolinaNaoAditivada = Gasolina(5, 'NÃO')
    assert test_oito_gasolinaNaoAditivada.calcular_valor(10) == 50
    assert test_oito_gasolinaNaoAditivada.calcular_valor(5) == 25
    
    test_oito_gasolinaAditivada = Gasolina(5.5, 'SIM')
    assert test_oito_gasolinaAditivada.calcular_valor(15) == 82.5
    assert test_oito_gasolinaAditivada.calcular_valor(5) == 27.5
    
    test_oito_etanolMilho = Etanol(6, 'Milho')
    assert test_oito_etanolMilho.calcular_valor(10) == 60
    assert test_oito_etanolMilho.calcular_valor(5) == 30
    
    test_oito_etanolCana_de_acucar = Etanol(6.5, 'Cana de açucar')
    assert test_oito_etanolCana_de_acucar.calcular_valor(15) == 97.5
    assert test_oito_etanolCana_de_acucar.calcular_valor(5) == 32.5

def test_abastecimento_e_resumo_abastecimento():
    BombaDeCombustivel.contadorId = 0
    test_nove_bombaUm = BombaDeCombustivel()
    test_nove_Gasolina = Gasolina(5, 'sim')
    test_nove_bombaUm.associar_combustivel(test_nove_Gasolina)
    
    test_nove_abastecimento = Abastecimento(test_nove_bombaUm, 5)
    assert test_nove_abastecimento._bomba == test_nove_bombaUm
    assert test_nove_abastecimento._combustivel == test_nove_Gasolina
    assert test_nove_abastecimento._qtd_litros == 5
    assert test_nove_abastecimento._valor == 25
    
    assert test_nove_abastecimento.resumo_abastecimento() == 'Abastecimento na bomba 1: 5 litros -> R$ 25.00'
    
    with pytest.raises(TypeError, match='Bomba inválida. A bomba deve ser do tipo BombaDeCombustivel.'):
        Abastecimento(test_nove_Gasolina, 5)
    with pytest.raises(TypeError, match='Quantidade de litros deve ser um float ou inteiro.'):
        Abastecimento(test_nove_bombaUm, '5')
    with pytest.raises(ValueError, match='Quantidade de litros deve ser maior que zero.'):
        Abastecimento(test_nove_bombaUm, -5)

def test_abastecer_e_registrar_abastecimento():
    BombaDeCombustivel.contadorId = 0
    test_dez_controle = Controle_De_Abastecimentos()
    test_dez_bombaUm = BombaDeCombustivel()
    test_dez_combustivelGas = Gasolina(5, 'sim')
    test_dez_bombaUm.associar_combustivel(test_dez_combustivelGas)
    test_dez_abastecimento = Abastecimento(test_dez_bombaUm, 20)
    
    assert test_dez_bombaUm.abastecer(10, test_dez_controle) == 'Realizando abastecimento na bomba 1: 10 litros...\nTotal a pagar: R$ 50.00'
    assert test_dez_controle.registrar_abastecimento(test_dez_abastecimento) == 'Realizando abastecimento na bomba 1: 20 litros...\nTotal a pagar: R$ 100.00'

    with pytest.raises(TypeError, match='Controle inválido. O controle deve ser da classe Controle_De_Abastecimento'):
        test_dez_bombaUm.abastecer(10, test_dez_abastecimento)
    
def test_resumo_abastecimentos_e_valor_total_abastecimentos(capsys):
    BombaDeCombustivel.contadorId = 0
    test_onze_controle = Controle_De_Abastecimentos()
    test_onze_bombaUm = BombaDeCombustivel()
    test_onze_combustivelGas = Gasolina(5.5, 'sim')
    test_onze_bombaUm.associar_combustivel(test_onze_combustivelGas)
    test_onze_controle.registrar_abastecimento(Abastecimento(test_onze_bombaUm, 5))
    test_onze_controle.registrar_abastecimento(Abastecimento(test_onze_bombaUm, 10))
    test_onze_controle.registrar_abastecimento(Abastecimento(test_onze_bombaUm, 15))

    test_onze_bombaDois = BombaDeCombustivel()
    test_onze_etanol = Etanol(6, 'milho')
    test_onze_bombaDois.associar_combustivel(test_onze_etanol)
    test_onze_controle.registrar_abastecimento(Abastecimento(test_onze_bombaDois, 10))
    test_onze_controle.registrar_abastecimento(Abastecimento(test_onze_bombaDois, 15))
    
    test_onze_controle.resumo_abastecimentos()
    resumo_abastecimentos = capsys.readouterr()
    # assert resumo_abastecimentos.out.strip()  == 'Resumo dos abastecimentos:\n- Bomba 1 (Gasolina Aditivada): 5 litros -> R$ 27.50\n- Bomba 1 (Gasolina Aditivada): 10 litros -> R$ 55.00\n- Bomba 1 (Gasolina Aditivada): 15 litros -> R$ 82.50'
    
    assert test_onze_controle._valor_total_abastecimentos == 315.0

def test_aaa():
    test_doze_posto = PostoDeCombustivel('Ipiranga')
    assert test_doze_posto._nome == 'Ipiranga'

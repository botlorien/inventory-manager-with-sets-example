
class InventoryManager:

    def __init__(self) -> None:
        self._produtos_disponiveis = set()
        self._produtos_vendidos = set()
        self._produtos_danificados = set()

    def __repr__(self) -> str:
        return f'InventoryManager(produtos_disponiveis={self._produtos_disponiveis}, produtos_vendidos={self._produtos_vendidos}, produtos_danificados={self._produtos_danificados})'

    def adicionar_produto(self,nome:str):
        if isinstance(nome,str):
            self._produtos_disponiveis.add(nome)
        else:
            raise TypeError(
                f"Invalid type for nome: {type(nome)}. Expected {type(str())}"
            )

    def registrar_venda(self,nome:str):
        if isinstance(nome,str) and nome in self._produtos_disponiveis:
            self._produtos_vendidos.add(nome)
        else:
            raise TypeError(
                f"Invalid type for nome or nome not in produtos disponiveis: {type(nome)}. Expected {type(str())}"
            )

    def registrar_dano(self,nome:str):
        if isinstance(nome,str) and nome in self._produtos_disponiveis:
            self._produtos_danificados.add(nome)
        else:
            raise TypeError(
                f"Invalid type for nome or nome not in produtos disponiveis: {type(nome)}. Expected {type(str())}"
            )
    def verificar_disponibilidade(self, nome:str):
        return nome in self._produtos_disponiveis

    def inventario_total(self):
        return self._produtos_vendidos | self._produtos_danificados | self._produtos_disponiveis

    def produtos_nao_vendidos_ou_danificados(self):
        return self._produtos_disponiveis - (self._produtos_danificados | self._produtos_vendidos)

    def produtos_unicos_vendidos_ou_danificados(self):
        return self._produtos_vendidos ^ self._produtos_danificados
    

if __name__=='__main__':
    # Criando uma instancia
    inventory = InventoryManager()

    # Adicionando produtos
    inventory.adicionar_produto('Arroz')
    inventory.adicionar_produto('Feijão')
    inventory.adicionar_produto('Macarrão')

    # Exibindo a representação da classe
    print("Repr da classe depois de adicionar os produtos: ",inventory)

    # Registrando uma venda
    inventory.registrar_venda('Arroz')

    # Registrando um dano
    inventory.registrar_dano('Feijão')

    # Exibindo a representação da classe
    print('Repr da classe depois de registrar venda e dano: ',inventory)
    

    # Exibindo o inventario total
    print('Inventario total: ',inventory.inventario_total())

    # Exibindo produtos não vendidos ou danificados
    print('Produtos não vendidos ou danificados: ',inventory.produtos_nao_vendidos_ou_danificados())

    # Exibindo produtos unicos vendidos ou danificados
    print('Produtos unicos vendidos ou danificados: ',inventory.produtos_unicos_vendidos_ou_danificados())
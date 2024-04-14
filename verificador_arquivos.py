import os


"""
Essa classe faz o o gerenciamento dos arquivos xml
precisa ser indicado um caminho
retorna  uma lista de nomes dos arquivos .xml presentes no diretorio informado.
"""
    
    
class Gerenciador_Arquivos:
    
    def __init__(self, caminho):
        """Inicia a classe com a variavel caminho para a pasta com os xmls."""
        self.caminho = caminho
        
    def lista_arquivos_xml(self):
        """Retorna todos os arquivos .xml do caminho, diretorio, path em uma lista."""
        
        #Verifica se o caminho é valido 1 erro
        if not os.path.exists(self.caminho) or not os.path.isdir(self.caminho):
            raise ValueError("Caminho invalido")
            
        #Listando todos os arquivos do diretório com list comprehension condicional
        arquivos_xml = [file for file in os.listdir(self.caminho) if file.endswith('.xml')]
        
        # 2 possivel erro
        if not arquivos_xml:
            raise ValueError("Não foram encontrados arquivos XML no diretório.")
        
        return arquivos_xml
    


if  __name__ == "__main__":
    teste = Gerenciador_Arquivos(r"F:\Area de trabalho antiga\Área de Trabalho\xml reader\xml  reader\XML")
print(teste.lista_arquivos_xml())

import os
import xml.etree.ElementTree as ET
#todo: make it with lxml instead of ElementTree later to test it.
class Processador_XML:
    def processar_arq(self, caminho): 
        if not os.path.exists(caminho):
            raise FileNotFoundError("O arquivo especificado não existe")
        tree = ET.parse(caminho)  # lê o arquivo XML e cria uma árvore de elementos
        print(tree)
        root = tree.getroot()    # pega a raiz da árvore (elemento principal do documento)
        
        #return self._extrair_dados(root)   # chama o método que realmente faz a extração dos dados
        # Definindo o namespace
        ns = {'nfe': 'http://www.portalfiscal.inf.br/nfe'}
        
        # Busca todos os itens detalhados na nota
        itens = root.findall('.//nfe:det', ns)
        # Usando o namespace nas buscas
        emit = root.find('.//nfe:emit', ns)
        dest = root.find('.//nfe:dest', ns)
        for item in itens:
            self._extrair_dados(item, ns)

        
        if not itens:
            print("Nenhum item encontrado no documento XML.")
            return

        if emit is None or dest is None:
            print("Elementos emitente ou destinatário não encontrados no documento XML.")
            return
        
        # Extraindo informações
        xNome_emit = emit.find('nfe:xNome', ns).text if emit.find('nfe:xNome', ns) is not None else 'Não disponível'
        xLgr_emit = emit.find('nfe:enderEmit/nfe:xLgr', ns).text if emit.find('nfe:enderEmit/nfe:xLgr', ns) is not None else 'Não disponível'
        fone_emit = emit.find('nfe:enderEmit/nfe:fone', ns).text if emit.find('nfe:enderEmit/nfe:fone', ns) is not None else 'Não disponível'

        xNome_dest = dest.find('nfe:xNome', ns).text if dest.find('nfe:xNome', ns) is not None else 'Não disponível'
        xLgr_dest = dest.find('nfe:enderDest/nfe:xLgr', ns).text if dest.find('nfe:enderDest/nfe:xLgr', ns) is not None else 'Não disponível'
        fone_dest = dest.find('nfe:enderDest/nfe:fone', ns).text if dest.find('nfe:enderDest/nfe:fone', ns) is not None else 'Não disponível'

        print(f"Nome Emitente: {xNome_emit}")
        print(f"Logradouro Emitente: {xLgr_emit}, Telefone: {fone_emit}")
        print(f"Nome Destinatário: {xNome_dest}")
        print(f"Logradouro Destinatário: {xLgr_dest}, Telefone: {fone_dest}")
        print("------------------------------")


    def _extrair_dados(self,  item, ns):
        """
        Extrai os dados do produto e os dados de imposto do item fornecido.
        """
        dados = {}

        produto = item.find('nfe:prod', ns)
        imposto = item.find('nfe:imposto', ns)

        cProd = produto.find('nfe:cProd', ns).text
        xProd = produto.find('nfe:xProd', ns).text
        NCM = produto.find('nfe:NCM', ns).text
        CFOP = produto.find('nfe:CFOP', ns).text
        uCom = produto.find('nfe:uCom', ns).text
        qCom = produto.find('nfe:qCom', ns).text
        vUnCom = produto.find('nfe:vUnCom', ns).text
        vProd = produto.find('nfe:vProd', ns).text
        vTotTrib = imposto.find('.//nfe:vTotTrib', ns).text if imposto.find('.//nfe:vTotTrib', ns) is not None else '0.00'

        print(f"Produto: {xProd}")
        print(f"  Código: {cProd}, NCM: {NCM}, CFOP: {CFOP}")
        print(f"  Unidade Comercial: {uCom}, Quantidade: {qCom}, Valor Unitário: {vUnCom}")
        print(f"  Valor Total Produto: {vProd}, Valor Total Tributos: {vTotTrib}")
        print("------------------------------------------------------------")
        
        

#Cria um objeto, instancia, da class Processador_XML e chama a função para processamento de XMLs
# processador = Processador_XML()
# processador.processar_arq(r"53190500652008000132550000000932741000932747.xml")
if __name__ == "__main__":
    caminho = r"C:\Users\diogo\OneDrive\Documentos\xmls\32190602627042000182550010000100191301330511.xml"
    processador = Processador_XML()
    processador.processar_arq(caminho)






    
    
    
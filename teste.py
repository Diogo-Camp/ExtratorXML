import os
import xml.etree.ElementTree as ET

class Processador_XML:
    def processar_arq(self, caminho): 
        tree = ET.parse(caminho)  # lê o arquivo XML e cria uma árvore de elementos
        root = tree.getroot()    # pega a raiz da árvore (elemento principal do documento)
        
        # Namespace usado no XML da NF-e
        ns = {'nfe': 'http://www.portalfiscal.inf.br/nfe'}

        # Imprimir tags e textos dos elementos da tree
        emit = root.find('.//nfe:emit', ns)
        dest = root.find('.//nfe:dest', ns)

        # Acessar 'xNome' dentro de 'emit' e 'dest'
        xNome_emit = emit.find('nfe:xNome', ns).text if emit is not None else 'N/A'
        xNome_dest = dest.find('nfe:xNome', ns).text if dest is not None else 'N/A'

        # Acessar 'enderEmit' e 'enderDest'
        enderEmit = emit.find('nfe:enderEmit', ns) if emit is not None else None
        enderDest = dest.find('nfe:enderDest', ns) if dest is not None else None

        # Exemplos de como acessar os dados (verificar se o elemento existe)
        xLgr_emit = enderEmit.find('nfe:xLgr', ns).text if enderEmit is not None else 'N/A'
        xBairro_emit = enderEmit.find('nfe:xBairro', ns).text if enderEmit is not None else 'N/A'
        xPais_emit = enderEmit.find('nfe:xPais', ns).text if enderEmit is not None else 'N/A'
        fone_emit = enderEmit.find('nfe:fone', ns).text if enderEmit is not None else 'N/A'

        xLgr_dest = enderDest.find('nfe:xLgr', ns).text if enderDest is not None else 'N/A'
        xBairro_dest = enderDest.find('nfe:xBairro', ns).text if enderDest is not None else 'N/A'
        xPais_dest = enderDest.find('nfe:xPais', ns).text if enderDest is not None else 'N/A'
        fone_dest = enderDest.find('nfe:fone', ns).text if enderDest is not None else 'N/A'

        print(f"Nome Emitente: {xNome_emit}")
        print(f"Logradouro Emitente: {xLgr_emit}, Bairro: {xBairro_emit}, País: {xPais_emit}, Telefone: {fone_emit}")
        print(f"Nome Destinatário: {xNome_dest}")
        print(f"Logradouro Destinatário: {xLgr_dest}, Bairro: {xBairro_dest}, País: {xPais_dest}, Telefone: {fone_dest}")
        for emit in root.iterfind('.//nfe:emit', namespaces={'nfe': 'http://www.portalfiscal.inf.br/nfe'}):
            # Processa cada elemento 'emit'
            print(emit)
# Usar o caminho correto do arquivo XML
caminho_arquivo = r"53190500652008000132550000000932741000932747.xml"
processador = Processador_XML()
processador.processar_arq(caminho_arquivo)

"""
O uso de namespaces em XML é uma forma de evitar conflitos de nomes em documentos XML que podem conter elementos com o mesmo nome, mas com significados diferentes. Eles funcionam como prefixos que ajudam a distinguir elementos que pertencem a diferentes vocabulários ou aplicações.
"""
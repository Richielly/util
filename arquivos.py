import os
import patoolib


def descompactar_arquivos(diretorio_raiz):
    # Verificar se o diretório informado existe
    if not os.path.exists(diretorio_raiz):
        print("O diretório informado não existe!")
        return

    # Percorrer o diretório raiz e suas subpastas
    for dirpath, dirnames, filenames in os.walk(diretorio_raiz):
        for file in filenames:
            if file.endswith(('.zip', '.rar', '.7z')):
                arquivo_completo = os.path.join(dirpath, file)
                # Define o diretório de saída como nome do arquivo sem a extensão
                diretorio_saida = os.path.join(dirpath, os.path.splitext(file)[0])

                # Se o diretório de saída não existir, crie-o
                if not os.path.exists(diretorio_saida):
                    os.makedirs(diretorio_saida)

                try:
                    print(f"Descompactando: {arquivo_completo}")
                    patoolib.extract_archive(arquivo_completo, outdir=diretorio_saida)
                except Exception as e:
                    print(f"Erro ao descompactar {arquivo_completo}. Erro: {e}")


# Testando
descompactar_arquivos(r"C:\Users\Equiplano\Downloads\SimAm")

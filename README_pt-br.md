<div align='center'>

![Cat Code Logo](doc/thumb.png)  
[Início](README.md)

## ◈ Como instalar
Rode o seguinte comando no seu terminal linux:

<div align='left'>

  ```shell
    $ mkdir ~/my-path; cd ~/my-path        # criando um path para seus comandos
    $ git clone https://github.com/pandasoli/cat-code.git # download do projeto
    $ mv cat-code/src/* .; rm -r -f cat-code # deixando tudo na pasta do path
    $ mv main.py catc                       # renomeando arquivo principal
    $ chmod +x ./catc                       # deixando-o executável
  ```
</div>

Depois disso você precisa adicionar a pasta que vc criou no path do sistema.  
Então no fianl do arquivo ~/.profile escreva:
<div align='left'>

  ```sh
    # MINE

    if [ -b "$HOME/my-path" ] ; then
      PATH="$HOME/my-path:$PATH"
    fi
  ```
</div>
<br/>

## ◈ Como usar
Agora apenas rode o comando:

<div align='left'>

  ```sh
    catc file.yml # ...arquivos
  ```
</div>
<br/>

## ◈ Como criar sua propria highlight
Na pasta /langs é onde ficam os arquivos de configuração  
de cada linguagem, todos tem a extenssão .yml.

Seu padrão deve ser:

<div align='left'>

  ```yml
    colors: # opcional
      # suas variaveis de cor
      red: 31
      blue: 34

    regexes:
      - color: 'red'      # chamando uma variavel de cor
        regex:            # isso pode ser uma lista ou não
          - '\bfalse'
          - '\btrue'

      - color: 34         # cor azul (não chama uma variavel)
        regex: '[a-zA-Z]'
  ```
</div>

Se a sua linguagem tem mais de uma extenssão, no arquivo  
extensions.yml ponha isso:

<div align='left'>

  ```yml
    # "extensão": "nome do arquivo .yml criado em /langs"
    # OBS: não é necessário o nome do arquivo.
    c: cpp
    h: cpp
  ```
</div>
</div>
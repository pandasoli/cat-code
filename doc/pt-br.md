<div align='center'>

![Cat Code Logo](doc/thumb.png)  
[Início](README.md)

## ◈ Como instalar
Rode os seguintes comandos no seu terminal linux:

<div align='left'>

  ```shell
    $ cd cat-code
    $ chmod +x ./mach.sh
    $ ./make.sh
  ```
</div>
<br/>

## ◈ Como usar
Agora apenas rode o comando:

<div align='left'>

  ```sh
    catc <...arquivos>
  ```
</div>

Se você quiser ler um arquivo com outra syntax:
<div align='left'>

  ```sh
    catc file.yml:json # arquivo:syntax
  ```
</div>
<br/>

## ◈ Como criar sua propria highlight
Na pasta /langs é onde ficam os arquivos de configuração  
de cada linguagem, todos tem a extenssão .yml.

Seu padrão deve ser:

<div align='left'>

  ```yml
    keyword: (let|const|return)
    math-char: (<|>|\+|\-|\*|\/|\%|\=|\:|\.|\,|\||\&|\w+:)
    bracket: (\[|\]|\{|\}|\(|\))
    string: ('.*'|".*"|`.*`)
    number: \\b[0-9e_]+(?:\.[0-9e_]+)?
    important: (this)
    comment: (//.+|/\*[a-zA-Z\n ]+\*/)
    identifier: '\w+'
    space: '( |\n)'
  ```
</div>

O arquivo `config.yml` server para temas e para se a  
sua linguagem tem mais de uma extenssão, a syntax  
desse arquivo é assim:

<div align='left'>

  ```yml
    theme: 'nordic-darker'
    extensions:
      c: cpp
      h: cpp
      hpp: cpp
  ```
</div>
</div>
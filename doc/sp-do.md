<div align='center'>

![Cat Code Logo](doc/thumb.png)  
[Comienzo](README.md)

## ◈ Como instalar
Ejecutes los seguintes comandos en tu terminal linux:

<div align='left'>

  ```shell
    $ cd cat-code
    $ chmod +x ./mach.sh
    $ ./make.sh
  ```
</div>
<br/>

## ◈ Como utilizar
Ahora solo ejecutes el comando:

<div align='left'>

  ```sh
    catc <...archivos>
  ```
</div>

Si quieres leer un archivo con otra syntax:
<div align='left'>

  ```sh
    catc file.yml:json # archivo:syntax
  ```
</div>
<br/>

## ◈ Como crear tu propia highlight
En la carpeta /langs es donde están los archivos de configuración  
de cada linguaje, todos tienen la extensión .yml.

Su patrón debe ser:

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

<!-- Si tu linguaje tiene más que una extensión, en el archivo  
extensions.yml ponha eso: -->
El archivo `config.yml` sirve para temas y para si  
tu linguaje tiene mais de una extension, la syntax  
desto archivo es así:

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
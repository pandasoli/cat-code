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
    catc file.yml # ...archivos
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
    colors: # tus variables de color
      blue: 34

    groups:
      # color verde (no llama una variable)
      - color: 32
        # tu regex
        regex: '"[a-zA-Z0-9\\_-]+"'
        # opcional - una lista de regexes
        regexes:
          - '"[a-zA-Z0-9\\_-]+"'
          - "'[a-zA-Z0-9\\\\_-]+'"
        # groups hijos
        children:
          # llamando una variavel de color
          - color: blue
            regexes:
              - '\\n'
              - '\\t'
  ```
</div>

Si tu linguaje tiene más que una extensión, en el archivo  
extensions.yml ponha eso:

<div align='left'>

  ```yml
    # "extensión": "nombre del archivo .yml creado en /langs"
    # OBS: no es necesário lo nombre del archivo.
    c: cpp
    h: cpp
  ```
</div>
</div>
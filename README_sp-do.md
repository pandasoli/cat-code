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
<br/>

## ◈ Como crear tu propia highlight
En la carpeta /langs es donde están los archivos de configuración  
de cada linguaje, todos tienen la extensión .yml.

Su patrón debe ser:

<div align='left'>

  ```yml
    colors: # opcional
      # tus variables de color
      red: 31
      blue: 34

    regexes:
      - color: 'red'      # llamando a una variable de color
        regex:            # eso puede ser una lista o no
          - '\bfalse'
          - '\btrue'

      - color: 34         # color azul (no llama a una variable)
        regex: '[a-zA-Z]'
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
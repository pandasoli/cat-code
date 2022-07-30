<div align='center'>

![Cat Code Logo](doc/thumb.png)  
[Home](README.md)

## ◈ How to install
Run the following commands on your linux terminal:

<div align='left'>

  ```shell
    $ cd cat-code
    $ chmod +x ./mach.sh
    $ ./make.sh
  ```
</div>
<br/>

## ◈ How to use
Now just run the command:

<div align='left'>

  ```sh
    catc file.yml # ...files
  ```
</div>

If you can read a file with another syntax:
<div align='left'>

  ```sh
    catc file.yml:json # file:syntax
  ```
</div>
<br/>

## ◈ How to create your own highlight
In the /langs folder is where stay the configuration files  
of each language, all they have the .yml extenssion.

Its template must be:

<div align='left'>

  ```yml
    colors: # optional
      # your color variables
      blue: 34

    regexes:
      - color: blue          # calling a color variable
      regexes:               # this can be a list or not
        - '\\n'
        - '\\t'

    - color: 32                   # green color (doesn't call a variable)
      rewrite: False              # clear de colors inside
      regex: '"[a-zA-Z0-9\\_-]+"'
  ```
</div>

If your language has more than one extenssion, in the file  
extensions.yml put this:

<div align='left'>

  ```yml
    # "extenssion": "name of the .yml file created at /langs"
    # OBS: it's not necessary the file name.
    c: cpp
    h: cpp
  ```
</div>
</div>
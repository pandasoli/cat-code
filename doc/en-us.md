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
    catc <...files>
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

The `config.yml` file is for the themes and if your  
your language has more than one extenssion, the syntax  
of this file is thus:

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
<div align='center'>

![Cat Code Logo](doc/thumb.png)  
[Home](README.md)

## ◈ How to install
Run the following command on your linux terminal:

<div align='left'>

  ```shell
    $ mkdir ~/my-path; cd ~/my-path       # creating a path for yout commands
    $ git clone https://github.com/pandasoli/cat-code.git  # download project
    $ mv cat-code/src/* .; rm -r -f cat-code # putting all in the path folder
    $ mv main.py catc                     # renaming main file
    $ chmod +x ./catc                     # turning executable
  ```
</div>

After this you need to add the folder you created to the system path.  
So in the end of the file ~/.profile write:
<div align='left'>

  ```sh
    # MINE

    if [ -b "$HOME/my-path" ] ; then
      PATH="$HOME/my-path:$PATH"
    fi
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
<br/>

## ◈ How to create your own highlight
In the /langs folder is where stay the configuration files  
of each language, all they have the .yml extenssion.

Its template must be:

<div align='left'>

  ```yml
    colors: # optional
      # your color variables
      red: 31
      blue: 34

    regexes:
      - color: 'red'      # calling a color variable
        regex:            # this can be a list or not
          - '\bfalse'
          - '\btrue'

      - color: 34         # blue color (doesn't call a variable)
        regex: '[a-zA-Z]'
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
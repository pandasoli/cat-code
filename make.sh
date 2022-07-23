#!/bin/bash

instalation() {
  # ◈ Folder my-path
  if [ -f "~/my-path" ]; then
    mkdir ~/my-path
  fi

  # ◈ Folder cat-code at my-path
  if [ -d "~/my-path/cat-code" ]; then
    rm -r -f ~/my-path/cat-code/*
  elif [ -f "~/my-path/cat-code" ]; then
    mkdir ~/my-path/cat-code
  fi

  # ◈ Moving files
  cp -r src/* ~/my-path/cat-code/
  mv ~/my-path/cat-code/main.py ~/my-path/cat-code/catc

  # ◈ Turning executable
  chmod +x ~/my-path/cat-code/catc

  # ◈ Writting .profile
  profile_lines=(
    ''
    '# 🐈 Cat Code 🖤'
    "if [ -d \"\$HOME/my-path/cat-code\" ]; then"
    "  PATH=\"\$HOME/my-path/cat-code:\$PATH\""
    'fi'
    ''
  )

  for line in "${profile_lines[@]}"; do
   echo $line >> "$HOME/.profile"
  done
}

success() {
  echo -e '\033[1;32m◈ Installation completed\033[0m'
  PATH="$HOME/my-path/cat-code:$PATH"
}

error() {
  echo -e '\033[1;31m◈ Installation not completed\033[0m'
  echo -e "  \033[31mI don't know what the fuck was going on 🤔\033[0m"
}


echo ''
echo -e '🐈 \033[1;32mCat Code\033[0m 🖤'
echo ''
(instalation) && (success) || (error)
echo ''

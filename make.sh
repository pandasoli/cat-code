
if [ -f "~/my-path" ]; then
  mkdir ~/my-path
fi

if [ -d "~/my-path/cat-code" ]; then
  rm -r -f ~/my-path/cat-code/*
else
  mkdir ~/my-path/cat-code
fi

cp -r src/* ~/my-path/cat-code/
mv ~/my-path/cat-code/main.py ~/my-path/cat-code/catc

chmod +x ~/my-path/cat-code/catc

echo "if [ -d \"\$HOME/my-path/cat-code\" ]; then" >> "$HOME/.profile"
echo "  PATH=\"\$HOME/my-path/cat-code:\$PATH\"" >> "$HOME/.profile"
echo "fi" >> "$HOME/.profile"

$example = Read-Host -Prompt "nom dossier"

cd $HOME

mkdir $example

cd $example

git clone https://github.com/KeligMartin/4-SRC.git
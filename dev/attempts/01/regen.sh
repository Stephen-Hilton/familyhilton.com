python3 -m venv sitegen/venv_01
source sitegen/venv_01/bin/activate
pip install pyyaml jinja2 markdown
pip install --upgrade pip

python3 -m sitegen build --root ./root  # writes /root/index.html and /root/pages/**


cp -r root/* ../../../ # copy to parent directory

python3 -m http.server 8000 --directory ../../../

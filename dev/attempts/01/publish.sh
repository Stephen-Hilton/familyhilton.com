python3 -m venv sitegen/venv_01
source sitegen/venv_01/bin/activate
pip install pyyaml jinja2 markdown
pip install --upgrade pip

python3 -m sitegen build --root ./root  # writes /root/index.html and /root/pages/**

export PUBPATH="../../../docs"
mkdir -p ${PUBPATH}        # create parent directory if it doesn't exist
setopt rm_star_silent
rm -rf ${PUBPATH}/*     # clear parent directory (to trash)
cp -R root/* ${PUBPATH} # copy to parent directory

# push to github
git add ${PUBPATH}
git add root
git commit -m "update site with new content"
git push -u origin main
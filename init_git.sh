rm -rf .git
git init
git config user.name 'IntelligentComputing'
git config user.email '<>'
git add .
git commit -m 'init'
git remote add origin git@github.com:intcomp/vlkit
git push -u origin main -f

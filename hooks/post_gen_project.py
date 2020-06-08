from os.path import exists
import subprocess

dir2ps={'docs':['paper','presentations'],
        'data':['data_analysed','data_exp','database'],
        'code':['test','deps'],
       }
dir2info={'docs':'`docs`  \nThis directory contains the manuscripts and presentations.',
        'data':'`data`  \nThis directory contains raw data either retrieved from databases or generated from wet-lab experiments',
        'code':'`code`  \nThis directory contains a git repository which is version controlled.',
        }

for dir1p in dir2ps:
    [subprocess.call(f"mkdir -p {dir1p}/{dir2p}",shell=True) for dir2p in dir2ps[dir1p]]

for dir1p in dir2info:
    with open(f"{dir1p}/README.md", 'w') as f:
        f.write(dir2info[dir1p])    

## 1 make 2 analysis directories
from cookiecutter.main import cookiecutter
cookiecutter('https://github.com/rraadd88/template_repo.git',
             no_input=True,
             output_dir='code',
             extra_context={'repo_name': '{{ cookiecutter.repo_name }}'},
            )
## 2 symlinks
coms=[
    'echo "ln -s ../../../data" > code/{{ cookiecutter.repo_name }}/{{ cookiecutter.repo_name }}/create_symlinks.sh',
    'echo "ln -s ../../../../../var" >> code/{{ cookiecutter.repo_name }}/{{ cookiecutter.repo_name }}/create_symlinks.sh',
    'echo "ln -s ../../database" > data/create_symlinks.sh',
]
[subprocess.call(s,shell=True) for s in coms]
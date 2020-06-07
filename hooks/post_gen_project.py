from os.path import exists
import subprocess

dir2ps={'docs':['paper','presentations'],
        'data':['data_analysed','data_wet_lab','database'],
        'code':['notebooks'],
       }
dir2info={'docs':'`docs`  \nThis directory contains the manuscripts and prensentations.',
        'data':'`data`  \nThis directory contains raw data either retrieved from databases for generated from wet-lab experiments :muscle-emoji.',
        'code':'`code`  \nThis directory contains  \n1. raw codes (could be jupyter notebooks etc) stored in stepwise manner in numbered directories (eg. `00_something`) and  \n2. a git repository which is version controlled (obviously!).',
        }

for dir1p in dir2ps:
    [subprocess.call(f"mkdir -p {dir1p}/{dir2p}",shell=True) for dir2p in dir2ps[dir1p]]

for dir1p in dir2info:
    with open(f"{dir1p}/README.md", 'w') as f:
        f.write(dir2info[dir1p])    
        
## 1 make 2 analysis directories
subprocess.call("cd code;cookiecutter https://github.com/rraadd88/template_repo.git",shell=True)
        
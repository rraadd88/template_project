from os.path import exists
import subprocess
## 1 make 2 analysis directories
subprocess.call("cookiecutter --no-input https://github.com/rraadd88/template_code.git",shell=True)

dir2ps={'docs':['paper','presentations','method'],
		'data':['01clonning','02expression','03blahblah']}
dir2info={'docs':'`docs`  \nThis directory contains the manuscripts and prensentations.',
		'data':'`data`  \nThis directory contains raw data either retrieved from databases for generated from wet-lab experiments :muscle-emoji.',
		'code':'`code`  \nThis directory contains  \n1. raw codes (could be jupyter notebooks etc) stored in stepwise manner in numbered directories (eg. `00_something`) and  \n2. a git repository which is version controlled (obviously!).',
		}		

for dir1p in dir2ps:
    [subprocess.call(f"mkdir -p {dir1p}/{dir2p}",shell=True) for dir2p in dir2ps[dir1p]]

for dir1p in dir2info:
	with open(f"{dir1p}/README.md", 'w') as f:
		f.write(dir2info[dir1p])    
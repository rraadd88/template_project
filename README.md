# template_project
This template for organising project files is roughly based on [A Quick Guide to Organizing Computational Biology Projects](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1000424)

## directory structure

    project_name/
    ├── data
    │   ├── data_exp
    │   ├── database -> ../../    
    │   ├── data_analysed
    │   ├── data_analysed.yml (cfg)
    │   └── README.md
    ├── code
    │   └── {repo_name} (contains scripts)
    │       ├── {repo_name}
    │       │   ├── 00_annot_v01.ipynb
    │       │   ├── 01_exp_v01.ipynb
    │       │   ├── get00_annot_v01.py
    │       │   ├── get01_exp_v01.py
    │       │   ├── get98_plots.py
    │       │   ├── get99_figures.py
    │       │   ├── run.py
    │       │   ├── figs 
    │       │   ├── plot 
    │       │   ├── data_si 
    │       │   ├── cfg_figures.yml
    |       |   ├── data -> ../../
    │       |   └── var -> ../../../var (contains logos)
    │       ├── requirements.txt
    │       ├── environment.yml
    │       ├── README.md
    │       └── setup.py
    ├── docs
    │   ├── method
    │   ├── paper
    │   ├── presentations
    │   └── README.md
    └── README.md

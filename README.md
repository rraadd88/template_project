# template_project
This template for organising project files is roughly based on [A Quick Guide to Organizing Computational Biology Projects](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1000424)

## directory structure

	project_name/
	├── code
	│   ├── notebooks
	│   │   ├── plots_v01_.ipynb
	│   │   ├── annot_v00_.ipynb
	│   │   ├── merge_v00_.ipynb
	│   │   ├── data_analysed.yml (cfg)
	│   │   ├── data -> ../../data
	|   |   |   ├── data_analysed 
	│   │   |   └── database -> database
	│   │   ├── figs 
	│   │   └── plot 
	│   ├── README.md
	│   └── repo_name (contains scripts)
	│       ├── environment.yml
	│       ├── MANIFEST.in
	│       ├── README.md
	│       ├── repo_name
	│       │   ├── cfg.yml (data_analysed.yml)
	│       │   ├── curate00_annot.py
	│       │   ├── curate01_exp.py
	│       │   ├── plots.py
	│       │   ├── figures.py
	│       ├── requirements.txt
	│       ├── setup.cfg
	│       └── setup.py
	├── data
	│   ├── 01clonning
	│   ├── 02expression
	│   ├── 03blahblah
	│   ├── data_analysed
	│   ├── data_analysed.yml (cfg)
	│   └── README.md
	├── docs
	│   ├── method
	│   ├── paper
	│   ├── presentations
	│   └── README.md
	└── README.md


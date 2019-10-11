# template_project
This template for organising project files is roughly based on [A Quick Guide to Organizing Computational Biology Projects](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1000424)

## directory structure

	project_name/
	├── code
	│   ├── 00_something
	│   │   ├── analysis_v01_.ipynb
	│   │   ├── curate_v01_.ipynb
	│   │   ├── data_ -> repo_name/repo_name/data_
	│   │   ├── data_annot -> repo_name/repo_name/data_annot
	│   │   ├── data_merge -> repo_name/repo_name/data_merge
	│   │   ├── figs -> repo_name/repo_name/figs
	│   │   └── plot -> repo_name/repo_name/plot
	│   ├── README.md
	│   └── repo_name
	│       ├── environment.yml
	│       ├── MANIFEST.in
	│       ├── README.md
	│       ├── repo_name
	│       │   ├── analysis_v00_.ipynb
	│       │   ├── cfg.yml
	│       │   ├── curate.py
	│       │   ├── curate_v01_.ipynb
	│       │   ├── data_
	│       │   ├── data_annot
	│       │   ├── data_merge
	│       │   ├── figs
	│       │   ├── figures_v00_.ipynb
	│       │   ├── global_vars.py
	│       │   ├── logplots.log
	│       │   └── plot
	│       ├── requirements.txt
	│       ├── setup.cfg
	│       └── setup.py
	├── data
	│   ├── 01clonning
	│   ├── 02expression
	│   ├── 03blahblah
	│   └── README.md
	├── docs
	│   ├── method
	│   ├── paper
	│   ├── presentations
	│   └── README.md
	└── README.md


# SPPR-DJANGO-NEW Documentation
<hr />

## Manual Installation (without environtment.yml/.txt)
  1. Installing Miniconda (using Python 3.8) 
  2. After installation, check if Miniconda(or Conda) is properly installed `conda --version`
  3. Create a Conda environment with Python 3.9 `conda create -n sppr-django-new python=3.9`
  4. Activate the environment `conda activate sppr-django-new`
  5. Install the required package:
      - Conda -> `conda install PKGNAME`
      - Pip   -> `pip install PKGNAME`

## Import Env Installation (conda [cheatsheet](https://docs.conda.io/projects/conda/en/latest/_downloads/843d9e0198f2a193a3484886fa28163c/conda-cheatsheet.pdf))
  1. Do the same step in **[Manual Installation](#manual-installation)** from 1 to 2
  2. Create a Conda environment with the environment.yml `conda env create -n sppr-django-new --file requirements.yml`

## Clone The Forked Repo (New) 
`git clone https://github.com/msultont/sppr-django-new.git`
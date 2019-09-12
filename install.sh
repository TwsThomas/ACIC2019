wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh
bash ~/miniconda.sh -b -p $HOME/miniconda
rm ~/miniconda.sh

# a mettre .bashrc
export PATH=${HOME}/miniconda/bin:${PATH}

conda update -y conda
conda create -y -n stable python=3.6 numpy scipy tensorflow scikit-learn pandas image matplotlib
conda init bash

# Restart kernel....

conda activate stable

# conda deactivate
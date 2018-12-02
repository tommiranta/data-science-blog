# Python in Power BI - Best of two worlds?
Links to blog post: [Medium](https://www.medium.com) & [LinkedIn](https://www.linkedin.com)

This blog post focused on showcasing how to use Python in Power BI. We use the [Boston Housing dataset](http://lib.stat.cmu.edu/datasets/boston) that is available from [scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_boston.html). In this example the dataset is used for clustering although it is usually used for solving regression tasks. First we use PCA to reduce the dimensions to 2 that will allow us to visualize the data in a 2-dimensional plot. Afterwards we apply K-Means clustering to identify any homogenous groups in the data. Finally this data is utilized to make visualizations in Microsoft Power BI Desktop.

## Pre-requisites
This example assumes that Power BI Desktop ([download for free](https://powerbi.microsoft.com/en-us/downloads/)) and Python + [pipenv](https://docs.pipenv.org) is installed on the system. Feel free to use a another instance of Python, you can check the required libraries from the `Pipfile`. 

## Setting up Python in Power BI
* Clone or download the repository
* Open terminal/console and navigate to the `python_in_powerbi` folder
* Run `pipenv install` to install all required packages (alternatively run with the `--dev` option to also install pep8 linter)
* Run `pipenv --venv` and take note of the location of the virtual environment
* Open Power BI Desktop and open the `Options`
 * Navigate to `Preview features`and enable `Python support` (a restart of Power BI required at this point)
 * Navigate to `Python scripting` and change the `Detected Python home directories` to `Other`
 * `Browse` to the `Scripts` folder that is found in the newly created virtual environment.
 * Click OK and you're ready for Python in Power BI!

 ## Using Python in Power BI
 Read my blog post for a step-by-step walkthrough how to use Python in Power BI.

 ## File descriptions
 * `boston_housing.pbit` - Ready to use Power BI template. You only need to make sure your Python environment is configured in Power BI
 * `boston_housing.ipynb` - Jupyter notebook, which contains the exporatory data anlysis and modeling work done to create the scripts.
 * `boston_housing.py` - Script that is used to load the dataset in Power BI
 * `heatmap_pc1.py` - Script that is used to display a heatmap of principal component 1
 * `heatmap_pc2.py` - Script that is used to display a heatmap of principal component 2

 ## Some helpful links
* 
 
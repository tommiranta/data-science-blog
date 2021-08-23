# Python in Power BI - Best of two worlds?
Links to blog post: [Medium](https://www.medium.com) & [LinkedIn](https://www.linkedin.com)

This blog post focused on showcasing how to use Python in Power BI. We use the [Boston Housing dataset](http://lib.stat.cmu.edu/datasets/boston) that is available from [scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_boston.html). In this example the dataset is used for clustering although it is usually used for solving regression tasks. First we use PCA to reduce the dimensions to 2 that will allow us to visualize the data in a 2-dimensional plot. Afterwards we apply K-Means clustering to identify any homogenous groups in the data. Finally this data is utilized to make visualizations in Microsoft Power BI Desktop.

## Pre-requisites
This example assumes that Power BI Desktop ([download for free](https://powerbi.microsoft.com/en-us/downloads/)) and Python + [pipenv](https://docs.pipenv.org) is installed on the system. Feel free to use a another instance of Python, you can check the required libraries from the `Pipfile`. 

## Setting up Python in Power BI
* Clone or download the repository
* Open Command Prompt and navigate to the `python_in_powerbi` folder
* Run `pipenv install` to install all required packages (add the `--dev` option to include pep8 linter)
* Run `pipenv --venv` and take note of the location of the virtual environment
* Open Power BI Desktop and open the `Options & Settings` > `Options`
 * Navigate to `Python scripting` and change the `Detected Python home directories` to `Other`
 * `Browse` to the `Scripts` folder that is found in the newly created virtual environment.
 * Click OK and you're ready for Python in Power BI!

 ### Use virtualenv as Python environment (optional)
 You can use virtualenv instead of pipenv to manage the Python environment for Power BI. Just replace the pipenv steps above with the following commands.
* Open the Command Prompt and navigate to the `python_in_powerbi` folder
* `python -m venv venv` to create a virtual environment
* `venv\Scripts\activate.bat` to activate the virtual environment
* `(venv) pip install -r requirements.txt` to install the Python libraries
* The path to your python environment is `<full_path_to_python_in_powerbi>\venv\Scripts` 

 ## Using Python in Power BI
 Read my blog post for a step-by-step walkthrough how to use Python in Power BI.

 ## File descriptions
 * `boston_housing.pbit` - Ready to use Power BI template. You only need to make sure your Python environment is configured in Power BI
 * `boston_housing.ipynb` - Jupyter notebook, which contains the exporatory data anlysis and modeling work done to create the scripts.
 * `boston_housing.py` - Script that is used to load the dataset in Power BI
 * `heatmap_pc1.py` - Script that is used to display a heatmap of principal component 1
 * `heatmap_pc2.py` - Script that is used to display a heatmap of principal component 2

 ## Some helpful links
* Homepage of Power BI Desktop where you can download the software - https://powerbi.microsoft.com/en-us/desktop
* Blog post showcasing various Python visualizations - https://powerbi.microsoft.com/en-us/blog/pythonblogepisode1
* Official Power BI documentation for using Python scripts - https://docs.microsoft.com/en-gb/power-bi/desktop-python-scripts
* Power BI requires ChromeDriver for visualizations whose original output is in HTML format - http://chromedriver.chromium.org/downloads
 
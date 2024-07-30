### Virtual Environment
# Create a virtual envioronment
python -m venv myenv

#Active the virtual environment in Linux
source myenv/Bin/activate

#Activate the virtual environment in Windows
myenv\Scripts\activate.bat

###################################################
# Now the "Requirements.txt" file
pip freeze > requirements.txt

#install the packages listed in the requirements.txt file
pip install -r requirements.txt



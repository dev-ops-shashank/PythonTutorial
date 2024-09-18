
# In the terminal, I entered below command to install the virtual enviorment modules:
#     pip install virtualenv
#     virtualenv myenv

# now to activate it, make sure you have the path of the 'myenv' folder, let's say it is source
#    On Unix or MacOS:
#     source myenv/bin/activate
#    On Windows:
#     myenv\Scripts\activate

# what is: pip freeze
# It returns all the packages installed in a given python env along with the versions

# pip freeze > requirements.txt 
# command will create a txt file containing all the installed packages.
# Now if you want to recreate this virtual enviroment somewhere else you just need to intall these 
# packages there using commnd:
# pip install -r .\requirements.txt 

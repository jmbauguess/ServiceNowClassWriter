# ServiceNowClassWriter
Uses web services to connect to a ServiceNow instance and copy data from the custom tables that hold model and selenium testing classes, then writes them to java files.

Run the setup.py file in the command line to install the program.

To use the program:

ServiceNowClassWriter ${username} ${password} ${instance} ${model|selenium}

If you choose model, it will look for the Model Class Creator table and generate java files of that data.
If you choose selenium, it will look for the Selenium Class Creator table and generate java files of that data.

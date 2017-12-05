To run the application, please follow the steps written below:

## Run the virtual machine!

Using the terminal, change directory to vagrant (**cd vagrant**), then type **vagrant up** to launch your virtual machine.


## Running the Item Catalog App
Once it is up and running, type **vagrant ssh**. This will log your terminal into the virtual machine, and you'll get a Linux shell prompt. When you want to log out, type **exit** at the shell prompt.  To turn the virtual machine off (without deleting anything), type **vagrant halt**. If you do this, you'll need to run **vagrant up** again before you can log into it.


Now that you have Vagrant up and running, change your current directory to the /vagrant directory by typing **cd /vagrant**. This will take you to the shared folder between your virtual machine and host machine.

Now navigate to the directory containing this project by using cd command

Now type **python database_setup.py** to initialize the database.

Type **python test_data.py** to populate the database with dummy data.

Type **python application.py** to run the Flask web server. In your browser visit **http://localhost:5000** to view the catalog app.

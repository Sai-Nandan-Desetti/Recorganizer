Installation
========================================

- It's assumed that you have the following already installed:
    - python: the language in which the app is written.
    - pip: to install python packages.    
    - git: to work with GitHub repositories.
- We don't cover how to install them here.


Install streamlit
******************
Recorganizer is built using https://streamlit.io/. So, in order to run the app, 
you need to first install streamlit.

.. code-block:: bash

    pip install streamlit


Clone the repository
*********************
Since the app is not hosted in some cloud above, you'll have to host it on your local machine. 
For which the first thing you need to do is to clone the following repository:

.. code-block:: bash

    git clone https://github.com/Sai-Nandan-Desetti/Recorganizer.git


Run the app
************
In the `Recorganizer` folder, you should see a file named `app.py`.

- Open it and enter the path to your VLC media player.
    - See the example in the documentation: https://sai-nandan-desetti.github.io/Recorganizer/app.html#example
- Save the file.
- Execute the following command:

.. code-block:: bash

    streamlit run app.py

- The app should automatically open in your browser.
- Enter the details as required and you can record the session!
- To close the app, you've to terminate it in the terminal: Press `Ctrl C`

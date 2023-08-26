app
==========

.. automodule:: app
   :members:
   :undoc-members:
   :show-inheritance:


Example
-------------

.. code-block:: python
    
    if __name__ == "__main__":    
        app = App()
        # Enter the path to your VLC player here.
        # Remember to keep forward slashes.
        vlc_path = 'D:/Apps/VLC/vlc.exe'
        app.run(vlc_path)

# Recorganizer
An app to organize video recordings generated through VLC.

## Motivation
This app was built for a very specific purpose. [SSSIHMS, PSN](https://sssihms.org/) needed a way to record snippets of medical scans (video) to capture the video input and use the `Record` functionality provided by VLC to create video snippets. These snippets were then required to be placed in a particular folder whose path was to be determined by the details of the session and, particularly, the patient.

This app is designed to collect relevant details and organize the clips created during the session into the intended folder.

## Demo
You can watch a demo on how to use the app [here](https://clipchamp.com/watch/OOBeGDEB2bq).

### Video Input
* Obviously, the video input shown in the demo is not going to be the kind doctors actually use.
* I used a pre-existing `mp4` file for the demo.
* Particularly, in the `Media` tab, I used the `Open File` option. A doctor would use something else-- `Open Capture Device` option, perhaps.
* So long as the clips created with VLC during the session are in one of the supported formats, everything should be fine.

### VLC Record
* You must've noticed in the video that when you click on `Record` in VLC, absolutely nothing seems to happen. Well, nothing noticeable anyway.
* But every odd time you click on it, a new clip starts being recorded. And, every even time you click, the recording stops and the recorded clip is stored in a location specified in your VLC `preferences`.
* In the demo, I clicked six times. So, three clips were created.

### Source Folder
* It's advised to set the settings in VLC such that, by default, the recorded clips go to the `Recordings` folder. By default, on Windows 11, they're located in the `Videos` folder. Hope the demo helps you appreciate the confusion that can arise when you use the default location.

## Installation
For the installation and documentation of the app, see [here](https://sai-nandan-desetti.github.io/Recorganizer/).

## Notes
* Once you clone this repo, you may want to delete the current contents of the `Recordings` folder which is present only for the purpose of demonstration.
* The utility of this app lies in being a preliminary step to organizing the sessions in a central database. Currently, this app works entirely on your local machine. It would be a useful future work to extend the functionality to interact with a database.

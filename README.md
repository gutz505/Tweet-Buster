# Tweet-Buster

This project involves the development of an application environment for misinformation classifier models. Specifically, the application is supposed to employ models during live browsing session on the Twitter (X) platform. The application consists of a Google Chrome browser extension and a Python implementation which hosts the trained models.

### Setup
#### Step 1
Download the 'Tweet Buster (Chrome Extension)' directory containing the background.js, content.js and manifest.json files as well as a 'Logo' directory. Open your Google Chrome Browser and navigate to the Extensions Manager. Under the section 'My Extensions' select 'Load Unpacked', then navigate to the downloaded directory and click 'Select Folder'. The browser extension is running from this moment onwards and is sending tweet-content to your local machine port (5000) whenever you access a Twitter (X) page.

#### Step 2
Download the 'tweet_buster.ipynb' notebook and familiarize yourself with the different preselected model options (documented within the notebook). Execute the code cell of your chosen model, then execute the code cell setting up the tweet-sanitization and response classes. Finally, launch the code cell which starts the Flask instance. Now you are ready to navigate to a Twitter (X) page inside your Chrome Webbrowser and see the classification results displayed to you directly inside the HTML elements.

#### Step 3
Once you are done with your browsing session on Twitter (X), make sure to manually terminate the running Flask code cell inside the Python notebook. Also uninstall the browser extension by navigating to your extension manager and clicking 'Remove' under the Tweet-Buster extension. Note that the local port communication employed by this application environment does represent a potential attack vector onto your system. Therefore it is not recommended to keep either of the extension as well as the Flask instance running for extended periods. 


### System Specifications
This application was developed and tested throughout June 2024 in the following system/software environment:
- Windows 11 Home Version 23H2
- Python 3.10.11
- Google Chrome Version 126.0.6478.114 (Official Build) (64-bit)

### GitHub Repository
Locate all resources generated throughout this project at the following link:
https://github.com/gutz505/Tweet-Buster

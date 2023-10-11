# ElvUI AutoUpdater written in python
ElvUI AutoUpdater is a python script that allows you to automatically update your ElvUI addon for world of warcraft by downloading the latest version from the official repository and replacing the old files with the new ones. 

This script is designed to simplify the process of keeping your ElvUI up to date.

## Prerequisites
Before using the ElvUI Auto-Updater, make sure you have the following requirements met:

1. You need to have Python installed on your system. 
Download and install Python from the official website:

[Python Downloads](https://www.python.org/downloads/)

3. You need to have the `requests` library installed. 
You can install it using pip:

`pip install requests`


4. ElvUI should be already installed in your world of warcraft directory, and you should know the path to your ElvUI installation.

## How to use

1. Clone or download this repository to your local machine.
2. Edit line 11 from update.py and replace it with your game path like the example.

3. Open a terminal or command prompt and navigate to the directory where you have saved the script.

4. Run the script using Python:

`python updater.py` or `python3 updater.py`

5. If your lazy, use the bat file for updating. You can make a shortcut to your desktop if you like.

## How it works
The script will connect to the official ElvUI repository on GitHub and download the latest version of the addon.
It will extract the downloaded ZIP file and update your ElvUI installation by replacing the existing files with the new ones.

Remember to have your world of warcraft client closed before running the script, as it may cause issues if the game is running.

## Contributing
🔥 Pull requests are welcome. 

For major changes, please open an issue first to discuss what you would like to change.

## License
👍 [MIT](https://choosealicense.com/licenses/mit/) - Feel free to share, work with it or clone to your own repository!

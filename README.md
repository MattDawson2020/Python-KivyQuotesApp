## 🐍 Python-Kivy quotes app

- Sixth example project from [Udemy course](https://www.udemy.com/course/the-python-mega-course/)
- Uses Kivy library to create a simple app that can later easily be converted to anAndoird or IOS device
- Design is primarily based around mobile user but is also usable for PC
- Libraries used: kivy, json, datetime, glob, pathlib, random. Also includes hoverable module for button hover behaviours


## 📓 Comments

- Kivy library makes mobile based design very easy, as you can design and position widgets on the page with little code
- Small amount of code creates an already very usable and easily customizable template, without the need for extensive HTML and CSS
- Overall styling is not close to what I would consider final, but I have kept it as it was to demonstrate what can be done in about two hours by someone with no experience in the library
- I am not too keen on the use of a json file for the users and txt files for the quotes, preferring to use a DB. This is most likely done by the instructor to minimize the difficulty of making the app portable to other OS
- Android version of the app works correctly via the APK file. The course creator says that doing so on a Windows/Mac is extremely difficulty at times and so walked me through using an Oracle virtual machine to run a localized version of Ubunutu/Linux in order to use the ``` buildozer ``` library to build an android version
- IOS version is supposedly only able to be made using a Mac, which I currently do not have, will revisit in future 


## 💻 Running the app

- Clone this repo to your local machine, navigate to the directory, and then use ``` python main.py  ``` to run the application
- The window will popup on your screen, letting you interact with the app
- Alternatively if you wish to try the mobile version, download the ```myapp-0.1-arm64-v8a-debug.apk ``` file from the bin directory to your mobile device, and let the installer create a fully functioning mobile version. If you are struggling use a free service like ```https://www.file.io/``` to create a downloadable link
- If you choose the mobile version simply tap the icon to load and use the app




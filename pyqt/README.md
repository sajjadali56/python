# Ste 1

```sh
$ python -m venv venv
$ source venv/bin/activate
(venv) $ python -m pip install pyqt6
```

# Ste 2

```sh
pip3 install PyInstaller
pyinstaller app.py
pyinstaller app.spec
```

# 

Type this code to navigate to the folder containing the ui file and convert the .ui file to a .py file:

```sh
cd "your/ui/folder/here"
pyuic5 mainDialog.ui -o mainDialog.py
```

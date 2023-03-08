pause
python -m build
python -m twine upload --repository PyperText dist/*
start deleteDist.exe
pause
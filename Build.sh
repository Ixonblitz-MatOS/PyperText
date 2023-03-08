python -m build
python -m twine upload --repository PyperText dist/*
rmdir ./dist
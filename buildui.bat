@echo off

IF "%1" == "clean" (
    del roadr_editor\main.py
    del roadr_editor\settings.py
) ELSE (
    pyuic5 roadr_editor\main.ui -o roadr_editor\main.py
    pyuic5 roadr_editor\settings.ui -o roadr_editor\settings.py
)
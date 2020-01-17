# Timetable

## Setup

Install tkinter:

- `sudo apt-get install python3-tk`

Install rtm-cli

https://github.com/dwaring87/rtm-cli

Create / edit crontab file:

- `crontab -e`

Finally follow instructions for crontab

## Crontab

```sh
#m h * * days | message dialog
20 8 * * 1,4 export DISPLAY=:0 && gnome-terminal --maximize -- bash -c "cd ~/timetable; clear; python3 main.py <argument>; exit;exec bash;"
```

## To Do

- [ ] System icon tray
- [ ] Avoid run if no internet connection
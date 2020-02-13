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
20 8 * * 1,4 export DISPLAY=:0 && gnome-terminal --maximize -- bash -c "cd ~/timetable; clear; python3 main.py <subject> <interface>; exit;exec bash;"
#m h * * days | timer
35 8 * * 1,4 export DISPLAY=:0 && cd ~/timetable; python3 main.py <subject> <interface> <elapsed_time>
```

## To Do

- [ ] System icon tray
- [ ] Avoid run if no internet connection
- [ ] Excecute graph after timer but hide console
- [ ] Fix bug, rtm command not found

# pendulo

# Run website

```bash
start_web_app.sh
```

# Logs

To debug, you can run the below command to check what is going on:

```bash
tail -f logs/app.log
```

# Adding the website to the boot sequence

This will allow the website running after a reboot.
The following commands are meant to **run only one time**:

1.
```bash
sudo cp -rf start_web_app.sh /etc/init.d/
```

2.
```bash
sudo chmod +x /etc/init.d/start_web_app.sh
```

3.
```bash
sudo update-rc.d start_web_app.sh defaults
```

4.
Add this to the `crontab` file:

Run :
```bash
crontab -e
```

And then append this to the file: `@reboot ~/pendulo/start_web_app.sh`

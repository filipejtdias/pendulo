# pendulo

# Install (first time only)

- Create/Set user as sudo and remove check for password. [ref](https://www.raspberrypi.org/documentation/linux/usage/users.md)
- Set some commands to run without prompting sudo password. [ref](https://stackoverflow.com/questions/21659637/how-to-fix-sudo-no-tty-present-and-no-askpass-program-specified-error)    

```bash
dias ALL = NOPASSWD: ALL
```

```bash
make install
```

# Pull updates
```bash
make git-update
```

# Run website

```bash
make start
```

# Logs

To debug, you can run the below command to check what is going on:

```bash
tail -f logs/app.log
```

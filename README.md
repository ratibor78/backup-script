# Backup Script

A simple Python script for creating backups of selected files and folders using a configuration file. This script uses Python's built-in modules to provide a lightweight and easy-to-use solution for automating backups.

## Features
- Supports backup of multiple files and directories.
- Outputs backups as `.zip` files with timestamp as name.
- Fully customizable via a simple configuration file.
- Works on Linux, macOS, and possible on Windows(not tested).

## Requirements
- Python 3.x or higher.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/backup-script.git
   cd backup-script
   ```

2. Ensure you have Python installed:
   ```bash
   python3 --version
   ```

## Usage
### 1. Manual Execution
1. Create or edit the configuration file (`config.ini`) to specify the files and directories to back up:
   ```ini
   [source]
   paths = /path/to/folder1, /path/to/file1

   [destination]
   path = /path/to/backup/destination
   ```

2. Run the script manually:
   ```bash
   python3 backup.py -c config.ini
   ```

3. The backup will be created as a `backup_timestamp.zip` file in the specified destination directory, with a timestamp in the filename.

---

### 2. Scheduling Backups with `cron`
You can use `cron` to schedule backups at regular intervals (e.g., daily, hourly).

#### Example: Schedule a daily backup at 2 AM
1. Edit the `crontab` file:
   ```bash
   crontab -e
   ```

2. Add the following line to schedule the script:
   ```bash
   0 2 * * * /usr/bin/python3 /path/to/backup-script/backup.py -c /path/to/config.ini
   ```

   - Replace `/usr/bin/python3` with the path to your Python interpreter (`which python3` to find it).
   - Replace `/path/to/backup-script/backup.py` and `/path/to/config.ini` with the actual paths to your script and configuration file.

3. Save and exit the editor. The backup will now run daily at 2 AM.

---


### Configuration File Example
```ini
[source]
paths = /home/user/documents, /home/user/file.txt

[destination]
path = /tmp/backup
```

---

## Error Handling
- The script will skip invalid or non-existent paths and display a warning.
- If the configuration file is missing or malformed, an appropriate error message will be displayed.

---

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

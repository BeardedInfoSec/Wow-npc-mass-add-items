# Wow-npc-mass-add-items
# GM Command Item Adder Script

This script automates the process of adding items to a character in World of Warcraft Classic, The Burning Crusade, or Wrath of the Lich King using the GM command `.additem`. The script was designed to run with SPP Classics. The script prompts the user to enter Wowhead URLs for items to be added, cleans the URLs, removes duplicates, and generates a list of GM commands to add the items to the target character.

## Dependencies

This script requires the following Python modules to be installed:

- `pyautogui`
- `pyperclip`
- `os`
- `time`
- `mysql.connector`
- `getpass4`

## How to use the script for adding items to WoW characters and vendors

1. Navigate to wowhead.com
2. Open up the gear you want to add to your character or vendor in separate tabs.
3. Run the script `npc_additem.py`
4. The script will copy all the URLs and extract the item and spell IDs.
5. Select if you want to add the items to a vendor or character.
6. Log in to World of Warcraft and target either a character or a vendor.
7. The script will then add the items to the target.
8. Note that the player must be a game master (GM) to use this script.

Note that the script cleans up the temporary `cleaned_list.txt` file it generates during the process of generating the GM commands.

## Limitations

This script has the following limitations:

- The Wowhead URLs must be for items in World of Warcraft Classic, The Burning Crusade, or Wrath of the Lich King.
- The character must have GM privileges and the ability to use the `.additem` and `.npc additem` command.
- The script assumes that the character is targeting the NPC that will be used to add the items to the character. If the character is not targeting the NPC, the script will not work.
- The script may not work correctly if the Wowhead URLs are not formatted correctly or if there are errors in the input file.


##Edit SQL DB From External Computer

##Opening Firewall Ports
open firewall on machine to allow port 3310

##Edit SPP-Database.ini to allow external traffic
Open ./SPP_Classics_V2/SPP_Server/Server\Database/SPP-Database.ini

[mysqld]
port=3310
key_buffer_size=16M
max_allowed_packet=256M
bind-address=0.0.0.0

##MySQL Account Creation
Log in to the MySQL server using the MySQL command-line client or another MySQL client tool.
Grant privileges to the user you are using to connect. For example, you can use the following command to grant all privileges to the user 'myuser' on all databases:
sql

GRANT ALL PRIVILEGES ON *.* TO 'myuser'@'COMPUTERNAME' IDENTIFIED BY 'mypassword';

GRANT ALL PRIVILEGES ON *.* TO 'myuser'@'COMPUTERNAME' IDENTIFIED BY 'mypassword';
Replace 'myuser', 'mypassword', and 'COMPUTERNAME' with your actual username, password, and IP address. If you want to limit the privileges to specific databases or tables, you can modify the command accordingly.
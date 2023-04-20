# Wow-npc-mass-add-items
# GM Command Item Adder Script

This script automates the process of adding items to a character in World of Warcraft Classic, The Burning Crusade, or Wrath of the Lich King using the GM command `.additem`. The script prompts the user to enter Wowhead URLs for items to be added, cleans the URLs, removes duplicates, and generates a list of GM commands to add the items to the target character.

## Dependencies

This script requires the following Python modules to be installed:

- `pyautogui`
- `pyperclip`
- `os`
- `time`

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

# Wow-npc-mass-add-items
# GM Command Item Adder Script

This script automates the process of adding items to a character in World of Warcraft Classic, The Burning Crusade, or Wrath of the Lich King using the GM command `.additem`. The script prompts the user to enter Wowhead URLs for items to be added, cleans the URLs, removes duplicates, and generates a list of GM commands to add the items to the target character.

## Dependencies

This script requires the following Python modules to be installed:

- `pyautogui`
- `time`
- `os`

## Usage

1. Create a text file named `item_list.txt` in the same directory as the script.
2. Add Wowhead URLs for the items you want to add, one per line, to the `item_list.txt` file.
3. Run the script.
4. Enter `1` to indicate that you have finished adding items to the `item_list.txt` file.
5. Enter the GM command (`.additem`) to be used to add the items to the character.
6. Review the command you entered and confirm it is correct.
7. If necessary, target the NPC that will be used to add the items to the character.
8. Wait for the script to execute the GM commands and add the items to the character.

Note that the script cleans up the temporary `cleaned_list.txt` file it generates during the process of generating the GM commands.

## Limitations

This script has the following limitations:

- The Wowhead URLs must be for items in World of Warcraft Classic, The Burning Crusade, or Wrath of the Lich King.
- The target character must have GM privileges and the ability to use the `.additem` command.
- The script assumes that the character is targeting the NPC that will be used to add the items to the character. If the character is not targeting the NPC, the script will not work.
- The script may not work correctly if the Wowhead URLs are not formatted correctly or if there are errors in the input file.

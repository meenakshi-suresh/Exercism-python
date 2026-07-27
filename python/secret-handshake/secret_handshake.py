"""This module implements the secret handshake based on a binary string input. 
The handshake consists of a series of commands that correspond to specific binary digits. 
The commands are as follows:
- 1: "wink"
- 10: "double blink"
- 100: "close your eyes"
- 1000: "jump"
If the first bit of the binary string is set (1), the order of the commands is reversed. 
The function `commands` takes a binary string as input and returns a list of commands
based on the secret handshake rules.
"""
def commands(binary_str):
    """
    Given a binary string, return a list of commands based on the secret handshake rules.

    Args:
        binary_str (str): A string representing a binary number.

    Returns:
        list: A list of commands corresponding to the binary string.
    """
    # Define the mapping of binary digits to commands
    command_mapping = {
        '1': 'wink',
        '10': 'double blink',
        '100': 'close your eyes',
        '1000': 'jump'
    }

    # Initialize an empty list to store the commands
    handshake_commands = []

    # Iterate through the binary string in reverse order
    for i in range(len(binary_str)):
        if binary_str[-(i + 1)] == '1':
            # Get the corresponding command based on the position
            command = command_mapping.get('1' + '0' * i)
            if command:
                handshake_commands.append(command)

    # If the first bit is set, reverse the order of commands
    if binary_str[0] == '1':
        handshake_commands.reverse()

    return handshake_commands

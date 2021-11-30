"""
Helper messages that will be used throughout

Author: Christian M. Fulton
Date: 01.Nov.2021
"""
from enum import Enum
from colorama import init, Fore, Style


init(autoreset=True)

# idea for color convention hierarchy
# acknowledge(green) -> mention(cyan) -> notify(yellow) -> error(lightred) -> fatal(magenta)
class Message(Enum):
    """
    Messages used in production
    """
    ##########
    # ERRORS #
    ##########
    dir_exists_err = (
        lambda dirname: Fore.LIGHTRED_EX + f'Warning, {dirname} already exists!'
    )
    write_data_err = (
        lambda data, fname: Fore.LIGHTRED_EX + f'Unable to write {data[:20].rstrip()}... to {fname}.'
    )
    missing_elem_err = (
        lambda err: Fore.MAGENTA + f'Fatal error: No such element: {err}! Aborting...'
    )

    ###########
    # SUCCESS #
    ###########
    write_file_com = (
        lambda fname, dirname: Fore.GREEN + f'{fname} successfully saved to {dirname}!'
    )
    write_data_com = (
        lambda data, fname: Fore.CYAN + f'Successfully wrote {data[:20].rstrip()}... to {fname}.'
    )
    extract_com = (
        lambda data: Fore.GREEN + f'Data successfully extracted from {data}.'
    )
    
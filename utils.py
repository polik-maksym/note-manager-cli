#
#
#
#
###############################################################################

from datetime import datetime

def generate_id()-> str:
    return datetime.now().strftime("%Y%m%d%H%M%S%f")


def get_timestamp()-> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def parse_tags(tags_input: str)-> list[str]:
    return list(
        dict.fromkeys(
                tag.strip()
                for tag in tags_input.split(",")
                if tag.strip()
        )
    )



def make_separator(length: int = 40, char: str = "-" )-> str:
    """
    Повертає рядок-роздільник.

    Args:
        length: довжина роздільника.
        char: символ роздільника.
    Returns:
        Рядок із символів char.
    """
    return char * length

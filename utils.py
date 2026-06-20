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



def make_separator(text: str, min_length: int = 40, char_sep: str = "-" )-> str:
    """
    повертає роздільник, довжина якого дорівнює довжині тексту,
    але не менше за min_length
    text - для визначення line_length
    """
    line_length = max(min_length, len(text))
    return char_sep * line_length

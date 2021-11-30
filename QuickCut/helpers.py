"""
Helper functions

Author:Christian M. Fulton
"""


def verify_eng(e):
    """
    verify eng str?
    This is a WIP and probably won't even carry over production
    """
    pattern = re.compile('^\w{3}.\d{8}$')
    num_pattern = re.compile('\d{8}')
    res = pattern.match(e)
    # more and more...


def verify_data(d):
    """
    Verify dict data returns values
    ... It seems that this would typically go in tests
    """
    NotImplementedError


# just when you thought there weren't any true helpers...
class FromDict:
    def __init__(self,d):
        for k, v in d.items():
            setattr(self, k, v)
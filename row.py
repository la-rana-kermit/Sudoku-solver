class Row(object):
    """
    Class that represent single sudoku row
    """

    row = None

    def __init__(self, row):
        """
        Class constructor that represent single sudoku row

        :param row: Row identifier

        :type row: int
        """
        self.row = row

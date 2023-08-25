class Column(object):
    """
    Class that represent single sudoku column
    """

    column = None

    def __init__(self, column):
        """
        Class constructor that represent single sudoku column

        :param column: Column identifier

        :type column: int
        """
        self.column = column

class Row(object):
    """
    Class that represent single sudoku row
    """

    row: list = []

    def __init__(self, row_id: int):
        """
        Class constructor that represent single sudoku row

        :param row_id: Row identifier

        :type row_id: int
        """
        self.row_id = row_id

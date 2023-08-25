class Subgrid(object):
    """
    Class that represent single sudoku subgrid
    """

    subgrid = None

    def __init__(self, subgrid_row, subgrid_column):
        """
        Class constructor that represent single sudoku subgrid

        :param subgrid_row: Row identifier
        :param subgrid_column: Column identifier

        :type subgrid_row: int
        :type subgrid_column: int
        """
        self.subgrid_row = subgrid_row
        self.subgrid_column = subgrid_column

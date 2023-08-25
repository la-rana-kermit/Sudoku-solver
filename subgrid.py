class Subgrid(object):
    """
    Class that represent single sudoku subgrid
    """

    subgrid: list = []

    def __init__(self, subgrid_row_id: int, subgrid_column_id: int):
        """
        Class constructor that represent single sudoku subgrid

        :param subgrid_row_id: Row identifier
        :param subgrid_column_id: Column identifier

        :type subgrid_row_id: int
        :type subgrid_column_id: int
        """
        self.subgrid_row_id = subgrid_row_id
        self.subgrid_column_id = subgrid_column_id

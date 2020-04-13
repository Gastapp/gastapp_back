class ImputNotJsonException(Exception):

    def __str__(self):
        return "The input is not JSON formatted"

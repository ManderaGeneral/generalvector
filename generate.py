
from generallibrary import Log

from generalpackager import Packager

if __name__ == "__main__":
    Log("root").configure_stream(level=20)
    Packager("generalvector").generate_localfiles(print_out=20)


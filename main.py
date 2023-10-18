from os import listdir, path
from os.path import isfile


def convert_header(file_path: str):
    print(f"Converting file {file_path}")
    # See: https://www.edfplus.info/specs/edf.html
    # Offset of startdate is 8 + 80 + 80 = 168 ASCII characters
    startdate_offset: int = 168
    # The startdate is 8 ascii characters long
    startdate_end: int = startdate_offset + 8
    with open(file_path, 'rb+') as f:
        # Only read the first 500 bytes of the file, we don't need the rest
        header = f.read(500)
        startdate = str(header[startdate_offset:startdate_end])
        print(f"Startdate: {startdate}")
        new_startdate = "01.01.23"
        # The new start date must be exactly 8 characters long
        assert len(new_startdate) == 8
        
        print(f"Overwriting start date with '{new_startdate}'")
        # Go back to the beginning of the startdate in the header
        f.seek(startdate_offset)
        # Write back the new date
        f.write(str.encode(new_startdate, "ascii"))


if __name__ == '__main__':
    files_dir: str = "/Users/jonasfrey/Documents/_Docs/Masterarbeit/Rohdaten"
    files: list[str] = [f for f in listdir(files_dir) if isfile(path.join(files_dir, f)) and f.lower().endswith(".edf")]
    for file in files:
        convert_header(path.join(files_dir, file))

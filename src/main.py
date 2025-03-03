from src.splitter import Splitter

#################### Attributes ####################
supported_formats = ["YOLO 1.1"]

#################### Methods ####################
def get_splitter(format) -> Splitter:
    if format == "YOLO 1.1":
        from .YOLO.yolo11splitter import YOLO11Splitter
        return YOLO11Splitter()
    
#################### Main ####################
if __name__ == "__main__":
    # Allow the user to select the dataset format
    print("Supported dataset formats:")
    for i, format in enumerate(supported_formats):
        print(f"{i + 1}. {format}")
    format = input("Select the dataset format (type the number): ")
    if format.isnumeric() and 1 <= int(format) <= len(supported_formats):
        splitter = get_splitter(supported_formats[int(format) - 1])
        splitter.split_dataset("data")
    else:
        print("Invalid format selected. Terminating...")
from src.splitter import Splitter

#################### Attributes ####################
supported_formats = ["YOLO 1.1"]

#################### Methods ####################
def get_splitter(format) -> Splitter:
    if format == "YOLO 1.1":
        from src.YOLO.yolo11splitter import YOLO11Splitter
        return YOLO11Splitter()
    
#################### Main ####################
if __name__ == "__main__":
    # Allow the user to select the dataset format
    print("Supported dataset formats:")
    for i, format in enumerate(supported_formats):
        print(f"{i + 1}. {format}")
    format = input("Select the dataset format (type the number): ")
    folder_name = input("Enter the dataset folder name: ")
    train_ratio = input("Enter the training set ratio (default is 0.7): ")
    val_ratio = input("Enter the validation set ratio (default is 0.2): ")
    test_ratio = input("Enter the test set ratio (default is 0.1): ")
    seed = input("Enter the random seed (default is 42): ")

    if format.isnumeric() and 1 <= int(format) <= len(supported_formats):
        splitter = get_splitter(supported_formats[int(format) - 1])
        splitter.split_dataset(folder_name, float(train_ratio) if train_ratio else 0.7, float(val_ratio) if val_ratio else 0.2, float(test_ratio) if test_ratio else 0.1,  int(seed) if seed else 42)
    else:
        print("Invalid format selected. Terminating...")
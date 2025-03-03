import os
import random
from src.splitter import Splitter
from src.splitValidator import validateSplit

class YOLO11Splitter(Splitter):
    def split_dataset(self, folder_name: str, train_ratio: float = 0.7, val_ratio: float = 0.2, test_ratio: float = 0.1, seed: int = None):
        # If seed is provided, shuffle; otherwise, keep order
        if seed is not None:
            random.seed(seed)

        # Validate the split ratios
        if not validateSplit(train_ratio, val_ratio, test_ratio): 
            raise ValueError("Invalid split ratios. Terminating...")
        
        base_path = os.path.join('data', folder_name)
        if not os.path.exists(base_path):
            raise FileNotFoundError(f"Directory {base_path} not found.")

        # Paths
        data_path = os.path.join(base_path, 'obj_train_data')

        if not os.path.exists(data_path):
            raise FileNotFoundError(f"Directory {data_path} not found.")

        train_txt = os.path.join(base_path, 'train.txt')
        val_txt = os.path.join(base_path, 'valid.txt')
        test_txt = os.path.join(base_path, 'test.txt')
        
        # Collect all image files
        images = [f for f in os.listdir(data_path) if f.endswith(('.jpg', '.png', '.jpeg', '.JPG', '.PNG', '.JPEG'))]
        
        if seed is not None:
            random.shuffle(images)
        
        # Split indices
        total = len(images)
        train_count = int(total * train_ratio)
        val_count = int(total * val_ratio)
        
        train_files = images[:train_count]
        val_files = images[train_count:train_count + val_count]
        test_files = images[train_count + val_count:]
        
        def write_filelist(filename, files):
            with open(filename, 'w') as f:
                for file in files:
                    img_path = os.path.join(data_path, file)
                    f.write(f"{img_path}\n")
        
        write_filelist(train_txt, train_files)
        write_filelist(val_txt, val_files)
        write_filelist(test_txt, test_files)
        
        print(f"Dataset split: {len(train_files)} train, {len(val_files)} val, {len(test_files)} test")
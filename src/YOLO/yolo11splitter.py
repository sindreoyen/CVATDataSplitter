import os
import random
from src.splitter import Splitter

class YOLO11Splitter(Splitter):
    def split_dataset(base_path, train_ratio=0.7, val_ratio=0.2, test_ratio=0.1, seed=None):
        # If seed is provided, shuffle; otherwise, keep order
        if seed is not None:
            random.seed(seed)
        
        # Paths
        data_path = os.path.join(base_path, 'obj_train_data')

        if not os.path.exists(data_path):
            raise FileNotFoundError(f"Directory {data_path} not found.")

        train_txt = os.path.join(base_path, 'train.txt')
        val_txt = os.path.join(base_path, 'valid.txt')
        test_txt = os.path.join(base_path, 'test.txt')
        
        # Collect all image files
        images = [f for f in os.listdir(data_path) if f.endswith(('.jpg', '.png'))]
        
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
                    base_name = os.path.splitext(file)[0]
                    img_path = os.path.join('obj_train_data', file)
                    txt_path = os.path.join('obj_train_data', base_name + '.txt')
                    f.write(f"{img_path}\n")
                    if os.path.exists(os.path.join(data_path, base_name + '.txt')):
                        f.write(f"{txt_path}\n")
        
        write_filelist(train_txt, train_files)
        write_filelist(val_txt, val_files)
        write_filelist(test_txt, test_files)
        
        print(f"Dataset split: {len(train_files)} train, {len(val_files)} val, {len(test_files)} test")
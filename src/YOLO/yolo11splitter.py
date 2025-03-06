import os
import shutil
import random
from src.splitter import Splitter
from src.splitValidator import validateSplit

class YOLO11Splitter(Splitter):
    def __init__(self):
        super().__init__()

    def split_dataset(self, folder_name: str, train_ratio: float = 0.7, val_ratio: float = 0.2, test_ratio: float = 0.1, seed: int = None):
        if seed is not None:
            random.seed(seed)

        if not validateSplit(train_ratio, val_ratio, test_ratio): 
            raise ValueError("Invalid split ratios. Terminating...")
        
        base_path = os.path.join('data', folder_name)
        new_base_path = os.path.join('data', f'{folder_name}_new')
        if not os.path.exists(base_path):
            raise FileNotFoundError(f"Directory {base_path} not found.")
        os.makedirs(new_base_path, exist_ok=True)

        # Paths for train, valid, test
        subsets = ['train', 'valid', 'test']
        for subset in subsets:
            os.makedirs(os.path.join(new_base_path, subset, 'images'), exist_ok=True)
            os.makedirs(os.path.join(new_base_path, subset, 'labels'), exist_ok=True)

        data_path = os.path.join(base_path, 'obj_train_data')
        if not os.path.exists(data_path):
            raise FileNotFoundError(f"Directory {data_path} not found.")

        images = [f for f in os.listdir(data_path) if f.endswith(('.jpg', '.png', '.jpeg', '.JPG', '.PNG', '.JPEG'))]
        if seed is not None:
            random.shuffle(images)

        total = len(images)
        train_count = int(total * train_ratio)
        val_count = int(total * val_ratio)
        
        train_files = images[:train_count]
        val_files = images[train_count:train_count + val_count]
        test_files = images[train_count + val_count:]
        
        def move_files(files, subset):
            for file in files:
                shutil.copy(os.path.join(data_path, file), os.path.join(new_base_path, subset, 'images', file))
                annotation = file.rsplit('.', 1)[0] + '.txt'
                annotation_path = os.path.join(data_path, annotation)
                if os.path.exists(annotation_path):
                    shutil.copy(annotation_path, os.path.join(new_base_path, subset, 'labels', annotation))
        
        move_files(train_files, 'train')
        move_files(val_files, 'valid')
        move_files(test_files, 'test')
        
        def write_filelist(filename, files, subset):
            with open(filename, 'w') as f:
                for file in files:
                    f.write(f"data/newfolder/{subset}/images/{file}\n")
        
        write_filelist(os.path.join(new_base_path, 'train.txt'), train_files, 'train')
        write_filelist(os.path.join(new_base_path, 'valid.txt'), val_files, 'valid')
        write_filelist(os.path.join(new_base_path, 'test.txt'), test_files, 'test')

        shutil.copy(os.path.join(base_path, 'obj.names'), os.path.join(new_base_path, 'obj.names'))
        with open(os.path.join(new_base_path, 'obj.data'), 'w') as f:
            f.write("classes= 1\ntrain  = data/train.txt\nvalid  = data/valid.txt\ntest = data/test.txt\nnames = data/obj.names\nbackup = backup/")
        
        print(f"Dataset split and reorganized: {len(train_files)} train, {len(val_files)} val, {len(test_files)} test")

# YOLO 1.1 – From CVAT documentation [(link)](https://docs.cvat.ai/docs/manual/advanced/formats/format-yolo/)

### The folder with the data should have the following structure for the YOLO 1.1 format from CVAT.

##### If you notice any errors here, please submit an issue.

```
folder/
├── obj.data
├── obj.names
├── obj_<subset>_data
│   ├── image1.txt
│   └── image2.txt
└── train.txt # list of subset image paths


# the only valid subsets are: train, valid
# train.txt and valid.txt:
obj_<subset>_data/image1.jpg
obj_<subset>_data/image2.jpg

# obj.data:
classes = 3 # optional
names = obj.names
train = train.txt
valid = valid.txt # optional
backup = backup/ # optional

# obj.names:
cat
dog
airplane

# image_name.txt:
# label_id - id from obj.names
# cx, cy - relative coordinates of the bbox center
# rw, rh - relative size of the bbox
# label_id cx cy rw rh
1 0.3 0.8 0.1 0.3
2 0.7 0.2 0.3 0.1

```

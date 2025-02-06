import os
import cv2
import numpy as np
import albumentations as A
from glob import glob
import pyfiglet
from termcolor import colored

start = pyfiglet.figlet_format("START")
color_start = colored(start, "blue")
finish = pyfiglet.figlet_format("FINISH")
color_finish = colored(finish, "red")


def create_output_folder(output_path):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

def load_images_from_folder(folder_path):
    return glob(os.path.join(folder_path, "*.jpg"))  # Modify extension as needed

def get_augmentations():
    return [
        A.HorizontalFlip(p=1),
        A.VerticalFlip(p=1),
        A.RandomRotate90(p=1),
        A.ShiftScaleRotate(shift_limit=0.05, scale_limit=0.05, rotate_limit=30, p=1),
        # A.GaussNoise(var_limit=(10.0, 50.0), p=1),
        # A.GaussNoise(var_limit={"low": 10.0, "high": 50.0}, p=1),
        A.MotionBlur(blur_limit=5, p=1),
        A.MedianBlur(blur_limit=5, p=1),
        A.RandomBrightnessContrast(brightness_limit=0.2, contrast_limit=0.2, p=1),
        A.CLAHE(clip_limit=2, p=1),
        A.InvertImg(p=1)
    ]

def apply_augmentations(image, augmentations):
    return [aug(image=image)['image'] for aug in augmentations]

def save_images(images, base_filename, output_folder):
    for idx, img in enumerate(images):
        save_path = os.path.join(output_folder, f"{base_filename}_aug{idx}.jpg")
        cv2.imwrite(save_path, img)

def process_images(input_folder, output_folder):
    create_output_folder(output_folder)
    image_paths = load_images_from_folder(input_folder)
    augmentations = get_augmentations()
    
    for img_path in image_paths:
        img = cv2.imread(img_path)
        if img is None:
            continue
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        aug_images = apply_augmentations(img, augmentations)
        base_name = os.path.splitext(os.path.basename(img_path))[0]
        save_images(aug_images, base_name, output_folder)

if __name__ == "__main__":
    input_folder = "인풋 폴더 경로"
    output_folder = "결과 폴더 경로"
    print(color_start)
    process_images(input_folder, output_folder)
    print(color_finish)
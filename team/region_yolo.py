# region_counter.py
from ultralytics import solutions

def create_region_counter(region_points, model_path, classes=None):
    return solutions.RegionCounter(
        # show=True,
        region=region_points,
        model=model_path,
        classes=classes
    )

def count_objects(region_counter, frame):
    return region_counter.count(frame)

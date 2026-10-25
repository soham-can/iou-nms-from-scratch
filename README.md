
# IoU and Non-Maximum Suppression (NMS)

## Overview
This project implements Intersection over Union (IoU) and
greedy Non-Maximum Suppression (NMS) from scratch using Python.

It explores how bounding-box overlap is measured and how
redundant detections are removed using confidence scores and
an IoU threshold.

## Objectives
- Understand bounding-box coordinates.
- Implement IoU without relying on an existing implementation.
- Implement greedy NMS using the custom IoU function.
- Visualize overlapping and retained bounding boxes.
- Study the effect of different IoU thresholds.
- Validate the algorithms using automated tests.

## Technologies
- Python
- NumPy
- Pandas
- Matplotlib
- OpenCV
- pytest
- Jupyter Notebook

## Project Structure
- `data/`: Synthetic bounding-box dataset and sample image.
- `notebooks/`: Step-by-step experiments and visualizations.
- `src/iou.py`: IoU implementation.
- `src/nms.py`: Greedy NMS implementation.
- `src/visualization.py`: Visualization utilities.
- `tests/`: Automated tests for IoU and NMS.

## Intersection over Union (IoU)
IoU measures the overlap between two bounding boxes.

IoU = Intersection Area / Union Area

An IoU of 0 indicates no overlap, while an IoU of 1
indicates identical boxes.

## Non-Maximum Suppression (NMS)
Greedy NMS reduces redundant detections by:
1. Sorting boxes by confidence score.
2. Selecting the highest-confidence remaining box.
3. Calculating its IoU with the other candidates.
4. Suppressing candidates whose IoU exceeds the threshold.
5. Repeating until no candidates remain.

This implementation uses class-agnostic suppression.

## Experiments
The project compares IoU thresholds of 0.3, 0.5, 0.7,
0.8, and 0.85.

For the included six-box example:
- Thresholds 0.3, 0.5, and 0.7 retain 3 boxes.
- Threshold 0.8 retains 5 boxes.
- Threshold 0.85 retains 6 boxes.

These results demonstrate that increasing the threshold
makes suppression less aggressive for this example.

## Testing
Run the automated tests from the project root:

```bash
python -m pytest -v
```

The current test suite contains 10 tests covering identical,
non-overlapping, partially overlapping, nested, and touching
boxes, as well as NMS suppression and basic edge cases.

## Limitations
- The dataset contains synthetic detections.
- No object detection model is trained in this project.
- NMS is class-agnostic.
- Test coverage is not exhaustive.

## Conclusion
This project demonstrates the geometric basis of IoU and
the role of greedy NMS in removing redundant object detections.
These concepts are foundational to object detection pipelines,
including YOLO-based systems.

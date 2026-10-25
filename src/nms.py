import numpy as np

def iou(box1, box2):
    x1, y1, x2, y2 = box1
    x3, y3, x4, y4 = box2

    intersection_area = max(0, min(x2, x4) - max(x1, x3)) * max(0, min(y2, y4) - max(y1, y3))
    box1_area = (x2 - x1) * (y2 - y1)
    box2_area = (x4 - x3) * (y4 - y3)

    return intersection_area / (box1_area + box2_area - intersection_area)

def nms(boxes,score,iou_threshold=0.5):
    boxes=np.asanyarray(boxes,dtype=np.float32)
    scores=np.asarray(score,dtype=np.float32)
    if len(boxes)==0:
        return []
    if boxes.ndim != 2 or boxes.shape[1] != 4:
        raise ValueError("Each box must contain four coordinates.")

    if len(boxes) != len(scores):
        raise ValueError("Each box must have one confidence score.")

    if not 0 <= iou_threshold <= 1:
        raise ValueError("IoU threshold must be between 0 and 1.")
    order = np.argsort(scores)[::-1]

    keep = []
    while len(order) > 0:
        i = order[0]
        keep.append(i)

        if len(order) == 1:
            break

        ious = np.array([iou(boxes[i], boxes[j]) for j in order[1:]])

        order = order[1:][ious <= iou_threshold]

    return [int(idx) for idx in keep]

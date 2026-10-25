def iou(box_a, box_b):
    intersection_x1 = max(box_a[0], box_b[0])
    intersection_y1 = max(box_a[1], box_b[1])
    intersection_x2 = min(box_a[2], box_b[2])
    intersection_y2 = min(box_a[3], box_b[3])

    intersection_area = (
        max(0, intersection_x2 - intersection_x1)
        * max(0, intersection_y2 - intersection_y1)
    )

    area_a = (
        (box_a[2] - box_a[0])
        * (box_a[3] - box_a[1])
    )

    area_b = (
        (box_b[2] - box_b[0])
        * (box_b[3] - box_b[1])
    )

    union_area = area_a + area_b - intersection_area

    if union_area <= 0:
        return 0.0

    return intersection_area / union_area


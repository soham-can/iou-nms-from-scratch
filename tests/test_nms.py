from src.nms import nms


def test_nms_suppresses_overlapping_boxes():
    boxes = [
        (100, 100, 250, 250),
        (110, 110, 245, 245),
        (500, 350, 600, 500)
    ]
    scores = [0.95, 0.88, 0.83]

    assert nms(boxes, scores, 0.5) == [0, 2]


def test_nms_empty_input():
    assert nms([], [], 0.5) == []

def test_nms_single_box():
    boxes = [(100, 100, 200, 200)]
    scores = [0.9]

    assert nms(boxes, scores, 0.5) == [0]


def test_nms_keeps_non_overlapping_boxes():
    boxes = [
        (100, 100, 200, 200),
        (300, 300, 400, 400)
    ]
    scores = [0.9, 0.8]

    assert nms(boxes, scores, 0.5) == [0, 1]


def test_nms_threshold_zero():
    boxes = [
        (100, 100, 200, 200),
        (110, 110, 210, 210)
    ]
    scores = [0.9, 0.8]

    assert nms(boxes, scores, 0.0) == [0]

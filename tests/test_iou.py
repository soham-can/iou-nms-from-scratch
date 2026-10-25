
from src.iou import iou


def test_identical_boxes():
    box = (100, 100, 250, 250)
    assert iou(box, box) == 1.0


def test_non_overlapping_boxes():
    box_a = (100, 100, 200, 200)
    box_b = (300, 300, 400, 400)
    assert iou(box_a, box_b) == 0.0


def test_partial_overlap():
    box_a = (100, 100, 250, 250)
    box_b = (150, 150, 300, 300)
    assert abs(iou(box_a, box_b) - 0.2857142857) < 1e-6

def test_one_box_inside_another():
    outer = (100, 100, 300, 300)
    inner = (150, 150, 250, 250)

    assert iou(outer, inner) == 0.25


def test_touching_boxes():
    box_a = (100, 100, 200, 200)
    box_b = (200, 100, 300, 200)

    assert iou(box_a, box_b) == 0.0

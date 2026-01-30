def get_center_of_bbox(bbox):
    """
    Given a bounding box in the format [x1, y1, x2, y2],
    return the center point (cx, cy).
    """
    x1, y1, x2, y2 = bbox
    cx = (x1 + x2) / 2
    cy = (y1 + y2) / 2
    return int(cx), int(cy)

def get_bbox_width(bbox):
    """
    Given a bounding box in the format [x1, y1, x2, y2],
    return the width of the bounding box.
    """
    x1, y1, x2, y2 = bbox
    width = x2 - x1
    return int(width)

def measure_distance(point1, point2):
    """
    Measure Euclidean distance between two points.
    Each point is a tuple (x, y).
    """
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5

def measure_xy_distance(point1, point2):
    """
    Measure the distance in x and y directions between two points.
    Each point is a tuple (x, y).
    Returns a tuple (dx, dy).
    """
    dx = point2[0] - point1[0]
    dy = point2[1] - point1[1]
    return dx, dy

def get_foot_position(bbox):
    """
    Given a bounding box in the format [x1, y1, x2, y2],
    return the foot position (center of bottom edge).
    """
    x1, y1, x2, y2 = bbox
    return int((x1 + x2) / 2), int(y2)
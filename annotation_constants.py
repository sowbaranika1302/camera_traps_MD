"""
annotation_constants.py

Shared constants used to interpret annotation output


Categories assigned to bounding boxes.  Used throughout our repo; do not change unless
you are Dan or Siyu.  In fact, do not change unless you are both Dan *and* Siyu.

We use integer indices here; this is different than the API output .json file,
where indices are string integers.
"""

NUM_DETECTOR_CATEGORIES = 23  # this is for choosing colors, so ignoring the "empty" class

# This is the label mapping used for our incoming iMerit annotations
# Only used to parse the incoming annotations. In our database, the string name is used to avoid confusion
# MegaDetector outputs
detector_bbox_categories = [
   {"name": "Bird", "id": 0},
    {"name": "Eastern Gray Squirrel", "id": 1},
    {"name": "Eastern Chipmunk", "id": 2},
    {"name": "Woodchuck", "id": 3},
    {"name": "Wild Turkey", "id": 4},
    {"name": "White-Tailed Deer", "id": 5},
    {"name": "Virginia Opossum", "id": 6},
    {"name": "Eastern Cottontail", "id": 7},
    {"name": "Vehicle", "id": 9},
    {"name": "Striped Skunk", "id": 10},
    {"name": "Red Fox", "id": 11},
    {"name": "Eastern Fox Squirrel", "id": 12},
    {"name": "Northern Raccoon", "id": 13},
    {"name": "Grey Fox", "id": 14},
    {"name": "Horse", "id": 15},
    {"name": "Dog", "id": 16},
    {"name": "American Crow", "id": 17},
    {"name": "Chicken", "id": 18},
    {"name": "Domestic Cat", "id": 19},
    {"name": "Coyote", "id": 20},
    {"name": "Bobcat", "id": 21},
    {"name": "American Black Bear", "id": 22}
]

detector_bbox_category_id_to_name = {}
detector_bbox_category_name_to_id = {}

for cat in detector_bbox_categories:
    detector_bbox_category_id_to_name[cat['id']] = cat['name']
    detector_bbox_category_name_to_id[cat['name']] = cat['id']

"""
annotation_constants.py

Shared constants used to interpret annotation output


Categories assigned to bounding boxes.  Used throughout our repo; do not change unless
you are Dan or Siyu.  In fact, do not change unless you are both Dan *and* Siyu.

We use integer indices here; this is different than the API output .json file,
where indices are string integers.
"""
import os
model_variant = os.environ.get('MODEL_TYPE', '0')

if model_variant == "2":
    NUM_DETECTOR_CATEGORIES = 23
  # this is for choosing colors, so ignoring the "empty" class
    annotation_bbox_categories = [
        {'id': 1, 'name': 'bird'},
        {'id': 2, 'name': 'eastern gray squirrel'},
        {'id': 3, 'name': 'eastern chipmunk'},
        {'id': 4, 'name': 'woodchuck'},
        {'id': 5, 'name': 'wild turkey'},
        {'id': 6, 'name': 'white-tailed deer'},
        {'id': 7, 'name': 'virginia opossum'},
        {'id': 8, 'name': 'eastern cottontail'},
        {'id': 9, 'name': 'empty'},
        {'id': 10, 'name': 'vehicle'},
        {'id': 11, 'name': 'striped skunk'},
        {'id': 12, 'name': 'red fox'},
        {'id': 13, 'name': 'eastern fox squirrel'},
        {'id': 14, 'name': 'northern raccoon'},
        {'id': 15, 'name': 'grey fox'},
        {'id': 16, 'name': 'horse'},
        {'id': 17, 'name': 'dog'},
        {'id': 18, 'name': 'american crow'},
        {'id': 19, 'name': 'chicken'},
        {'id': 20, 'name': 'domestic cat'},
        {'id': 21, 'name': 'coyote'},
        {'id': 22, 'name': 'bobcat'},
        {'id': 23, 'name': 'american black bear'}
    ]

    # MegaDetector outputs
    detector_bbox_categories = [
        {'id': 1, 'name': 'bird'},
        {'id': 2, 'name': 'eastern gray squirrel'},
        {'id': 3, 'name': 'eastern chipmunk'},
        {'id': 4, 'name': 'woodchuck'},
        {'id': 5, 'name': 'wild turkey'},
        {'id': 6, 'name': 'white-tailed deer'},
        {'id': 7, 'name': 'virginia opossum'},
        {'id': 8, 'name': 'eastern cottontail'},
        {'id': 9, 'name': 'empty'},
        {'id': 10, 'name': 'vehicle'},
        {'id': 11, 'name': 'striped skunk'},
        {'id': 12, 'name': 'red fox'},
        {'id': 13, 'name': 'eastern fox squirrel'},
        {'id': 14, 'name': 'northern raccoon'},
        {'id': 15, 'name': 'grey fox'},
        {'id': 16, 'name': 'horse'},
        {'id': 17, 'name': 'dog'},
        {'id': 18, 'name': 'american crow'},
        {'id': 19, 'name': 'chicken'},
        {'id': 20, 'name': 'domestic cat'},
        {'id': 21, 'name': 'coyote'},
        {'id': 22, 'name': 'bobcat'},
        {'id': 23, 'name': 'american black bear'}
        ]
# This is the label mapping used for our incoming iMerit annotations
# Only used to parse the incoming annotations. In our database, the string name is used to avoid confusion
else:
    NUM_DETECTOR_CATEGORIES = 3
    annotation_bbox_categories = [
        {'id': 0, 'name': 'empty'},
        {'id': 1, 'name': 'animal'},
        {'id': 2, 'name': 'person'},
        {'id': 3, 'name': 'group'},  # group of animals
        {'id': 4, 'name': 'vehicle'}
    ]

    # MegaDetector outputs
    detector_bbox_categories = [
        {'id': 0, 'name': 'empty'},
        {'id': 1, 'name': 'animal'},
        {'id': 2, 'name': 'person'},
        {'id': 3, 'name': 'vehicle'}
    ]

annotation_bbox_category_id_to_name = {}
annotation_bbox_category_name_to_id = {}

for cat in annotation_bbox_categories:
    annotation_bbox_category_id_to_name[cat['id']] = cat['name']
    annotation_bbox_category_name_to_id[cat['name']] = cat['id']

detector_bbox_category_id_to_name = {}
detector_bbox_category_name_to_id = {}

for cat in detector_bbox_categories:
    detector_bbox_category_id_to_name[cat['id']] = cat['name']
    detector_bbox_category_name_to_id[cat['name']] = cat['id']

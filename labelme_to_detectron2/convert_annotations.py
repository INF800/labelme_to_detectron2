import sys
import json
from pathlib import Path
from tqdm import tqdm

from labelme_to_detectron2.convert_annotation import convert_to_d2 

annotation_dir = Path(sys.argv[1])
labelme_annotations = annotation_dir.glob("*.json")
labelme_annotations = sorted([*labelme_annotations])

suffix = "d2json"

print('Finding unique labels')
unique_labels = set()
for annotation in tqdm(labelme_annotations):
    with annotation.open() as f:
        data = json.load(f)
    for shape in data["shapes"]:
        unique_labels.add(shape["label"])

unique_labels = sorted(list(unique_labels))
print('unique labels:', unique_labels)

print('converting:')
for path in tqdm(labelme_annotations):
    with open(path, "r") as f:
        ann = json.load(f)
        ann_d2 = convert_to_d2(ann, unique_labels)
        
        out_path = path.parent / (path.stem + "." + suffix)
        with open(out_path, "w") as f:
            json.dump(ann_d2, f, indent=4)
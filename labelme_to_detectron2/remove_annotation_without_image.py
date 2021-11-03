import os
import sys
from pathlib import Path
from pprint import pprint

annotation_dir = Path(sys.argv[1])
labelme_annotations = annotation_dir.glob("*.json")
images = annotation_dir.glob("*.jpg")

labelme_annotations = sorted([*labelme_annotations])
images = sorted([*images])

image_names = [str(image.stem) for image in images]
annot_names = [str(annotation.stem) for annotation in labelme_annotations]

image_names = set(image_names)
annot_names = set(annot_names)

print("Images:", len(image_names))
print("Annotations:", len(annot_names))

pprint("Images missing annotations:")
pprint(image_names-annot_names)

pprint("Annotation missing images:")
pprint(annot_names-image_names)

pprint('Removing annotations missing images')
annots_without_images = sorted(list(annot_names - image_names))
for name in annots_without_images:
    path = annotation_dir / (name+'.json')
    print(f"Removing {path}")
    os.remove(path)

pprint('Removed!')
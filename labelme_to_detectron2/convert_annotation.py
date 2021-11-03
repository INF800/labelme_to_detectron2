from pathlib import Path
import numpy as np

def convert_to_d2(annot, unique_labels):
  record = dict()
  record["file_name"] = Path(annot['imagePath']).name # add base path later in the loop
  record["image_id"] = None # fill later in the loop
  record["height"] = annot['imageHeight']
  record["width"] = annot['imageWidth']
  
  shapes = annot["shapes"]
  objs = []
  for shape in shapes:
      label_name = shape['label']
      label_id = unique_labels.index(label_name)
      poly = shape['points']
      poly = np.array(poly)
      px = poly.T[0]
      py = poly.T[1]
      poly = [(x + 0.5, y + 0.5) for x, y in zip(px, py)]
      poly = [p for x in poly for p in x]
      obj = {
          "bbox": [np.min(px), np.min(py), np.max(px), np.max(py)],
          "bbox_mode": 0, # detecton2.structures.BoxMode.XYXY_ABS,
          "segmentation": [poly],
          "category_id": label_id,
      }
      objs.append(obj)
  
  record["annotations"] = objs
  return record

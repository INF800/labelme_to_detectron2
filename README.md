# labeleme_to_detectron2

Convert labelme annotations to detectron2 annotation format.


**USAGE:**

```
python -m labelme_to_detectron2.convert_annotations {labelme_annotations_dir}
```

Copy the unique labels that will be displayed.

Files will be created in `*.d2json` format (same as json)

Divide into train and test datasets and then register dataset using the code below:

```python
from pathlib import Path

unique_labels=['person', 'vehicle']
def get_dataset_dicts(img_dir):
    dataset_dicts = []
    img_dir = Path(img_dir)
    for i, jsonpath in enumerate([*img_dir.glob("*.d2json")]):
      with open(str(jsonpath), 'r') as fp:
        annot = json.load(fp)
        annot['image_id'] = i
        annot['file_name'] = str(img_dir/Path(annot['file_name']).name) 
        
        dataset_dicts.append(annot)
    
    return dataset_dicts

for d in ["train", "test"]:
    DatasetCatalog.register("dataset_" + d, lambda d=d: get_dataset_dicts(f"{base}/{d}"))
    MetadataCatalog.get("dataset_" + d).set(thing_classes=unique_labels)
```


### Insatallation

Install locally with sym-link for fast code updates
```
pip install -e .
```

Generate distributable file
```
python3 setup.py sdist
```
Can install using: `pip install https://github.com/INF800/labelme_to_detectron2/raw/main/dist/labelme_to_detectron2-x.x.x.tar.gz`

Share distributable using pypi
```
twine upload dist/* 
```

import json
import os
import argparse
from shutil import copyfile

def append_json(args):
    with open(args.original_COCO_file, 'r') as f:
        original_coco = json.load(f)
    
    with open(args.your_COCO_file, 'r') as g:
        your_coco = json.load(g)

    num = int(args.numbers)
    labels = args.labels
    results = {'person': 0,'car': 0,'truck': 0}
    print(results)
    total_num = 0
    print(labels)
    
    for annotation in original_coco['annotations']:
        this_annot = [cat['name'] for cat in original_coco['categories'] if cat['id'] == annotation['category_id']][0]
        print(this_annot)
        if this_annot not in labels:
            continue
        if results[this_annot] >= num:
            continue
        if annotation['image_id'] <= 219:
            continue
        
        results[this_annot] += 1
        total_num += 1
        annotation['id'] = 1387 + total_num
        your_coco['annotations'].append(annotation)

        for image in original_coco['images']:
            if image['id'] == annotation['image_id']:
                filename = [image['file_name']][0]
                if filename not in os.listdir(args.custom_image_folder):
                    copyfile(args.COCO_image_folder + filename, args.custom_image_folder + filename)
                    your_coco['images'].append(image)
    
    with open(args.appended_COCO_file, 'w') as output:
        json.dump(your_coco, output, indent=4)


    

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--original_COCO_file', help='The COCO annotation file downloaded from COCO website')
    parser.add_argument('--your_COCO_file', help='The COCO file to be appended')
    parser.add_argument('--COCO_image_folder', help='The COCO photos folder downloaded from COCO website')
    parser.add_argument('--labels', help='The labels in the original COCO file to be appended')
    parser.add_argument('--numbers', help='The number of each labels to be appended from the original COCO')
    parser.add_argument('--appended_COCO_file', help='The COCO file where the result is saved')
    parser.add_argument('--custom_image_folder', help='The folder in which image files are saved')

    args = parser.parse_args()

    append_json(args)
    print("WARNING: THE CATAGORY ID IS NOT CHANGED! PLZ MODIFY IT MANUALLY!")

if __name__ == '__main__':
    main()


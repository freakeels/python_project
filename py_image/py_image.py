import cv2
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import glob

_file_name = 'test.mp4'
_thumbnail_number = 15
_preview_x_num = 3
_preview_y_num = 5
_thumb_size_x = 300
_thumb_size_y = 200
_thumb_gap_x = 50
_thumb_gap_y = 20
_preview_x_total = _thumb_size_x * _preview_x_num + _thumb_gap_x * (_preview_x_num+1)
_preview_y_total = _thumb_size_y * _preview_y_num + _thumb_gap_y * (_preview_y_num+1)
_cap_init_frame = 1000

def create_thumbnails(video_src, thumbnail_number):
    thumbnails = []

    if not video_src.isOpened():
        print "could not open :",_file_name
        return

    length = int(video_src.get(cv2.CAP_PROP_FRAME_COUNT))
    capture_gap = int(length / thumbnail_number)

    video_src.set(cv2.CAP_PROP_POS_FRAMES, _cap_init_frame)

    success, image = video_src.read()
    count = 0

    while success and (count < length):
        video_src.set(cv2.CAP_PROP_POS_FRAMES, count+_cap_init_frame)
        success, image = video_src.read()
        thumbnails.append(image)
        count += capture_gap

    return thumbnails

def output_thumb_images(thumbnail_list, thumbnail_number):
    for i in range(thumbnail_number):
        cv2.imwrite("frame%06d.jpg" % i, thumbnail_list[i])     # save frame as JPEG file

def create_thumbnail_preview(thumbnails, thumbnail_number):
    top_image = Image.new("RGB", (_preview_x_total, _preview_y_total), "white")

    for y in range(thumbnail_number/_preview_x_num):
        for x in range(thumbnail_number/_preview_y_num):
            cv_image = cv2.cvtColor(thumbnails[y*_preview_x_num + x],cv2.COLOR_BGR2RGB)
            pil_image = Image.fromarray(cv_image)
            pil_image.thumbnail((_thumb_size_x, _thumb_size_y), Image.ANTIALIAS)
            thumb_pos_x = _thumb_gap_x * (x+1) + _thumb_size_x * x
            thumb_pos_y = _thumb_gap_y * (y+1) + _thumb_size_y * y
            top_image.paste(pil_image, ( thumb_pos_x , thumb_pos_y), None)

    # draw = ImageDraw.Draw(top_image)
    # font = ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", 36)
    # draw.text((0, 0),"Sample Text", (0, 0, 0), font=font)
    return top_image

def main():
    for video_name in glob.glob('/Users/hsuchih-kao/Downloads/Video/*.avi'):
        print video_name
        video_src = cv2.VideoCapture(video_name)
        thumbnails = create_thumbnails(video_src, _thumbnail_number)
        thumbnail_preview = create_thumbnail_preview(thumbnails, _thumbnail_number)
        thumbnail_preview.save(video_name.split('.')[0]+"_result.jpg")


if __name__ == '__main__':
    main()
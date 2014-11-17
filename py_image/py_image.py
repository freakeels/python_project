import cv2

file_name = 'test.mp4'

def main():
    cap = cv2.VideoCapture(file_name)

    if not cap.isOpened():
        print "could not open :",file_name
        return

    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    capture_gap = int(length / 16)

    success, image = cap.read()
    count = 0

    while success and (count < length):
        cap.set(cv2.CAP_PROP_POS_FRAMES, count)
        success, image = cap.read()
        cv2.imwrite("frame%06d.jpg" % count, image)     # save frame as JPEG file
        count += capture_gap

if __name__ == '__main__':
    main()
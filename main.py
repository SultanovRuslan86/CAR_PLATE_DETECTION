import matplotlib.pyplot as plt
import pytesseract
import cv2
import easyocr

def open_img(img_path):
    carplate_img = cv2.imread(img_path)
    carplate_img = cv2.cvtColor(carplate_img, cv2.COLOR_BGR2RGB)
    plt.axis('off')
    plt.imshow(carplate_img)
    # plt.show()

    return carplate_img

def carplate_extract(image, carplate_haar_cascade):
    carplate_rects = carplate_haar_cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5)

    for x, y, w, h, in carplate_rects:
        carplate_img = image[y+15:y+h-10, x+15:x+w-20]

    return carplate_img

def enlarge_img(image, scale_percent):
    width = int(image.shape[1] * scale_percent/100)
    height = int(image.shape[0] * scale_percent/100)
    dim = (width, height)
    plt.axis('off')
    recized_image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

    return recized_image

def text_recogniton(file_path):
    reader = easyocr.Reader(["ru", "en"])
    result = reader.readtext(file_path, detail=0)
    return result

def main():
    carplate_img_rgb = open_img(img_path='/Users/ruslan/PycharmProjects/CAR_PLATE_DETECTION/cars/4.jpg')
    carplate_haar_cascade = cv2.CascadeClassifier('/Users/ruslan/PycharmProjects/CAR_PLATE_DETECTION/haar_cascades/haarcascade_russian_plate_number.xml')

    carplate_extract_img = carplate_extract(carplate_img_rgb, carplate_haar_cascade)
    carplate_extract_img = enlarge_img(carplate_extract_img, 150)
    plt.imshow(carplate_extract_img)
    # plt.show()

    carplate_extract_img_gray = cv2.cvtColor(carplate_extract_img, cv2.COLOR_RGB2GRAY)
    plt.axis('off')
    plt.imshow(carplate_extract_img_gray, cmap='gray')
    plt.show()

    file_path = carplate_extract_img_gray
    print('Номер автомобиля: ', *text_recogniton(file_path=file_path))





    # print('Номер автомобиля: ', text_recogniton())

    # print('Номер автомобиля: ', pytesseract.image_to_string(
    #     carplate_extract_img_gray,
    #     config='--psm 6 --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    # )


if __name__ == '__main__':
    main()

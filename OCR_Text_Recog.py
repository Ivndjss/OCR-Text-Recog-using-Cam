import cv2
from PIL import Image
import pytesseract

def main():
    camera = cv2.VideoCapture(0)

    while True:
        _, image = camera.read()
        cv2.imshow('image', image)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            cv2.imwrite('test1.jpg', image)
            break

    camera.release()
    cv2.destroyAllWindows()

    def tesseract():
        path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        image_path = "test1.jpg"
        pytesseract.pytesseract.tesseract_cmd = path_to_tesseract
        text = pytesseract.image_to_string(Image.open(image_path))
        print(text)

    tesseract()

if __name__ == '__main__':
    main()

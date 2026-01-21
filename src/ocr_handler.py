from rapidocr_onnxruntime import RapidOCR

class OCRHandler:
    def __init__(self):
        # Initialize RapidOCR with default options
        # use_det=True (Detection), use_cls=False (Orientation), use_rec=True (Recognition)
        self.ocr_engine = RapidOCR()

    def extract_text(self, image_path_or_bytes):
        """
        Extract text from an image.
        Returns the combined text string.
        """
        try:
            result, elapse = self.ocr_engine(image_path_or_bytes)
            if not result:
                return ""
            
            # Result is a list of [box, text, confidence]
            extracted_text = "\n".join([line[1] for line in result])
            return extracted_text.strip()
        except Exception as e:
            print(f"OCR Error: {e}")
            return ""

if __name__ == "__main__":
    # Simple test
    print("Initializing OCR Engine...")
    ocr = OCRHandler()
    print("OCR Engine Ready.")

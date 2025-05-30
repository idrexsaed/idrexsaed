import os
from pdfminer.high_level import extract_text

def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extracts text from a PDF file.

    Args:
        pdf_path: The path to the PDF file.

    Returns:
        The extracted text as a single string, or an empty string if an error occurs.
    """
    try:
        # Check if the file exists
        # While extract_text might also raise FileNotFoundError,
        # checking it explicitly allows for a more specific message
        # or handling before attempting to parse.
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"Error: The file '{pdf_path}' was not found.")
        
        text = extract_text(pdf_path)
        return text
    except FileNotFoundError as e:
        print(e)
        return ""
    except Exception as e:
        print(f"An error occurred during PDF parsing: {e}")
        return ""

if __name__ == '__main__':
    # Example usage (optional, for testing purposes)
    # Create a dummy PDF file for testing if you don't have one.
    # For example, using a library like ReportLab, or just use an existing PDF.
    # This part is commented out as it requires a PDF file to exist.
    # test_pdf_path = "example.pdf" 
    # if not os.path.exists(test_pdf_path):
    #     print(f"Note: Test PDF file '{test_pdf_path}' not found. Skipping example run.")
    # else:
    #     print(f"Extracting text from '{test_pdf_path}'...")
    #     extracted_content = extract_text_from_pdf(test_pdf_path)
    #     if extracted_content:
    #         print("\nExtracted Content:\n")
    #         print(extracted_content[:500] + "..." if len(extracted_content) > 500 else extracted_content)
    #     else:
    #         print("No content extracted or an error occurred.")
    pass

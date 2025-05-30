import re

def clean_text(raw_text: str) -> str:
    """
    Cleans raw text by normalizing whitespace and replacing common ligatures.

    Args:
        raw_text: The input string to clean.

    Returns:
        The cleaned text string.
    """
    if not isinstance(raw_text, str):
        # Handle cases where input is not a string, though type hinting should help
        print("Warning: clean_text received non-string input. Returning as is.")
        return str(raw_text) # Attempt to convert, or handle error differently

    # Replace common ligatures
    text = raw_text.replace("ﬁ", "fi")
    text = text.replace("ﬂ", "fl")
    text = text.replace("ﬀ", "ff")
    text = text.replace("ﬃ", "ffi")
    text = text.replace("ﬄ", "ffl")
    
    # Replace multiple whitespace characters (including newlines, tabs, etc.) with a single space
    text = re.sub(r'\s+', ' ', text)
    
    # Remove leading and trailing whitespace
    text = text.strip()
    
    return text

if __name__ == '__main__':
    # Example Usage
    sample_text_with_ligatures = "A ﬁne ﬂoating aﬀair, with diﬃcult ﬄuctuations."
    sample_text_with_whitespace = "  Hello   World\nNext\tLine\r\nAnother  \f Formfeed "
    
    print(f"Original (ligatures): '{sample_text_with_ligatures}'")
    cleaned_ligatures = clean_text(sample_text_with_ligatures)
    print(f"Cleaned (ligatures): '{cleaned_ligatures}'\n")
    
    print(f"Original (whitespace): '{sample_text_with_whitespace}'")
    cleaned_whitespace = clean_text(sample_text_with_whitespace)
    print(f"Cleaned (whitespace): '{cleaned_whitespace}'\n")

    combined_text = "Here is a ﬁle with ﬂaws and much    \n whitespace. Also ﬀ, ﬃ, ﬄ."
    print(f"Original (combined): '{combined_text}'")
    cleaned_combined = clean_text(combined_text)
    print(f"Cleaned (combined): '{cleaned_combined}'\n")

    empty_text = ""
    print(f"Original (empty): '{empty_text}'")
    cleaned_empty = clean_text(empty_text)
    print(f"Cleaned (empty): '{cleaned_empty}'\n")

    whitespace_only_text = "   \n\t  \r "
    print(f"Original (whitespace only): '{whitespace_only_text}'")
    cleaned_whitespace_only = clean_text(whitespace_only_text)
    print(f"Cleaned (whitespace only): '{cleaned_whitespace_only}'\n")

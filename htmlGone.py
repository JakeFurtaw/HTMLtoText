from bs4 import BeautifulSoup

def remove_html_tags(html):
    soup = BeautifulSoup(html, 'html.parser')
    # Extract text from the HTML and remove leading/trailing whitespace
    text = soup.get_text(strip=True)
    return text

def fix_links(links):
    fixed_links = []
    for text, link in links:
        if link.startswith('/'):
            # Add 'towson.edu' to links that start with '/'
            fixed_link = f"https://towson.edu{link.strip()}"
        else:
            fixed_link = link.strip()
        fixed_links.append((text.strip(), fixed_link))
    return fixed_links

def extract_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    # Find all <a> tags
    links = soup.find_all('a')
    # Extract href attribute from each <a> tag along with the text it was extracted from
    link_text_list = [(link.get_text(strip=True), link.get('href')) for link in links]
    return link_text_list

def main():
    # Input file containing HTML content
    input_file = "Faculty_Staff Search-i - Towson University.html"
    # Output file where cleaned text and links will be stored
    output_file = "Faculty_Staff Search-i - Towson University_Cleaned.txt"

    try:
        with open(input_file, "r", encoding="utf-8") as file:
            html_content = file.read()

        # Remove HTML tags and leading/trailing whitespace
        cleaned_text = remove_html_tags(html_content)

        # Extract links along with the text they were extracted from
        link_text_list = extract_links(html_content)
        
        # Fix links and remove leading/trailing whitespace
        fixed_links = fix_links(link_text_list)

        # Write cleaned text and links to output file
        with open(output_file, "w", encoding="utf-8") as file:
            file.write("Cleaned Text with Links:\n\n")
            file.write(cleaned_text + "\n\n")
            file.write("Extracted Links:\n\n")
            for text, link in fixed_links:
                file.write(f"{text}: {link}\n")

        print("HTML tags removed successfully and links extracted. Data saved to", output_file)
    
    except FileNotFoundError:
        print("File not found. Please make sure the input file exists.")

if __name__ == "__main__":
    main()
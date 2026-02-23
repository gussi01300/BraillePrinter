import os
import json

class BRFParser:    
    def __init__(self):
        # BRF standard control characters
        self.page_break = '\f'  # Page break (ASCII 0x0C)
        self.valid_line_breaks = {'\r\n', '\n', '\r'}  # Support all line break types
        self.invalid_chars = {'\x00'}  # Filter null chars to avoid split errors

    def _clean_invalid_chars(self, content):
        """Filter invalid control characters from content"""
        for char in self.invalid_chars:
            content = content.replace(char, '')
        return content

    def _split_content_preserve_order(self, content):
        """
        Split content into [page[lines]] structure, strictly preserve original order
        Keep empty lines/pages without loss
        """
        # Clean invalid characters first
        clean_content = self._clean_invalid_chars(content)
        
        # Split pages by page break (preserve empty pages)
        raw_pages = clean_content.split(self.page_break)
        
        page_lines_list = []
        for page_content in raw_pages:
            # Normalize all line breaks to \n (preserve consecutive line breaks)
            normalized_page = page_content.replace('\r\n', '\n').replace('\r', '\n')
            
            # Split lines (keep empty lines in original order)
            lines = normalized_page.split('\n')
            page_lines_list.append(lines)
        
        return page_lines_list

    def parse_file(self, file_path, encoding='ascii'):
        """
        Parse BRF file, preserve line/page order strictly without duplication
        Return: {page_number: [line1, line2, ...]}
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        # Read in text mode with specified encoding (disable auto line break conversion)
        with open(file_path, 'r', encoding=encoding, newline='') as f:
            content = f.read()
        
        # Split into page-line structure
        page_lines_list = self._split_content_preserve_order(content)
        
        # Build result dict (page number starts from 1)
        page_dict = {}
        for page_num, lines in enumerate(page_lines_list, start=1):
            page_dict[page_num] = lines
        
        return page_dict

    def parse_files(self, file_paths, encoding='ascii'):
        """
        Batch parse BRF files, avoid overwriting due to duplicate filenames
        Return: {file_name: {page_number: [line1, line2, ...]}}
        """
        total_result = {}
        for file_path in file_paths:
            try:
                page_dict = self.parse_file(file_path, encoding)
                file_name = os.path.basename(file_path)
                
                # Add suffix for duplicate filenames to prevent overwriting
                if file_name in total_result:
                    base, ext = os.path.splitext(file_name)
                    counter = 1
                    new_file_name = f"{base}_{counter}{ext}"
                    while new_file_name in total_result:
                        counter += 1
                        new_file_name = f"{base}_{counter}{ext}"
                    file_name = new_file_name
                total_result[file_name] = page_dict
            except Exception as e:
                print(f"Failed to parse {file_path}: {str(e)}")
        return total_result

# Test: Verify order/duplication issues
if __name__ == "__main__":
    parser = BRFParser()
    result = parser.parse_file("blankTemplate.brf")
    print(json.dumps(result, ensure_ascii=False, indent=2))

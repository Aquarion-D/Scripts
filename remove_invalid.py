import re

# File paths (change these paths if necessary)
selector_file_path = r"../lib/selectors/selectorPlaceholders.scss"
snowvision_file_path = r"../src/snowVision.scss"

# Step 1: Extract all placeholders from selectorPlaceholders.scss
valid_placeholders = set()
with open(selector_file_path, 'r', encoding='utf-8') as file:
    content = file.read()
    placeholder_pattern = re.compile(r"(%[\w-]+)")
    valid_placeholders.update(placeholder_pattern.findall(content))

# Step 2: Read snowVision.scss and find placeholders to verify
with open(snowvision_file_path, 'r', encoding='utf-8') as file:
    ww_content = file.read()

# Define a function to remove invalid placeholders
def remove_invalid_placeholders(content, valid_placeholders):
    placeholder_pattern = re.compile(r"(%[\w-]+)")
    
    def placeholder_replacement(match):
        placeholder = match.group(1)
        # Only keep placeholders that exist in the valid list
        return placeholder if placeholder in valid_placeholders else ""
    
    return placeholder_pattern.sub(placeholder_replacement, content)

# Remove invalid placeholders
cleaned_content = remove_invalid_placeholders(ww_content, valid_placeholders)

# Step 3: Save the cleaned content back to snowVision.scss
with open(snowvision_file_path, 'w', encoding='utf-8') as file:
    file.write(cleaned_content)

print("Clean-up complete!")

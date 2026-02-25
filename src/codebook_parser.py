import pdfplumber
import re
import json

def parse_codebook(pdf_path):
    """Parse PSED PDF codebook and return dictionary of variable definitions"""
    codebook = {}

    with pdfplumber.open(pdf_path) as pdf:
        # Loop through each page and extract text
        for page in pdf.pages:
            text = page.extract_text()
            if not text:
                continue  # skip blank pages

            # Split page text into lines for parsing
            lines = text.split('\n')

            #The codebook has two different variable types, continuous and categorical
            #Categorical variables are stored in the data as arbitrary codes which relate to a value (e.g., "1: Yes," "8: Don't Know"
            #With continuous variables, the number IS the value. 
            #In parsing teh codebook, we have to distinguish between values that require translation and values that do not. 

            # track which variable we are currently parsing
            current_vars = []

            for line in lines:
                #This loop detects variable name lines.
                #PSED variable names follow this pattern: letters + digit + optional suffix (e.g., AA4, BE52_W1)
                #Match at line start (^) to distinguish from description with similar text
                var_matches = re.findall(r'([A-Z]+\d[A-Z0-9_]*)', line)
                if var_matches:
                    current_vars = var_matches
                    for v in current_vars:
                        if v not in codebook:
                            codebook[v] = {'codes': {}, 'type': 'categorical'}

                #Detect code-label pairs i.e. "1. Yes" or "5. No")
                #Filters out noise in text by requiring label to start with a letter. 
                code_match = re.search(r'(\d+)\.\s+([A-Za-z].+)', line)
                if code_match and current_vars:
                    code = int(code_match.group(1))
                    label = code_match.group(2).strip()
                    for v in current_vars:
                        codebook[v]['codes'][code] = label

                # Detect continuous variables (example: "Code number of owners")
                if re.search(r'CODE\s+(NUMBER|AMOUNT|PERCENT)', line):
                    for v in current_vars:
                        codebook[v]['type'] = 'continuous'

    return codebook 

#We define the entry point as "__main__" then call the parse_codebook function
#While in main, we write the results of the funciton as ouput in our json dictionary
if __name__ == "__main__":
    result = parse_codebook("data/37202-0003-Codebook-waves_MULTI.pdf")    
    with open("data/codebook.json", "w") as output:
        json.dump(result, output, indent=2)
    print(f"Parsed {len(result)} variables. Saved to data/codebook.json")

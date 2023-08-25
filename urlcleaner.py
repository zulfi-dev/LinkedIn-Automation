def remove_query_params(url):
    if "?" in url:
        return url.split("?")[0]
    return url

input_file_path = "profile_links.txt"
output_file_path = "data_cleaned.txt"

cleaned_urls = []

with open(input_file_path, "r") as input_file:
    for line in input_file:
        url = line.strip()
        cleaned_url = remove_query_params(url)
        cleaned_urls.append(cleaned_url)

# Remove duplicates
unique_cleaned_urls = list(set(cleaned_urls))

with open(output_file_path, "w") as output_file:
    for url in unique_cleaned_urls:
        output_file.write(url + "\n")

print("Processing complete. Cleaned and unique URLs saved in output.txt.")
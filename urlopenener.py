import webbrowser

input_file_path = "data_cleaned.txt"
urls = []

# Read URLs from the output file
with open(input_file_path, "r") as input_file:
    urls = [line.strip() for line in input_file]

for index, url in enumerate(urls):
    print(f"Opening URL {index + 1}/{len(urls)}: {url}")
    webbrowser.open(url)

    # Wait for user input to continue to the next URL
    input("Press Enter to continue to the next URL...")

print("All URLs processed.")

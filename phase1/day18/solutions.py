"""
Day 18: Regular Expressions (Solutions)
"""

import re


# === Exercise 1: Email Validator ===

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}$'
    return bool(re.fullmatch(pattern, email))


# === Exercise 2: Date Extractor ===

def extract_dates(text):
    results = []

    # YYYY-MM-DD
    for m in re.finditer(r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})', text):
        results.append({
            "year": m.group("year"),
            "month": m.group("month"),
            "day": m.group("day"),
        })

    # MM/DD/YYYY
    for m in re.finditer(r'(?P<month>\d{2})/(?P<day>\d{2})/(?P<year>\d{4})', text):
        results.append({
            "year": m.group("year"),
            "month": m.group("month"),
            "day": m.group("day"),
        })

    # DD.MM.YYYY
    for m in re.finditer(r'(?P<day>\d{2})\.(?P<month>\d{2})\.(?P<year>\d{4})', text):
        results.append({
            "year": m.group("year"),
            "month": m.group("month"),
            "day": m.group("day"),
        })

    return results


# === Exercise 3: Text Cleaner ===

def clean_text(text):
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    # Replace multiple spaces/tabs with single space within lines
    text = re.sub(r'[^\S\n]+', ' ', text)
    # Strip each line
    lines = [line.strip() for line in text.splitlines()]
    text = '\n'.join(lines)
    # Remove duplicate blank lines
    text = re.sub(r'\n{3,}', '\n\n', text)
    # Strip leading/trailing whitespace from entire text
    return text.strip()


# === Exercise 4: Log Parser ===

def parse_logs(log_text, level=None):
    pattern = r'\[(?P<timestamp>[^\]]+)\]\s+(?P<level>\w+):\s+(?P<message>.+)'
    results = []
    for match in re.finditer(pattern, log_text):
        entry = {
            "timestamp": match.group("timestamp"),
            "level": match.group("level"),
            "message": match.group("message"),
        }
        if level is None or entry["level"] == level:
            results.append(entry)
    return results


# === Exercise 5: URL Finder ===

def find_urls(text):
    pattern = r'(?P<protocol>https?)://(?P<domain>[^\s/]+)(?P<path>/[^\s]*)?'
    results = []
    for match in re.finditer(pattern, text):
        results.append({
            "full_url": match.group(0),
            "protocol": match.group("protocol"),
            "domain": match.group("domain"),
            "path": match.group("path") or "",
        })
    return results


# === Verification ===

if __name__ == "__main__":
    # Exercise 1
    print("=== Exercise 1: Email Validator ===")
    test_emails = [
        ("user@example.com", True),
        ("first.last+tag@sub.domain.org", True),
        ("invalid@", False),
        ("@domain.com", False),
        ("no spaces@test.com", False),
        ("user@domain.c", False),
        ("test.user@company.co.uk", True),
    ]
    for email, expected in test_emails:
        result = validate_email(email)
        status = "PASS" if result == expected else "FAIL"
        print(f"  {status}: validate_email('{email}') = {result}")

    # Exercise 2
    print("\n=== Exercise 2: Date Extractor ===")
    text = "Born 2024-01-15, moved 03/20/2024, arrived 25.12.2023"
    dates = extract_dates(text)
    for d in dates:
        print(f"  {d['year']}-{d['month']}-{d['day']}")

    # Exercise 3
    print("\n=== Exercise 3: Text Cleaner ===")
    messy = """
    <h1>Title</h1>

    This   has    too   many   spaces.

    <p>And   <b>HTML</b>  tags.</p>



    Multiple    blank    lines   above.
    """
    cleaned = clean_text(messy)
    print(f"Cleaned:\n{cleaned}")

    # Exercise 4
    print("\n=== Exercise 4: Log Parser ===")
    logs = """[2024-01-15 14:30:45] ERROR: Database connection failed (retry: 3)
[2024-01-15 14:30:46] INFO: Retrying connection
[2024-01-15 14:30:47] ERROR: Connection timeout
[2024-01-15 14:30:48] INFO: Connection established
[2024-01-15 14:30:49] WARNING: High memory usage detected"""

    print("All entries:")
    for entry in parse_logs(logs):
        print(f"  [{entry['timestamp']}] {entry['level']}: {entry['message']}")
    print("Errors only:")
    for entry in parse_logs(logs, level="ERROR"):
        print(f"  [{entry['timestamp']}] {entry['message']}")

    # Exercise 5
    print("\n=== Exercise 5: URL Finder ===")
    text = """
    Visit https://www.example.com/path/to/page for details.
    API docs at http://api.service.io/v2/docs.
    Homepage: https://python.org
    """
    for url_info in find_urls(text):
        print(f"  {url_info['protocol']}:// {url_info['domain']} "
              f"-> path: '{url_info['path']}'")

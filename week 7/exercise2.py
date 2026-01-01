import re
import logging
from collections import Counter, defaultdict

# ---------------- LOGGING SETUP ----------------
logging.basicConfig(
    filename="analysis_audit.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ---------------- REGEX FOR APACHE LOGS ----------------
LOG_PATTERN = re.compile(
    r'(?P<ip>\S+) - - \[(?P<time>.*?)\] '
    r'"(?P<method>\S+) (?P<url>\S+) \S+" '
    r'(?P<status>\d{3}) (?P<size>\d+)'
)

# ---------------- ANALYZER CLASS ----------------
class LogAnalyzer:
    def __init__(self, logfile):
        self.logfile = logfile

        # Traffic stats
        self.total_requests = 0
        self.unique_ips = set()
        self.http_methods = Counter()
        self.urls = Counter()
        self.status_codes = Counter()

        # Error + security tracking
        self.errors = []
        self.failed_logins = defaultdict(int)
        self.security_incidents = []

    def parse_line(self, line):
        match = LOG_PATTERN.match(line)
        if not match:
            logging.warning("Malformed log entry skipped")
            return None
        return match.groupdict()

    def analyze_security(self, entry):
        ip = entry["ip"]
        url = entry["url"]
        status = int(entry["status"])

        # Failed login tracking
        if url == "/login" and status == 401:
            self.failed_logins[ip] += 1
            if self.failed_logins[ip] == 3:
                incident = f"Brute force detected from IP {ip}"
                self.security_incidents.append(incident)
                logging.warning(incident)

        # Forbidden access
        if status == 403:
            incident = f"Forbidden access attempt from {ip} to {url}"
            self.security_incidents.append(incident)
            logging.warning(incident)

        # SQL Injection patterns
        sql_patterns = ["select", "union", "drop", "--", ";"]
        if any(p in url.lower() for p in sql_patterns):
            incident = f"Possible SQL injection from {ip}: {url}"
            self.security_incidents.append(incident)
            logging.warning(incident)

    def process_logs(self):
        try:
            with open(self.logfile, "r") as file:
                for line in file:
                    entry = self.parse_line(line.strip())
                    if not entry:
                        continue

                    self.total_requests += 1
                    self.unique_ips.add(entry["ip"])
                    self.http_methods[entry["method"]] += 1
                    self.urls[entry["url"]] += 1
                    self.status_codes[int(entry["status"])] += 1

                    if int(entry["status"]) >= 400:
                        self.errors.append(entry)

                    self.analyze_security(entry)

            logging.info("Log processing completed successfully")

        except FileNotFoundError:
            logging.error("Log file not found")
            raise
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            raise

    def generate_summary_report(self):
        with open("summary_report.txt", "w") as f:
            f.write("=== SERVER LOG SUMMARY ===\n")
            f.write(f"Total Requests: {self.total_requests}\n")
            f.write(f"Unique Visitors: {len(self.unique_ips)}\n\n")

            f.write("HTTP METHODS:\n")
            for method, count in self.http_methods.items():
                f.write(f"{method}: {count}\n")

            f.write("\nMOST REQUESTED URLS:\n")
            for url, count in self.urls.most_common(5):
                f.write(f"{url}: {count}\n")

            f.write("\nSTATUS CODES:\n")
            for code, count in self.status_codes.items():
                f.write(f"{code}: {count}\n")

    def generate_security_report(self):
        with open("security_incidents.txt", "w") as f:
            f.write("=== SECURITY INCIDENTS ===\n")
            for incident in self.security_incidents:
                f.write(incident + "\n")

    def generate_error_log(self):
        with open("error_log.txt", "w") as f:
            f.write("=== HTTP ERRORS ===\n")
            for err in self.errors:
                f.write(
                    f"{err['ip']} {err['method']} {err['url']} "
                    f"Status {err['status']}\n"
                )

# ---------------- MAIN ----------------
def main():
    analyzer = LogAnalyzer("server.log")

    try:
        analyzer.process_logs()
        analyzer.generate_summary_report()
        analyzer.generate_security_report()
        analyzer.generate_error_log()

        print("Analysis complete.")
        print(f"Total requests: {analyzer.total_requests}")
        print(f"Security incidents: {len(analyzer.security_incidents)}")
        print(f"Errors found: {len(analyzer.errors)}")

    except Exception as e:
        print("Analysis failed:", e)

if __name__ == "__main__":
    main()



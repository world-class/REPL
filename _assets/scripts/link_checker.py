"""Simple link checker that will recursively extract URLs from .md files
from the current repository.

Asynchronous features with the help of the following page:
https://stackoverflow.com/a/13530258/8787680
"""
import multiprocessing as mp
import os
import subprocess
import time

# Third-party imports
import requests

FILE_NAME = "dead.txt"  # Will appear if it contains dead links
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"
    )
}

EXCLUDED_WEBSITES = [
    "calendar.google.com",
    "challengerocket.com",
    "https://www.khanacademy.org/math/precalculus/x9e81a4f98389efdf",
    "https://yukaichou.com/gamification-book/",
]

def extract_links(excluded_websites: list) -> list:
    """Extract links from all .md files recursively from the current
    repository."""
    cmd = (
        'cat ../../**/*.md | grep -Eo "(http|https)://[+a-zA'
        '-Z0-9./?=_~-]*" | sort | uniq > links.txt'
    )
    subprocess.run(cmd, shell=True)
    print("Links extracted from repository.")

    sites = []
    with open("links.txt") as f:
        content = f.readlines()
        for line in content:
            excluded = False
            for website in excluded_websites:
                if website in line:
                    print(f"Excluding: {website}")
                    excluded = True
            if not excluded:
                line = line.strip()
                sites.append(line)

    os.unlink("links.txt")
    return sites

def download_site(url, q):
    """Request an URL. If it can properly be retrieved, add it to queue
    `q` so that it gets written to a file with the job manager."""
    global HEADERS
    try:
        with requests.get(url, headers=HEADERS) as response:
            response_length = len(response.content)
            print(f"Current URL: {url}")
            if not response_length or not response.ok:
                if response.status_code != 403:  # ignore blocked requests
                    q.put(f"[{response.status_code}] {url}")
    except:  # Any kind of error occurring
        try:
            q.put(f"[{response.status_code}] {url}")
        except UnboundLocalError:  # response doesn't exist → connection error
            q.put(url)

def check_all_ok(dead_file):
    """Once we have requested all URLs, check if any was found to be
    dead and print them with their specific error code."""
    try:
        with open(dead_file) as f:
            content = f.readlines()
            if not content:  # We get an empty list
                print("No dead link found.")
                os.unlink(dead_file)
            else:
                print("Dead links found:\n")
                for line in content:
                    print(line.strip())
    except FileNotFoundError:
        print(f"<{dead_file}> doesn't exist.")

def listener(q):
    """Listens for messages on the `q`, writes to file."""

    with open(FILE_NAME, "w") as f:
        while True:
            m = q.get()

            # String received, signaling we're done
            if m == "kill":
                break

            f.write(str(m) + "\n")
            f.flush()

def job_manager(sites):
    """The purpose of the job manager is to add "jobs" in a "queue" so
    that at any time only one "job" will be written to a file thanks to
    a "listener" that receives incoming "jobs" from the "queue"."""
    # Must use Manager queue here, or will not work
    manager = mp.Manager()
    q = manager.Queue()
    pool = mp.Pool(mp.cpu_count() + 2)

    # Put listener to work first
    _ = pool.apply_async(listener, (q,))

    # Fire off workers
    jobs = []
    for site in sites:
        job = pool.apply_async(download_site, (site, q))
        jobs.append(job)

    # collect results from the workers through the pool result queue
    for job in jobs:
        job.get()

    # Now we are done, kill the listener
    q.put("kill")
    pool.close()

if __name__ == "__main__":
    SITES = extract_links(EXCLUDED_WEBSITES)  # Generate list of links
    START_TIME = time.time()  # Start timer right before launching job manager

    # Add links as 'jobs' to write dead links to a file
    job_manager(SITES)

    DURATION = time.time() - START_TIME
    print(f"Checked {len(SITES)} in {DURATION:.4f} seconds")

    # Scan through the file that contains dead links. If empty, delete it.
    check_all_ok(FILE_NAME)

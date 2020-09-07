import multiprocessing, csv
from indeed.spiders.reviews import crawler
from pathlib import Path

if __name__ == "__main__":
    filepath = Path("indeed/data_files/urls.csv")
    urls = []
    process_urls = []
    processes = 4

    with open(filepath, "r") as file:
        reader = csv.reader(file)
        print(reader)
        for row in reader:
            urls.append(row[0])

    len = int(len(urls)/processes)

    start_index, end_index = 0, 0
    jobs = []

    crawler(urls=urls, filename="l")

    for proc in range(0, processes):

        end_index += len
        process_urls = urls[start_index:end_index]
        if proc == processes - 1:
            process_urls = urls[start_index:]
        start_index += len

        process = multiprocessing.Process(target=crawler, args=(process_urls, proc))
        jobs.append(process)

    for j in jobs:
        j.start()

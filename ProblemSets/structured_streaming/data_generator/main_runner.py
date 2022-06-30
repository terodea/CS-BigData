from client import DataGenerator
import socket
import time
import argparse


def main(_args=None):

    host = 'localhost'
    port = 12345

    i = 0

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind((host, port))
    s.listen(1)

    try:
        while True:
            conn, addr = s.accept()
            try:
                obj = DataGenerator()
                
                for j in range(10):
                    data = obj._generate_events()
                    print(data)
                    conn.send(bytes("{}\n".format(data), "utf-8"))
                    time.sleep(1)
                conn.close()
            except socket.error: 
                pass
    finally:
        s.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="A data generator utility.",
        usage="python3 main_runner.py --no_of_events 10 --min_salary 500000 --max_salary 700000")
    parser.add_argument("--no_of_events", help="No of data points to generate.", type=int)
    parser.add_argument("--min_salary", help="Min Salary", type=int)
    parser.add_argument("--max_salary", help="Max Salary", type=int)
    _args = vars(parser.parse_args())
    main(_args)

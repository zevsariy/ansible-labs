import argparse
import memcache

def get_key(host):
    connect = memcache.Client([host + ':' + '11211'])
    print(connect.get("filepath").decode('utf-8'))
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('host', help='Host ip address')
    args = parser.parse_args()
    host = args.host
    get_key(host)

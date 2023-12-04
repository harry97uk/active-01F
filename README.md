# active-01F

A simple port scanner, which will tell you if the port is open or closed.

## Usage

```
$>  tinyscanner --help
Usage: tinyscanner [OPTIONS] [HOST] [PORT]
Options:
  -p               Range of ports to scan
  -u               UDP scan
  -t               TCP scan
  --help           Show this message and exit.
$>  tinyscanner -u 20.78.06.364 -p 80
Port 80 is open
$> tinyscanner -t 127.0.0.1 -p 1604
Port 1604 is closed
$> tinyscanner -t 10.53.224.5 -p 80-83
Port 80 is open
Port 81 is open
Port 82 is close
Port 83 is open
```

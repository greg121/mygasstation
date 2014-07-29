#!/bin/bash

curl http://tanken.t-online.de/tankstelle/diesel/519b4914bed7139bf0d43042 -o /root/tanken/output_geisa.txt
curl http://tanken.t-online.de/tankstelle/diesel/519b48babed7139bf0d42513 -o /root/tanken/output.txt
sleep 2
python /root/tanken/script.py
python /root/tanken/script_geisa.py

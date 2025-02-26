#!/bin/bash
while ! curl -s http://localhost:4444; do
    sleep 1
done

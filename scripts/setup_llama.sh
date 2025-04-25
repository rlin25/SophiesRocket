#!/bin/bash
git clone https://github.com/ggerganov/llama.cpp.git
cd llama.cpp
mkdir build && cd build
cmake .. -DLLAMA_CURL=OFF
cmake --build . --config Release

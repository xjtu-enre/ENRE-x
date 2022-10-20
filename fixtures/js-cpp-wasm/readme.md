## https://emscripten.org/docs/getting_started/downloads.html
# Fetch the latest version of the emsdk (not needed the first time you clone)
git pull

# Download and install the latest SDK tools.
./emsdk install latest

# Make the "latest" SDK "active" for the current user. (writes .emscripten file)
./emsdk activate latest

# Activate PATH and other environment variables in the current terminal
source ./emsdk_env.sh


## https://emscripten.org/docs/getting_started/Tutorial.html#tutorial
# 将c转换js和wasm命令
emcc hello_world.c

# 运行命令
node a.out.js







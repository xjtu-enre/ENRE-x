project(node_cpp_addon)
set(CMAKE_CXX_STANDARD 14)
# .node-gyp
include_directories(C:/Users/AppData/Local/node-gyp/Cache/14.8.0/include/node)
include_directories(node_modules/nan)
include_directories(node_modules/node-addon-api)
AUX_SOURCE_DIRECTORY(. CUR_DIR)
add_subdirectory(./lib)
add_executable(node_cpp_addon ${CUR_DIR} napi_example01.cpp)

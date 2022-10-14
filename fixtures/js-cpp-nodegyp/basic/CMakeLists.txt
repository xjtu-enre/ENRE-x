project(javascript_cpp_demo)    //这里是项目名称
set(CMAKE_CXX_STANDARD 14)      //这里是最小CMAKE版本
# .node-gyp
include_directories(C:/Users/AppData/Local/node-gyp/Cache/14.8.0/include/node)  //这里是引入node-gyp的路径
include_directories(node_modules/node-addon-api)
AUX_SOURCE_DIRECTORY(. CUR_DIR)
add_subdirectory(./lib)         //这里是如果用lib库则引入，无可忽略
add_executable(cpp_addon_test main.cpp)     //CMAKE中指定源文件生成执行文件
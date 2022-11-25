#include <stdio.h>
#include </Users/dair/emsdk/upstream/emscripten/cache/sysroot/include/emscripten/emscripten.h>
// 实现一个加法
EMSCRIPTEN_KEEPALIVE
int add(int a,int b) {
    return a+b;
}

// 直接输出
EMSCRIPTEN_KEEPALIVE
void hello(){
    printf("hello/n");
}

// 返回字符
EMSCRIPTEN_KEEPALIVE
char sayhi(){
    return 'a';
}
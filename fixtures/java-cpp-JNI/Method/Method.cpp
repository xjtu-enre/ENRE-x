#include <iostream>
#include <stdio.h>
#include "Method.h"

JNIEXPORT void JNICALL Java_Method_testHello
(JNIEnv*, jclass) {
	std::cout << "common method.." << std::endl;
}
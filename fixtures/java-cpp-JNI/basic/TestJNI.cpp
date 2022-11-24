#include "JNIDemo.h"
#include <iostream>
#include <stdio.h>
JNIEXPORT void JNICALL Java_JNIDemo_testHello
(JNIEnv*, jclass) {
	printf("this is C++ print at 10-17");
}
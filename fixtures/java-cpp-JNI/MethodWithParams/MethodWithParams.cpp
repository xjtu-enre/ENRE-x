#include <iostream>
#include <stdio.h>
#include "MethodWithParams.h"

JNIEXPORT jint JNICALL Java_MethodWithParams_f1
(JNIEnv*, jclass, jint a, jint b) {
	return a + b;
}
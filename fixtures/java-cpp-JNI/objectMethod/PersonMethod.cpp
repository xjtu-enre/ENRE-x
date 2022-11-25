#include <iostream>
#include <stdio.h>
#include "PersonMethod.h"
JNIEXPORT void JNICALL Java_PersonMethod_native_1init
(JNIEnv* env, jobject obj) {
    jclass clazz_person = env->GetObjectClass(obj);
    jmethodID methodID_setName = env->GetMethodID(clazz_person, "setName", "(Ljava/lang/String;)V");
    jstring name = env->NewStringUTF("David");
    env->CallVoidMethod(obj, methodID_setName, name);
    env->DeleteLocalRef(name);
    env->DeleteLocalRef(clazz_person);
}
#include "PersonField.h"
#include <iostream>
#include <stdio.h>
JNIEXPORT void JNICALL Java_PersonField_native_1init
(JNIEnv* env, jobject obj) {
    jclass clazz_person = env->GetObjectClass(obj);
    jfieldID fieldID_mAge = env->GetFieldID(clazz_person, "mAge", "I");
    jint age = env->GetIntField(obj, fieldID_mAge);
    std::cout << "Age: " << age << std::endl;
    env->DeleteLocalRef(clazz_person);
}
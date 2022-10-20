#include <iostream>
#include <stdio.h>
#include <node_api.h>
#define NAPI_CALL(env, call)                                    \
      do {                                                      \
        napi_status status = (call);                            \
        if (status != napi_ok) {                                \
          const napi_extended_error_info* error_info = nullptr; \
          napi_get_last_error_info((env), &error_info);         \
          bool is_pending;                                      \
          napi_is_exception_pending((env), &is_pending);        \
          if (!is_pending) {                                    \
            const char* message = error_info->error_message;    \
            napi_throw_error((env), "ERROR", message);          \
            return nullptr;                                     \
          }                                                     \
        }                                                       \
      } while(0)

napi_value hello(napi_env env, napi_callback_info info) {
  napi_value str = nullptr;
  NAPI_CALL(env, napi_create_string_utf8(env, "hello world", NAPI_AUTO_LENGTH, &str));
  std::cout<<"c++ say: hello world!"<<std::endl;
  return str;
}

void set_function(napi_env env, napi_value* target, const char* name, napi_callback cb) {
  napi_value fn = nullptr;
  napi_create_function(env, name, NAPI_AUTO_LENGTH, cb, nullptr, &fn);
  napi_set_named_property(env, *target, name, fn);
}

napi_value init(napi_env env, napi_value exports) {
  set_function(env, &exports, "hello", hello);
  return exports;
}

NAPI_MODULE(napi_addon01, init)
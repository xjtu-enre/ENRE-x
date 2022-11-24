#include <stdio.h>
#include <emscripten.h>
#include <stdlib.h>
#include <string.h>

int EMSCRIPTEN_KEEPALIVE func_square(int x) 
{
  return x * x;
}

int EMSCRIPTEN_KEEPALIVE func_sum(int x, int y) 
{
  return x + y;
}
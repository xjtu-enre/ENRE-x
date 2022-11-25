#include "pch.h"
#include<stdio.h>
#include<stdlib.h>
using namespace std;
extern"C" {
	struct label {
		bool isnull = true;
	};
	typedef struct alg* algStruct;
	struct alg :label {
		double add;
		double minus;
		double multi;
		double div;
	};

	_declspec(dllexport) algStruct algStructest(double a, double b) {
		algStruct algp = (algStruct)malloc(sizeof(struct alg));
		if (algp) {
			algp->isnull = false;
			algp->add = a + b;
			algp->minus = a - b;
			algp->multi = a * b;
			algp->div = a / b;
		}

		return algp;
	}
}
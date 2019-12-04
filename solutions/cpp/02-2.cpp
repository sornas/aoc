#include<fstream>
#include<iostream>
#include<vector>
#include <chrono>
using namespace std;

int run(vector<int> prog, int noun, int verb, int pointer, int op) {
	vector<int> mem(prog);
	mem[1] = noun;
	mem[2] = verb;

	// calculate
	pointer = 0;
	do {
		//cout << "Pointer: " << pointer << endl;
		//cout << "Memory: " << endl;
		//dump(mem);
		op = mem[pointer];
		switch (op) {
			case 1:
				mem[mem[pointer+3]] = mem[mem[pointer+1]] + mem[mem[pointer+2]];
				pointer += 4;
				break;
			case 2:
				mem[mem[pointer+3]] = mem[mem[pointer+1]] * mem[mem[pointer+2]];
				pointer += 4;
				break;
		}
	} while (mem[pointer] != 99);
	return mem[0];
}

int main() {
	ifstream inFile;
	inFile.open("02.in");

	vector<int> program;
	int noun, verb;
	int pointer;
	int op;

	// read program
	int n;
	while (inFile >> n) program.push_back(n);
	//cout << "Program: " << endl;
	//dump(program);

	int res;

	auto t1 = chrono::high_resolution_clock::now();

	for (int n = 0; n < 100; n++) {
		for (int v = 0; v < 100; v++) {
			res = run(program, n, v, pointer, op);
			//cout << n << " " << v << " " << res << endl;
			if (res == 19690720) {
				cout << n << " " << v << endl;
				auto t2 = chrono::high_resolution_clock::now();
				auto duration = chrono::duration_cast<std::chrono::microseconds>( t2 - t1 ).count();
				cout << duration << endl;
				return 0;
			}
		}
	}
	return 1;
}

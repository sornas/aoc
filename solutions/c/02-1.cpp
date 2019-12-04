#include<fstream>
#include<iostream>
#include<vector>
using namespace std;

int main() {
	ifstream inFile;
	inFile.open("02.in");

	vector<int> program;
	int noun, verb;
	// enter noun, verb
	cin >> noun;
	cin >> verb;
	
	// read program
	int n;
	while (inFile >> n) program.push_back(n);
	program[1] = noun;
	program[2] = verb;
	//cout << "Program: " << endl;
	//dump(program);

	// copy program to mem
	vector<int> mem(program);

	// calculate
	int pointer = 0;
	int op;
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
	cout << mem[0] << endl;
}

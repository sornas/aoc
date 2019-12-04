#include<iostream>

int main() {
	int mass, sum = 0;
	while (std::cin >> mass) sum += (mass / 3) - 2;
	std::cout << sum << std::endl;
}


#include<iostream>

int getFuel(int mass) {
	int fuel = (mass / 3) - 2;
	if (fuel <= 0) return 0;
	return fuel + getFuel(fuel);
}

int main() {
	int mass, sum = 0;
	while (std::cin >> mass) sum += getFuel(mass);
	std::cout << sum << std::endl;
}


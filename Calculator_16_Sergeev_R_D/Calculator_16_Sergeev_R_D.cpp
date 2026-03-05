#include <iostream> // Библиотека для ввода и вывода
#include <string> // Библиотека для работы со строками
#include <sstream> // Библиотека для преобразования строк в числа
#include <iomanip> // Библиотека для форматирования вывода

int  a = 0; 
int b = 0;
int result = 0;
// Функция для ввода 16ти ричного числа, принимает строку подсказку, возращает число в десятичном виде

int inputHex(std::string promt) {
	std::string input;
	int number;
	std::cout << promt;
	getline(std::cin, input);
	std::stringstream ss; // Создаем поток для преобразования строки в число
	ss << std::hex << input; // Записываем строку в поток. "Hex" означает что 16ти ричное число в системе
	ss >> number; // Преобразуем поток в число
	return number;
}

// Функция сложения на ассемблере, принимает 2 числа и возращает их сумму

int addAsm(int x, int y) {
	int result_asm = 0;
	__asm {
		mov eax,x // Загружаем первое число "X" в регистр "eax"
		mov ebx,y // Загружаем второе число "X" в регистр "ebx"
		add eax,ebx // Складываем в "eax"
		mov result_asm,eax // Сохраняем результат из "eax" в переменную 
		// Описываем какие регистры мы используем
	}
	return result_asm;
}


int main()
{
	setlocale(LC_ALL, "Rus");
	std::cout << "======================="<<std::endl;
	std::cout << "Введите числа в HEX (Например: 1F,A3,100)" << std::endl;
	a = inputHex("Введите первое число в HEX:");
	b = inputHex("Введите второе число в HEX:");
	result = addAsm(a, b);

	std::cout << "Результат:" << result;
	return 0;
}
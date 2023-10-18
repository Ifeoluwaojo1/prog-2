#include <cstdlib>
// Person class 
// Reviewer: 
// Student: Ifeoluwa Ojo


class Person{
	public:
		Person(int);
		int fib();
		int get();
		void set(int);
	private:

		int fibonacciRecursive(int);
		int age;
	};
int Person::get(){
		return age;
		}
void Person::set(int n) {
	 	age = n;
}
int Person::fibonacciRecursive(int n){
	if (n <= 1) {
		return n;
	} else {
		return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2);
	}
}

int Person::fib(){
	return fibonacciRecursive(age);
}

Person::Person(int n){
age = n;
}

extern "C"{
	Person* Person_new(int n) {return new Person(n);}
	int Person_get(Person* person) {return person->get();}
	void Person_set(Person* person, int n) {return person->set(n);}
	int Person_fib(Person* person) {return person->fib();}
	void Person_delete(Person* person){
		if (person){
			delete person;
			person = nullptr;
		}
	}
}